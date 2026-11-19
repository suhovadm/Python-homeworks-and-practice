# Заглавный файл. Здесь находится основной функционал программы.
# metadata обрабатывает полученные данные: разделяет исполнителя и название песни.
# player управляет аудиодвижком VLC и объединяет источником метаданных.
# icy_metadata занимается непосредственно получением ICY-данных из радиопотока
# (название песни, исполнитель, название передачи).

import os
import sys

# Определяем правильный путь к файлам ресурсов приложения.
# При запуске из Python используется текущая директория проекта.
# При запуске .exe (PyInstaller --onefile) используется директория распаковки.
def resource_path(relative_path):
    try:
        base_path = sys._MEIPASS # Путь к временной директории, созданной PyInstaller.
    except AttributeError:
        base_path = os.path.abspath(".") # Если приложение запущено не из .exe, используем директорию проекта.

    return os.path.join(base_path, relative_path) # Объединяем базовый путь с относительным к ресурсу.

import customtkinter as ctk

from player import RadioPlayer # Подключаем аудиодвижок.
from stations import STATIONS # Подключаем радиостанции.
from config import load_config, save_config # Подключаем функционал загрузки и сохранения настроек.
from metadata_updater import MetadataUpdater # Подключаем обновление метаданных.
from playback_controls import PlaybackControls # Подключаем кнопки "Назад", "Вперёд" и "Play/Pause".
from volume_control import VolumeControl # Подключаем функционал регулировки громкости.
from station_selector import StationSelector # Подключаем выпадающее меню с выбором радиостанций.
from now_playing import NowPlaying # Подключаем функционал текущего воспроизведения.
from clipboard import ClipboardManager # Импортируем функционал копирования названия трека и исполнителя песни.

from logo import Logo # Подключаем логотип.
from header import Header # Подключаем header
from footer import Footer # Подключаем footer

ctk.set_appearance_mode("dark") # Включает тёмный режим для стандартных элементов CustomTkinter.
ctk.set_default_color_theme("dark-blue") # Задаёт оформление кнопок Play/Pause, ползунка громкости и т.д.

class PunkRadioApp(ctk.CTk):

    def __init__(self):
        super().__init__()

        self.title("PUNK RADIO PLAYER") # Заголовочный тайтл. Это то, что рядом с кнопками "свернуть", "закрыть".
        self.geometry("440x422")
        self.resizable(False, False) # Возможность изменения размеров окна. Выключена.
        self.iconbitmap(resource_path("assets/icon.ico")) # Подключаем иконку из папки /assets

        self.configure(fg_color="#111318") # Дополняет общую тему dark-blue тёмно-графитовым цветом.

        self.config_data = load_config() # Загрузка сохранённого ранее конфига при запуске программы.
        self.player = RadioPlayer() # Получаем доступ к аудиодвижку для дальнейшей работы с ним.

        # Определяем, какая радиостанция будет выбрана при запуске программы.
        # Этот код восстанавливает последнюю выбранную радиостанцию из настроек.
        self.current_station = min(
            self.config_data["station"],
            len(STATIONS) - 1
        )

        self.playing = False # Запрашивать метаданные только тогда, когда нажат "Play".

        self.create_interface()

        self.protocol("WM_DELETE_WINDOW", self.close_app)

    def create_interface(self):

        # LOGO.
        self.logo = Logo(self)

        # HEADER.
        self.header = Header(self)

        # NOW PLAYING. Основной функционал находится в файле now_playing.py
        # Файл main.py только создаёт саму панель.
        self.now_playing = NowPlaying(self)
        self.now_playing.pack(padx=20, fill="x")

        self.track_label = self.now_playing.track_label
        self.artist_label = self.now_playing.artist_label
        self.status_label = self.now_playing.status_label

        # CLIPBOARD ( ПОДКЛЮЧАЕМ ФУНКЦИОНАЛ КОПИРОВАНИЯ ТРЕКА И ИСПОЛНИТЕЛЯ ПЕСНИ ).
        self.clipboard_manager = ClipboardManager(
            self,
            (
                self.now_playing,
                self.track_label,
                self.artist_label,
                self.status_label
            )
        )

        # STATION SELECTOR.
        self.station_selector = StationSelector(
            self,
            self
        )

        # PLAYBACK CONTROLS.
        self.playback_controls = PlaybackControls(
            self,
            self
        )

        # VOLUME. Подключение функционала регулировки громкости. Сам функционал живёт в файле volume_control.py
        self.volume_control = VolumeControl(
            self,
            self.player,
            self.config_data["volume"]
        )

        # FOOTER.
        self.footer = Footer(self)

        # METADATA UPDATER. Теперь прописывать обновление в мс. нужно 1 раз и только здесь.
        self.metadata_updater = MetadataUpdater(
            self,
            self.player,
            interval=3000 # Частота обновления метаданных (3000 мс. / 3 сек.)
        )

    # CLOSE APPLICATION.
    def close_app(self):

        save_config(
            self.volume_control.get_volume(),
            self.current_station
        )

        self.player.release()
        self.destroy()

if __name__ == "__main__":
    app = PunkRadioApp()
    app.mainloop()