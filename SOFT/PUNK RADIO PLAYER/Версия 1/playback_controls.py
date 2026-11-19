# Функционал кнопок проигрывателя - "вперёд", "назад" и "play/pause".

import customtkinter as ctk
from stations import STATIONS

class PlaybackControls:

    def __init__(self, parent, app):

        self.app = app

        self.controls = ctk.CTkFrame(
            parent,
            fg_color="transparent"
        )
        self.controls.pack(pady=(20, 8))

# ------ ЭТО ПРОСТО КОНТЕЙНЕРЫ. -----------------------------------

        # Кнопка "НАЗАД".
        self.previous_button = ctk.CTkButton(
            self.controls,
            text="◀\u200A", # Кнопка "Назад" сдвинута на 2px влево.
            width=65,
            height=50,
            corner_radius=10,
            border_width=2,
            border_color="#414B5C",
            fg_color="#303846",
            hover_color="#46546A",
            text_color="#FFFFFF",
            font=("Segoe UI Symbol", 23.5, "bold"),
            command=self.app.station_selector.previous_station
        )
        self.previous_button.pack(side="left", padx=6)

        # Кнопка PLAY / PAUSE.
        self.play_button = ctk.CTkButton(
            self.controls,
            text="PLAY",
            width=248, # ширина контейнера PLAY.
            height=48,
            font=("Arial", 21, "bold"),
            fg_color="#20A36B",
            hover_color="#168353",
            command=self.toggle_play
        )
        self.play_button.pack(side="left", padx=6)

        # Кнопка "ВПЕРЁД".
        self.next_button = ctk.CTkButton(
            self.controls,
            text="\u200A▶", # Кнопка "Вперёд" сдвинута на 2px вправо.
            width=65,
            height=50,
            corner_radius=10,
            border_width=2,
            border_color="#414B5C",
            fg_color="#303846",
            hover_color="#46546A",
            text_color="#FFFFFF",
            font=("Segoe UI Symbol", 23.5, "bold"),
            command=self.app.station_selector.next_station
        )
        self.next_button.pack(side="left", padx=6)

# --- ЭТО РЕАЛЬНЫЙ ФУНКЦИОНАЛ КНОПКИ PLAY / PAUSE. ------------------------

    # PLAY / PAUSE.
    def toggle_play(self):

        if self.app.playing:
            self.app.player.pause()
            self.app.playing = False

            # Возвращаем надпись PLAY после остановки воспроизведения.
            self.play_button.configure(text="PLAY")
            self.app.status_label.configure(
                text="PAUSED",
                text_color="#E0A43B"
            )

        else:
            station = STATIONS[self.app.current_station]

            self.app.player.play(station["url"])
            self.app.playing = True

            # Меняем надпись на PAUSE во время воспроизведения.
            self.play_button.configure(text="PAUSE")
            self.app.status_label.configure(
                text="C O N N E C T i N G ...",
                text_color='#A0A6B2',
                font=("Arial", 16, "bold")
            )

            self.app.track_label.configure(
                text="Ожидание информации..."
            )

            self.app.artist_label.configure(
                text=station["genre"]
            )