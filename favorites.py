"""Favorite Roblox places, stored locally."""
from config import load_config, save_config

def list_favorites() -> list[dict]:
    return load_config().get("favorite_places", [])

def add_favorite(name: str, place_id: str) -> None:
    config = load_config()
    favorites = [x for x in config.get("favorite_places", []) if x.get("place_id") != place_id]
    favorites.append({"name": name, "place_id": str(place_id)})
    config["favorite_places"] = favorites
    save_config(config)

def remove_favorite(place_id: str) -> bool:
    config = load_config()
    old = config.get("favorite_places", [])
    new = [x for x in old if x.get("place_id") != str(place_id)]
    config["favorite_places"] = new
    save_config(config)
    return len(new) != len(old)
