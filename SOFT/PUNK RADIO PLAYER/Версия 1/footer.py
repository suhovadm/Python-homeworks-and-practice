# Функционал FOOTER-a (нижнего колонтитула) с копирайтами.

import customtkinter as ctk

class Footer:

    def __init__(self, parent):

        self.footer = ctk.CTkLabel(
            parent,
            text="Created by n1rvana (c) 2026",
            font=("Comic Sans MS", 13),
            text_color="#555C68"
        )

        self.footer.pack(side="bottom", pady=4)