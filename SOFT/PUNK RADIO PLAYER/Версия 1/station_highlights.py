# Функционал подсветки радиостанции в выпадающем списке.

class StationHighlight:

    def __init__(self, station_menu, stations, get_current_station):

        self.station_menu = station_menu
        self.stations = stations
        self.get_current_station = get_current_station

        self.original_open = self.station_menu._open_dropdown_menu

        self.station_menu._open_dropdown_menu = self.open_dropdown_menu

    # ОТКРЫТИЕ ВЫПАДАЮЩЕГО СПИСКА.
    def open_dropdown_menu(self):

        # Подсветка выполняется только при открытии меню.
        if not self.station_menu._dropdown_menu.winfo_viewable():

            self.highlight_current_station()

        self.original_open()

    # ПОДСВЕТКА ТЕКУЩЕЙ РАДИОСТАНЦИИ.
    def highlight_current_station(self):

        menu = self.station_menu._dropdown_menu

        current_station = self.get_current_station()

        for index in range(len(self.stations)):

            menu.entryconfigure(
                index,
                background=(
                    "#454E60" # Подсветка текущей радиостанции - светло-серый.
                    if index == current_station
                    else "#252A34" # Подсветка всех остальных радиостанций - тёмно-серый.
                )
            )