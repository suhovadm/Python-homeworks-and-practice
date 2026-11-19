# Это аудиодвижок. Он отвечает за запуск, остановку, паузу и громкость.
# Для его работы необходимо установить VLC-плеер, без него работать не будет...

import vlc
from icy_metadata import ICYMetadata

class RadioPlayer:

    def __init__(self):

        self.instance = vlc.Instance(
            "--no-video",
            "--quiet",
            "--network-caching=300", # Уменьшаем сетевой буфер. 300 - быстрее, но возможны прерывания.
            "--live-caching=300" # Уменьшаем буферизацию живого потока.
        )

        self.player = self.instance.media_player_new()

        self.current_url = None

        self.icy = ICYMetadata()

    def play(self, url):

        # self.stop() # Старый метод выключен.
        self.icy.stop() # Убираем лишнюю задержку при переключении радиостанций.

        self.current_url = url

        media = self.instance.media_new(url)

        media.add_option(":http-reconnect")

        self.player.set_media(media)

        self.player.play()

        self.icy.start(url) # Запускаем отдельное получение ICY-метаданных.

    def pause(self):

        self.player.pause()

    def stop(self):

        self.icy.stop()

        self.player.stop()

    def set_volume(self, volume):

        volume = max(
            0,
            min(100, int(volume))
        )

        self.player.audio_set_volume(volume)

    def is_playing(self):

        return self.player.is_playing() == 1

    def _read_meta(self, media, meta_name):

        try:

            meta_type = getattr(
                vlc.Meta,
                meta_name,
                None
            )

            if meta_type is None:
                return None

            value = media.get_meta(meta_type)

            if value:
                return str(value).strip()

        except Exception:
            pass

        return None

    def get_metadata(self):

        # Сначала проверяем ICY.

        icy_title = self.icy.get_title()

        if icy_title:
            return icy_title, None

        # Если ICY ничего не получил, используем метаданные VLC.

        media = self.player.get_media()

        if media is None:
            return None, None

        now_playing = self._read_meta(
            media,
            "NowPlaying"
        )

        title = self._read_meta(
            media,
            "Title"
        )

        artist = self._read_meta(
            media,
            "Artist"
        )

        if title and artist:
            return title, artist

        if now_playing:
            return now_playing, artist

        if title:
            return title, artist

        if artist:
            return None, artist

        return None, None

    def release(self):

        self.stop()
        self.icy.release()

        self.player.release()
        self.instance.release()