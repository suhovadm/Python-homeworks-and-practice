# Функционал регулировки громкости.

import customtkinter as ctk

class VolumeControl:

    def __init__(self, parent, player, initial_volume=50):

        self.parent = parent
        self.player = player

        self.volume = initial_volume

        self.create_interface()
        self.update_volume(self.volume)

    # CREATE VOLUME INTERFACE.
    def create_interface(self):

        self.volume_frame = ctk.CTkFrame(
            self.parent,
            fg_color="transparent",
            width=480
        )
        self.volume_frame.pack(pady=(2, 0))

        self.volume_label = ctk.CTkLabel(
            self.volume_frame,
            text=f"VOLUME: {self.volume}%",
            text_color="#FFFFFF",
            font=("Arial", 15, "bold")
        )
        self.volume_label.pack(pady=(0, 3))

        self.volume_slider = ctk.CTkSlider(
            self.volume_frame,
            from_=0,
            to=100,
            width=400,
            height=18, # Толщина прокрутки volume.
            command=self.update_volume,
            progress_color="#20A36B",
            button_color="#20A36B",
            button_hover_color="#168353",
            fg_color="#343B49",
            border_width=0
        )
        self.volume_slider.pack(pady=2)

        self.volume_slider.set(self.volume)

    # VOLUME CONTROL.
    def update_volume(self, value):

        self.volume = max(
            0,
            min(100, int(float(value)))
        )

        self.player.set_volume(self.volume)

        self.volume_label.configure(
            text=f"VOLUME: {self.volume}%"
        )

    # GET CURRENT VOLUME.
    def get_volume(self):

        return self.volume