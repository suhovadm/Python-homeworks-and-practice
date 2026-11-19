# Функционал HEADER-a (заголовок). Не путать с логотипом!

import customtkinter as ctk

class Header:

    def __init__(self, parent):

        self.subtitle = ctk.CTkLabel(
            parent,
            text="| 90s / 2000s | U N D E R G R O U N D R A D I O |",
            font=("Arial", 13),
            text_color="#777D89"
        )

        self.subtitle.pack(pady=(0, 8))