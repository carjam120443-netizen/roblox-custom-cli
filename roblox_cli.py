#!/usr/bin/env python3
"""Roblox Custom CLI - a small, safe launcher for the official Roblox client.

This project does not patch, inject into, modify, or bypass Roblox.
It simply builds official Roblox URLs and opens them with the user's browser.
"""

from __future__ import annotations

import argparse
import json
import os
import re
import sys
import webbrowser
from pathlib import Path
from urllib.parse import urlparse

APP_NAME = "Roblox Custom CLI"
CONFIG_DIR = Path(os.environ.get("APPDATA", Path.home())) / "RobloxCustomCLI"
CONFIG_FILE = CONFIG_DIR / "config.json"
ROBLOX_HOME = "https://www.roblox.com/home"
ROBLOX_GAMES = "https://www.roblox.com/games/"


def load_config() -> dict:
    if not CONFIG_FILE.exists():
        return {"favorite_places": []}
    try:
        data = json.loads(CONFIG_FILE.read_text(encoding="utf-8"))
        return data if isinstance(data, dict) else {"favorite_places": []}
    except (OSError, json.JSONDecodeError):
        return {"favorite_places": []}


def save_config(data: dict) -> None:
    CONFIG_DIR.mkdir(parents=True, exist_ok=True)
    CONFIG_FILE.write_text(json.dumps(data, indent=2), encoding="utf-8")


def place_id_from_text(value: str) -> str | None:
    value = value.strip()
    if value.isdigit():
        return value
    parsed = urlparse(value)
    if parsed.netloc.lower().endswith("roblox.com"):
        match = re.search(r"/games/(\d+)", parsed.path)
        if match:
            return match.group(1)
    return None


def open_url(url: str) -> int:
    if not webbrowser.open(url):
        print(f"Could not open the browser automatically.\nOpen this URL manually:\n{url}")
        return 1
    print(f"Opened: {url}")
    return 0


def launch(place: str) -> int:
    place_id = place_id_from_text(place)
    if not place_id:
        print("Error: enter a Roblox place ID or an official roblox.com/games URL.")
        return 2
    # Opening the official game page lets Roblox's own website/client handle login,
    # updates, authentication, and launching. No private tokens are handled here.
    return open_url(f"{ROBLOX_GAMES}{place_id}/")


def interactive() -> int:
    print(f"\n{APP_NAME}")
    print("Safe launcher for the official Roblox website/client.\n")
    while True:
        print("[1] Roblox Home")
        print("[2] Launch a game")
        print("[3] Favorites")
        print("[4] Add favorite")
        print("[5] Quit")
        choice = input("\nSelect: ").strip()
        if choice == "1":
            open_url(ROBLOX_HOME)
        elif choice == "2":
            launch(input("Place ID or Roblox game URL: "))
        elif choice == "3":
            favorites = load_config().get("favorite_places", [])
            if not favorites:
                print("No favorites yet.")
            else:
                for index, item in enumerate(favorites, 1):
                    print(f"[{index}] {item}")
                selected = input("Launch number (blank to cancel): ").strip()
                if selected.isdigit() and 1 <= int(selected) <= len(favorites):
                    launch(str(favorites[int(selected) - 1]))
        elif choice == "4":
            place_id = place_id_from_text(input("Place ID or Roblox game URL: "))
            if place_id:
                config = load_config()
                favorites = config.setdefault("favorite_places", [])
                if place_id not in favorites:
                    favorites.append(place_id)
                    save_config(config)
                    print(f"Added {place_id} to favorites.")
                else:
                    print("Already a favorite.")
            else:
                print("Invalid Roblox place ID/URL.")
        elif choice == "5":
            return 0
        else:
            print("Unknown option.")


def main() -> int:
    parser = argparse.ArgumentParser(description=APP_NAME)
    sub = parser.add_subparsers(dest="command")
    sub.add_parser("home", help="Open official Roblox Home")
    game = sub.add_parser("launch", help="Open an official Roblox game page")
    game.add_argument("place", help="Place ID or roblox.com/games URL")
    favorite = sub.add_parser("favorite", help="Manage favorites")
    favorite.add_argument("place", help="Place ID or roblox.com/games URL")
    args = parser.parse_args()

    if args.command == "home":
        return open_url(ROBLOX_HOME)
    if args.command == "launch":
        return launch(args.place)
    if args.command == "favorite":
        place_id = place_id_from_text(args.place)
        if not place_id:
            print("Invalid Roblox place ID/URL.")
            return 2
        config = load_config()
        favorites = config.setdefault("favorite_places", [])
        if place_id not in favorites:
            favorites.append(place_id)
            save_config(config)
            print(f"Added {place_id} to favorites.")
        else:
            print("Already a favorite.")
        return 0
    return interactive()


if __name__ == "__main__":
    raise SystemExit(main())
