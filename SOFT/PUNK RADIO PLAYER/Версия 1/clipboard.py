# Функционал копирования трэка и названия исполнителя песни по нажатию ПКМ по области воспроизведения.
# В Windows копировать можно по нажатию на ПКМ и на колёсико мышки.

import tkinter as tk

class ClipboardManager:

    def __init__(self, root, widgets):
        self.root = root
        self.widgets = widgets

        self.copy_menu = tk.Menu(
            root,
            tearoff=0
        )

        self.copy_menu.add_command(
            label="Копировать исполнителя и трек",
            font=("Tahoma", 14),
            command=self.copy_both
        )

        # Привязка контекстного меню ко всем элементам.
        for widget in self.widgets:
            widget.bind(
                "<Button-3>",
                self.show_copy_menu
            )

            widget.bind(
                "<Button-2>",
                self.show_copy_menu
            )

    def copy_to_clipboard(self, text):

        if not text:
            return

        self.root.clipboard_clear()
        self.root.clipboard_append(text)
        self.root.update()

    def copy_both(self):

        artist = self.widgets[2].cget("text")
        track = self.widgets[1].cget("text")

        if artist and track:
            self.copy_to_clipboard(
                f"{artist} — {track}"
            )

        elif track:
            self.copy_to_clipboard(track)

        elif artist:
            self.copy_to_clipboard(artist)

    def show_copy_menu(self, event):

        try:
            self.copy_menu.tk_popup(
                event.x_root,
                event.y_root
            )
        finally:
            self.copy_menu.grab_release()