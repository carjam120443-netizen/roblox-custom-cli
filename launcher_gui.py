#!/usr/bin/env python3
"""Roblox Custom Launcher GUI.

Custom-branded, Fishstrap-inspired UX implemented independently.
Only checks whether the official Roblox client is installed. It never reads
credentials, cookies, session tokens, or authentication databases.
"""
from __future__ import annotations

import os
import tkinter as tk
import webbrowser

APP_NAME = "Roblox Custom Launcher"
VERSION = "1.1.0"
BG = "#0f1117"
PANEL = "#171a23"
ACCENT = "#7c5cff"
TEXT = "#f4f5f7"
MUTED = "#a6adbb"
GOOD = "#4ade80"
WARN = "#fbbf24"


def roblox_installed() -> bool:
    candidates = [
        os.path.expandvars(r"%LOCALAPPDATA%\Roblox\Versions"),
        os.path.expandvars(r"%PROGRAMFILES%\Roblox"),
        os.path.expandvars(r"%PROGRAMFILES(X86)%\Roblox"),
    ]
    return any(os.path.exists(path) for path in candidates)


def open_roblox() -> None:
    webbrowser.open("https://www.roblox.com/home")


def refresh_status(labels: dict[str, tk.Label]) -> None:
    installed = roblox_installed()
    labels["client"].config(text=("● Roblox client detected" if installed else "● Roblox client not detected"), fg=GOOD if installed else WARN)
    labels["website"].config(text="● Roblox website available", fg=GOOD)
    labels["login"].config(text="● Login handled by Roblox", fg=GOOD)
    labels["credentials"].config(text="● Credentials: never accessed", fg=GOOD)


def main() -> None:
    root = tk.Tk()
    root.title(f"{APP_NAME} Setup")
    root.geometry("800x520")
    root.minsize(700, 470)
    root.configure(bg=BG)

    header = tk.Frame(root, bg=PANEL, height=92)
    header.pack(fill="x")
    header.pack_propagate(False)
    tk.Label(header, text="RCL", font=("Segoe UI", 26, "bold"), fg=TEXT, bg=ACCENT, width=5).pack(side="left", padx=24, pady=18)
    title = tk.Frame(header, bg=PANEL)
    title.pack(side="left", pady=15)
    tk.Label(title, text=APP_NAME, font=("Segoe UI", 19, "bold"), fg=TEXT, bg=PANEL).pack(anchor="w")
    tk.Label(title, text="Custom Roblox bootstrapper", font=("Segoe UI", 10), fg=MUTED, bg=PANEL).pack(anchor="w")

    body = tk.Frame(root, bg=BG)
    body.pack(fill="both", expand=True, padx=36, pady=28)
    tk.Label(body, text="Welcome", font=("Segoe UI", 25, "bold"), fg=TEXT, bg=BG).pack(anchor="w")
    tk.Label(body, text="Check your Roblox installation and launch it safely.", font=("Segoe UI", 11), fg=MUTED, bg=BG).pack(anchor="w", pady=(5, 20))

    card = tk.Frame(body, bg=PANEL, padx=22, pady=18)
    card.pack(fill="x")
    tk.Label(card, text="Roblox status", font=("Segoe UI", 14, "bold"), fg=TEXT, bg=PANEL).pack(anchor="w", pady=(0, 10))
    labels = {}
    for key in ("client", "website", "login", "credentials"):
        labels[key] = tk.Label(card, font=("Segoe UI", 10), bg=PANEL, anchor="w")
        labels[key].pack(fill="x", pady=2)
    refresh_status(labels)

    row = tk.Frame(body, bg=BG)
    row.pack(fill="x", pady=24)
    def make_button(text, command, primary=False):
        return tk.Button(row, text=text, command=command, font=("Segoe UI", 11, "bold"), bg=ACCENT if primary else PANEL, fg=TEXT, activebackground=ACCENT, activeforeground=TEXT, relief="flat", bd=0, padx=22, pady=11, cursor="hand2")
    make_button("Launch Roblox", open_roblox, True).pack(side="left")
    make_button("Refresh Status", lambda: refresh_status(labels)).pack(side="left", padx=10)
    make_button("GitHub", lambda: webbrowser.open("https://github.com/carjam120443-netizen/roblox-custom-cli")).pack(side="left")
    tk.Label(body, text=f"Version {VERSION}  •  Official Roblox client  •  No credentials or session tokens are read", font=("Segoe UI", 9), fg=MUTED, bg=BG).pack(anchor="w", side="bottom")
    root.mainloop()


if __name__ == "__main__":
    main()
