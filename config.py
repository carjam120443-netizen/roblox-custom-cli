"""Configuration and persistent settings for Roblox Custom CLI."""
from __future__ import annotations
import json
from pathlib import Path

APP_DIR = Path.home() / ".roblox-custom-cli"
CONFIG_FILE = APP_DIR / "config.json"
DEFAULTS = {
    "roblox_executable": "",
    "favorite_places": [],
    "launch_history": [],
    "verbose": False,
}

def load_config() -> dict:
    APP_DIR.mkdir(parents=True, exist_ok=True)
    if not CONFIG_FILE.exists():
        save_config(DEFAULTS.copy())
    try:
        data = json.loads(CONFIG_FILE.read_text(encoding="utf-8"))
    except (OSError, json.JSONDecodeError):
        data = {}
    merged = DEFAULTS.copy()
    merged.update(data)
    return merged

def save_config(data: dict) -> None:
    APP_DIR.mkdir(parents=True, exist_ok=True)
    CONFIG_FILE.write_text(json.dumps(data, indent=2), encoding="utf-8")
