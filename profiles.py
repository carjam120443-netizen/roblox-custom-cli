"""Named local launcher profiles, inspired by modern bootstrapper workflows."""
from __future__ import annotations
from config import load_config, save_config

def list_profiles() -> dict:
    return load_config().get("profiles", {})

def save_profile(name: str, settings: dict) -> None:
    config = load_config()
    profiles = config.setdefault("profiles", {})
    profiles[name] = settings
    save_config(config)

def delete_profile(name: str) -> bool:
    config = load_config()
    profiles = config.setdefault("profiles", {})
    if name not in profiles:
        return False
    del profiles[name]
    save_config(config)
    return True
