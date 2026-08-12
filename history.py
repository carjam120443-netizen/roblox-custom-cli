"""Local launch history; no credentials or Roblox session data are stored."""
from config import load_config, save_config
from datetime import datetime, timezone

def record_launch(place_id: str, source: str = "cli") -> None:
    config = load_config()
    history = config.get("launch_history", [])
    history.append({
        "place_id": str(place_id),
        "source": source,
        "timestamp": datetime.now(timezone.utc).isoformat(),
    })
    config["launch_history"] = history[-50:]
    save_config(config)

def get_history() -> list[dict]:
    return load_config().get("launch_history", [])

def clear_history() -> None:
    config = load_config()
    config["launch_history"] = []
    save_config(config)
