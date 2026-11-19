# Дополнительный механизм определения исполнителя и названия песни.
# Дробление на файлы излишне, пока оставляем единым файлом.

import re
import threading
import urllib.request

class ICYMetadata:

    def __init__(self):

        self.title = None

        self._lock = threading.Lock()

        self._thread = None
        self._stop_event = None
        self._response = None

    def start(self, url):

        # Останавливаем предыдущее подключение.
        self.stop()

        # Создаём отдельное событие для нового потока.
        stop_event = threading.Event()

        thread = threading.Thread(
            target=self._listen,
            args=(url, stop_event),
            daemon=True
        )

        with self._lock:

            self.title = None
            self._stop_event = stop_event
            self._thread = thread

        thread.start()

    def stop(self):

        with self._lock:

            stop_event = self._stop_event
            response = self._response
            thread = self._thread

            self._stop_event = None
            self._response = None
            self._thread = None

            self.title = None

        # Отправляем сигнал остановки.
        if stop_event is not None:
            stop_event.set()

        # Закрываем старое соединение.
        if response is not None:

            try:
                response.close()
            except Exception:
                pass

        # Ждём завершения потока.
        if (
            thread is not None
            and thread.is_alive()
            and thread != threading.current_thread()
        ):

            thread.join(timeout=0.1) # Ожидание завершения ICY. Изначально было 2.

    def get_title(self):

        with self._lock:
            return self.title

    def _read_exact(self, response, size, stop_event):

        data = bytearray()

        while len(data) < size:

            if stop_event.is_set():
                return None

            chunk = response.read(
                min(4096, size - len(data))
            )

            if not chunk:
                return None

            data.extend(chunk)

        return bytes(data)

    def _decode_metadata(self, raw):

        for encoding in ("utf-8", "cp1251"):
            try:
                return raw.decode(encoding)
            except UnicodeDecodeError:
                continue

        return raw.decode("latin-1", errors="replace")

    def _extract_title(self, metadata):

        try:

            metadata = self._decode_metadata(metadata)

            patterns = [
                r"StreamTitle\s*=\s*'(.*?)';",
                r'StreamTitle\s*=\s*"(.*?)";'
            ]

            for pattern in patterns:

                match = re.search(
                    pattern,
                    metadata,
                    re.IGNORECASE | re.DOTALL
                )

                if match:

                    title = match.group(1).strip()

                    if title:
                        return title

        except Exception:
            pass

        return None

    def _listen(self, url, stop_event):

        response = None

        try:

            request = urllib.request.Request(
                url,
                headers={
                    "Icy-MetaData": "1",
                    "User-Agent": "PunkRadioPlayer/1.0",
                    "Accept": "*/*"
                }
            )

            response = urllib.request.urlopen(
                request,
                timeout=5 # Уменьшаем таймаут. Вместо 15 секунд ставим 5.
                # Он не ускоряет само воспроизведение, но позволяет обнаруживать проблемы с подлкючением к ICY.
            )

            # Проверяем, не остановили ли поток пока устанавливалось соединение.
            if stop_event.is_set():
                return

            with self._lock:

                if self._stop_event is not stop_event:
                    return

                self._response = response

            # Получаем интервал ICY.
            metaint = response.headers.get(
                "icy-metaint"
            )

            if not metaint:
                return

            metaint = int(metaint)

            if metaint <= 0:
                return

            # Читаем аудио и метаданные.
            while not stop_event.is_set():

                # Пропускаем аудиоданные.
                audio_data = self._read_exact(
                    response,
                    metaint,
                    stop_event
                )

                if audio_data is None:
                    break

                # Получаем длину блока метаданных.
                length_data = self._read_exact(
                    response,
                    1,
                    stop_event
                )

                if not length_data:
                    break

                metadata_length = (
                    length_data[0] * 16
                )

                # Нулевой размер означает, что в этом блоке нет метаданных.
                if metadata_length == 0:
                    continue

                metadata = self._read_exact(
                    response,
                    metadata_length,
                    stop_event
                )

                if metadata is None:
                    break

                title = self._extract_title(metadata)

                if title:

                    with self._lock:

                        # Старый поток не может перезаписать новые метаданные.
                        if (
                            self._stop_event is stop_event
                            and not stop_event.is_set()
                        ):

                            self.title = title

        except Exception:
            pass

        finally:

            if response is not None:

                try:
                    response.close()
                except Exception:
                    pass

            with self._lock:

                # Не очищаем состояние нового подключения.
                if self._response is response:
                    self._response = None

    def release(self):
        self.stop()