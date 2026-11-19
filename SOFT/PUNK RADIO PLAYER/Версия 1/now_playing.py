# Функционал отображения текущего воспроизведения, исполнитель и трэк.

import customtkinter as ctk

class NowPlaying(ctk.CTkFrame):
    def __init__(self, master):
        super().__init__(
            master,
            fg_color="#1B1F27",
            corner_radius=13,
            width=400,
            height=100
        )

        self.pack_propagate(False)

        self.track_label = ctk.CTkLabel(
            self,
            text="Название трэка.",
            font=("Comic Sans MS", 23, "bold"),
            text_color="#FFFFFF",
            wraplength=360
        )
        self.track_label.pack(pady=(4, 2))

        self.artist_label = ctk.CTkLabel(
            self,
            text="Исполнитель.",
            font=("Comic Sans MS", 19),
            text_color="#A0A6B2"
        )
        self.artist_label.pack(pady=1)

        self.status_label = ctk.CTkLabel(
            self,
            text="READY!",
            font=("Arial", 16, "bold"),
            text_color="#20B879"
        )
        self.status_label.pack(pady=3)