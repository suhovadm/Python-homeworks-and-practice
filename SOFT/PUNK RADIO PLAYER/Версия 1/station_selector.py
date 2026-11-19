# Функционал выпадающего меню с радиостанциями и выбором оных.

import customtkinter as ctk

from stations import STATIONS
from station_highlights import StationHighlight

class StationSelector:

    def __init__(self, parent, app):

        self.parent = parent
        self.app = app

        self.create_interface()

    def create_interface(self):

        # STATION SELECTOR.
        self.station_label = ctk.CTkLabel(
            self.parent,
            text=f"| RADiOSTATiON ({len(STATIONS)}) |", # Счётчик радиостанций.
            font=("Arial", 13, "bold"),
            text_color="#858B98"
        )
        self.station_label.pack(pady=(8, 3))

        # STATION MENU. Это само меню в свёрнутом состоянии.
        self.station_menu = ctk.CTkOptionMenu(
            self.parent,
            values=[s["name"] for s in STATIONS],
            command=self.change_station,
            width=400,
            height=50, # высота выпадающего меню с радиостанциями. Вместе с ним надо править self.geometry("440x422")
            fg_color="#252A34",
            button_color="#343B49",
            button_hover_color="#454E60",
            dropdown_fg_color="#252A34",
            font=("Arial", 18), # Шрифт, который отображается в меню в свёрнутом состоянии.
            dropdown_font=("Arial", 18)
        )
        self.station_menu.pack()

        self.station_menu.set(
            STATIONS[self.app.current_station]["name"]
        )

        # STATION HIGHLIGHT. Это не сама подсветка, сама подсветка находится в файле station_highlights.py
        self.station_highlight = StationHighlight(
            self.station_menu,
            STATIONS,
            lambda: self.app.current_station
        )

    # CHANGE STATION.
    def change_station(self, selected_name):

        for index, station in enumerate(STATIONS):

            if station["name"] == selected_name:
                self.app.current_station = index
                break

        if self.app.playing:

            self.app.player.play(
                STATIONS[self.app.current_station]["url"]
            )

            self.app.status_label.configure(
                text="CONNECTING...",
                font=("Arial", 16, "bold")
            )

        self.app.artist_label.configure(
            text=STATIONS[self.app.current_station]["genre"]
        )

        self.app.track_label.configure(
            text="Ожидание информации..."
        )

    # NEXT STATION.
    def next_station(self):

        self.app.current_station = (
            self.app.current_station + 1
        ) % len(STATIONS)

        self.station_menu.set(
            STATIONS[self.app.current_station]["name"]
        )

        # Исправляет баг с правой не рабочей кнопкой, когда она только переключала станцию, но не проигрывала её!
        self.change_station(
            STATIONS[self.app.current_station]["name"]
        )

    # PREVIOUS STATION.
    def previous_station(self):

        self.app.current_station = (
            self.app.current_station - 1
        ) % len(STATIONS)

        self.station_menu.set(
            STATIONS[self.app.current_station]["name"]
        )

        self.change_station(
            STATIONS[self.app.current_station]["name"]
        )