# Функционал логотипа, не путать с header-ом!

import customtkinter as ctk

class Logo:

    def __init__(self, parent):

        self.logo = ctk.CTkLabel(
            parent,
            text="PUNK RADIO PLAYER",
            font=("Arial", 24, "bold"),
            text_color="#FFFFFF"
        )

        self.logo.pack(pady=(8, 2))
