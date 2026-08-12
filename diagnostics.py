"""Safe launcher diagnostics."""
from __future__ import annotations
import os
import platform
import shutil
import sys
from pathlib import Path

def collect() -> dict:
    return {
        "python": sys.version.split()[0],
        "platform": platform.platform(),
        "architecture": platform.machine(),
        "roblox_in_path": shutil.which("RobloxPlayerBeta.exe") is not None,
        "home": str(Path.home()),
        "working_directory": os.getcwd(),
    }

def print_report() -> None:
    print("Roblox Custom CLI diagnostics")
    print("=" * 30)
    for key, value in collect().items():
        print(f"{key}: {value}")
