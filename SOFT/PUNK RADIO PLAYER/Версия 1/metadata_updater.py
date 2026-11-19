# Функционал обновления метаданных. Периодическое обновление информации о текущем
# воспроизводимом треке: исполнитель, название песни и статус воспроизведения.

from metadata import parse_metadata

class MetadataUpdater:

    def __init__(self, app, player, interval):

        self.app = app
        self.player = player
        self.interval = interval

        # Первый запуск обновления метаданных.
        self.app.after(
            self.interval,
            self.refresh_metadata
        )

    # METADATA.
    def refresh_metadata(self):

        if self.app.playing:

            title, artist = self.player.get_metadata()

            if title or artist:

                artist_name, track_name = parse_metadata(
                    title, artist
                )

                self.app.artist_label.configure(
                    text=artist_name
                )

                self.app.track_label.configure(
                    text=track_name
                )

            if self.player.is_playing():

                self.app.status_label.configure(
                    text="● LiVE",
                    text_color="#20B879",
                    font=("Arial", 16, "bold")
                )

        # Повторный запуск обновления метаданных.
        self.app.after(
            self.interval,
            self.refresh_metadata
        )