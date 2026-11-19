# Здесь обрабатывается информацию о композиции.
# Радиостанции могут передавать исполнителя и песню в одном поле, например
# blink-182 - What's My Age Again?. Поэтому добавим разделение.

import re
import html

# Недопустимые названия аудиопотока. Это нужно для фильтрации ICY-метаданных, чтобы не показывать
# вместо исполнителя и названия песни всякую подкапотную технину.
INVALID_TITLES = {
    "stream",
    "playlist",
    "playlist.mp3",
    "playlist.m3u",
    "playlist.m3u8",
    "playlist.pls",
    "stream.mp3",
    "stream.m3u",
    "stream.m3u8",
    "stream.pls",
    "audio",
    "live",
    "radio",
    "unknown",
    "untitled",
    "unknown title",
    "audio stream",
    "live stream",
    "now playing",
    "no title",
    "no metadata",
    "index",
    "index.m3u8",
    "index.m3u",
    "listen",
    "listen.mp3",
    "listen.m3u"
}

def clean_metadata(value):

    if not value:
        return None

    value = html.unescape(str(value))
    value = value.replace("\x00", "").strip()

    value = re.sub(
        r"^(ICY|StreamTitle)\s*[:=]\s*",
        "",
        value,
        flags=re.IGNORECASE
    )

    value = value.strip(" \t\r\n'\";")

    if not value:
        return None

    return value

def is_valid_title(value):

    if not value:
        return False

    normalized = value.lower().strip()

    if normalized in INVALID_TITLES:
        return False

    if normalized.startswith((
        "http://",
        "https://",
        "www."
    )):
        return False

    if normalized.endswith((
            ".mp3",
            ".m3u",
            ".m3u8",
            ".pls",
            ".aac",
            ".ogg",
            ".wav",
            ".flac"
    )):
        return False

    if re.match(
            r"^(playlist|stream|index|listen)([-_.]?\w*)?$",
            normalized
    ):
        return False

    if len(normalized) < 2:
        return False

    return True

def parse_metadata(title, artist):

    title = clean_metadata(title)
    artist = clean_metadata(artist)

    if artist and not is_valid_title(artist):
        artist = None

    if title and not is_valid_title(title):
        title = None

    if title and artist:
        return artist, title

    if title:

        separators = [
            " - ",
            " – ",
            " — ",
            " | "
        ]

        for separator in separators:

            if separator in title:

                parts = title.split(separator, 1)

                first = parts[0].strip()
                second = parts[1].strip()

                if first and second:
                    return first, second

        match = re.match(
            r"^(.+?)\s+by\s+(.+)$",
            title,
            flags=re.IGNORECASE
        )

        if match:
            return (
                match.group(2).strip(),
                match.group(1).strip()
            )

        return "Неизвестный исполнитель", title

    if artist:
        return artist, "Название композиции недоступно."

    return (
        "Информация недоступна.",
        "Ожидание метаданных..."
    )