# Подкапотный конфиг. Он будет сохранять громкость и последнюю выбранную радиостанцию.

import json
import os

CONFIG_FILE = "config.json"

DEFAULT_CONFIG = {
    "volume": 50,
    "station": 0
}

def load_config():
    if not os.path.exists(CONFIG_FILE):
        return DEFAULT_CONFIG.copy()

    try:
        with open(CONFIG_FILE, "r", encoding="utf-8") as file:
            data = json.load(file)

        return {
            "volume": max(0, min(100, int(data.get("volume", 50)))),
            "station": max(0, int(data.get("station", 0)))
        }

    except (ValueError, TypeError, OSError, json.JSONDecodeError):
        return DEFAULT_CONFIG.copy()

def save_config(volume, station):
    data = {
        "volume": volume,
        "station": station
    }

    with open(CONFIG_FILE, "w", encoding="utf-8") as file:
        json.dump(data, file, indent=4)