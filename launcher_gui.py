#!/usr/bin/env python3
"""Roblox Custom Launcher GUI with menu and persistent themes."""
from __future__ import annotations

import json
import os
import subprocess
import tkinter as tk
import webbrowser
from pathlib import Path

APP_NAME = "Roblox Custom Launcher"
VERSION = "1.3.0"
CONFIG = Path(os.getenv("APPDATA", Path.home())) / "RobloxCustomLauncher" / "settings.json"
THEMES = {
    "aero": {"bg": "#dceeff", "panel": "#eef8ff", "accent": "#3b8edb", "text": "#102030", "muted": "#42657d", "button": "#d2ebff"},
    "windows 95": {"bg": "#008080", "panel": "#c0c0c0", "accent": "#000080", "text": "#000000", "muted": "#303030", "button": "#d0d0d0"},
    "classic roblox": {"bg": "#f2f2f2", "panel": "#ffffff", "accent": "#e2231a", "text": "#171717", "muted": "#666666", "button": "#eeeeee"},
}
DEFAULT_THEME = "aero"


def load_theme() -> str:
    try:
        name = json.loads(CONFIG.read_text(encoding="utf-8")).get("theme", DEFAULT_THEME)
        return name if name in THEMES else DEFAULT_THEME
    except (OSError, ValueError, TypeError):
        return DEFAULT_THEME


def save_theme(name: str) -> None:
    CONFIG.parent.mkdir(parents=True, exist_ok=True)
    CONFIG.write_text(json.dumps({"theme": name}, indent=2), encoding="utf-8")


def roblox_installed() -> bool:
    candidates = [os.path.expandvars(r"%LOCALAPPDATA%\Roblox\Versions"), os.path.expandvars(r"%PROGRAMFILES%\Roblox"), os.path.expandvars(r"%PROGRAMFILES(X86)%\Roblox")]
    return any(os.path.isdir(path) for path in candidates)


def launch_roblox() -> None:
    try:
        os.startfile("roblox-player:")
    except (AttributeError, OSError):
        subprocess.Popen(["cmd", "/c", "start", "", "roblox-player:"], shell=False)


class LauncherApp:
    def __init__(self) -> None:
        self.root = tk.Tk()
        self.root.geometry("820x540")
        self.root.minsize(720, 480)
        self.root.title(APP_NAME)
        self.theme_name = load_theme()
        self.build()

    @property
    def theme(self):
        return THEMES[self.theme_name]

    def build(self) -> None:
        t = self.theme
        self.root.configure(bg=t["bg"])
        for widget in self.root.winfo_children():
            widget.destroy()

        menubar = tk.Menu(self.root, tearoff=False, bg=t["panel"], fg=t["text"])
        menu = tk.Menu(menubar, tearoff=False, bg=t["panel"], fg=t["text"])
        menu.add_command(label="Launch Roblox", command=launch_roblox)
        menu.add_command(label="Refresh Status", command=self.refresh)
        menu.add_separator()
        menu.add_command(label="Themes", command=self.show_themes)
        menu.add_separator()
        menu.add_command(label="GitHub", command=lambda: webbrowser.open("https://github.com/carjam120443-netizen/roblox-custom-cli"))
        menu.add_command(label="Exit", command=self.root.destroy)
        menubar.add_cascade(label="Menu", menu=menu)
        self.root.config(menu=menubar)

        header = tk.Frame(self.root, bg=t["panel"], height=92)
        header.pack(fill="x")
        header.pack_propagate(False)
        tk.Label(header, text="RCL", font=("Segoe UI", 25, "bold"), fg="#ffffff", bg=t["accent"], width=5).pack(side="left", padx=24, pady=17)
        title = tk.Frame(header, bg=t["panel"])
        title.pack(side="left", pady=14)
        tk.Label(title, text=APP_NAME, font=("Segoe UI", 19, "bold"), fg=t["text"], bg=t["panel"]).pack(anchor="w")
        tk.Label(title, text=f"Custom Roblox bootstrapper • {self.theme_name.title()} theme", font=("Segoe UI", 10), fg=t["muted"], bg=t["panel"]).pack(anchor="w")

        body = tk.Frame(self.root, bg=t["bg"])
        body.pack(fill="both", expand=True, padx=36, pady=28)
        tk.Label(body, text="Welcome", font=("Segoe UI", 25, "bold"), fg=t["text"], bg=t["bg"]).pack(anchor="w")
        tk.Label(body, text="Launch Roblox directly through the installed client.", font=("Segoe UI", 11), fg=t["muted"], bg=t["bg"]).pack(anchor="w", pady=(5, 20))

        card = tk.Frame(body, bg=t["panel"], padx=22, pady=18)
        card.pack(fill="x")
        tk.Label(card, text="Roblox status", font=("Segoe UI", 14, "bold"), fg=t["text"], bg=t["panel"]).pack(anchor="w", pady=(0, 10))
        self.client_status = tk.Label(card, font=("Segoe UI", 10), bg=t["panel"], anchor="w")
        self.client_status.pack(fill="x")
        for text in ("● Web login is not used for launching", "● Login handled by Roblox", "● Credentials: never accessed"):
            tk.Label(card, text=text, font=("Segoe UI", 10), fg="#16803c", bg=t["panel"], anchor="w").pack(fill="x", pady=2)
        self.refresh()

        row = tk.Frame(body, bg=t["bg"])
        row.pack(fill="x", pady=24)
        self.button(row, "Launch Roblox", launch_roblox, True).pack(side="left")
        self.button(row, "Refresh Status", self.refresh).pack(side="left", padx=10)
        self.button(row, "Themes", self.show_themes).pack(side="left")
        tk.Label(body, text=f"Version {VERSION} • Theme: {self.theme_name.title()} • Official client protocol", font=("Segoe UI", 9), fg=t["muted"], bg=t["bg"]).pack(anchor="w", side="bottom")

    def button(self, parent, text, command, primary=False):
        t = self.theme
        return tk.Button(parent, text=text, command=command, font=("Segoe UI", 11, "bold"), bg=t["accent"] if primary else t["button"], fg="#ffffff" if primary else t["text"], activebackground=t["accent"], activeforeground="#ffffff", relief="flat", bd=0, padx=22, pady=11, cursor="hand2")

    def refresh(self):
        t = self.theme
        installed = roblox_installed()
        self.client_status.config(text=("● Roblox client detected" if installed else "● Roblox client not detected"), fg="#16803c" if installed else "#a06000", bg=t["panel"])

    def show_themes(self):
        t = self.theme
        win = tk.Toplevel(self.root)
        win.title("RCL Themes")
        win.geometry("430x330")
        win.configure(bg=t["bg"])
        tk.Label(win, text="Choose a theme", font=("Segoe UI", 18, "bold"), fg=t["text"], bg=t["bg"]).pack(pady=(22, 6))
        tk.Label(win, text="Changes apply immediately and are saved.", font=("Segoe UI", 10), fg=t["muted"], bg=t["bg"]).pack(pady=(0, 16))
        for name in THEMES:
            tk.Button(win, text=name.title(), command=lambda n=name, w=win: self.set_theme(n, w), font=("Segoe UI", 11, "bold"), bg=THEMES[name]["button"], fg=THEMES[name]["text"], relief="flat", padx=20, pady=9).pack(fill="x", padx=55, pady=5)

    def set_theme(self, name: str, window: tk.Toplevel):
        self.theme_name = name
        save_theme(name)
        window.destroy()
        self.build()

    def run(self):
        self.root.mainloop()


if __name__ == "__main__":
    LauncherApp().run()
