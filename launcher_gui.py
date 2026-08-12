#!/usr/bin/env python3
"""Roblox Custom Launcher GUI.

Fishstrap-inspired installer/launcher UX, independently implemented and custom branded.
Uses the official Roblox website/client only; no credential handling, injection, or bypasses.
"""
from __future__ import annotations

import tkinter as tk
from tkinter import messagebox
import webbrowser

APP_NAME = "Roblox Custom Launcher"
VERSION = "1.0.0"
BG = "#0f1117"
PANEL = "#171a23"
ACCENT = "#7c5cff"
TEXT = "#f4f5f7"
MUTED = "#a6adbb"


def launch(url: str) -> None:
    webbrowser.open(url)


def install_message() -> None:
    messagebox.showinfo(
        APP_NAME,
        "Setup is ready. Roblox Custom Launcher uses the official Roblox client and website.\n\nNo Roblox credentials or session tokens are collected.",
    )


def main() -> None:
    root = tk.Tk()
    root.title(f"{APP_NAME} Setup")
    root.geometry("760x480")
    root.minsize(680, 440)
    root.configure(bg=BG)

    header = tk.Frame(root, bg=PANEL, height=92)
    header.pack(fill="x")
    header.pack_propagate(False)

    brand = tk.Label(header, text="RCL", font=("Segoe UI", 26, "bold"), fg=TEXT, bg=ACCENT, width=5)
    brand.pack(side="left", padx=24, pady=18)

    title_box = tk.Frame(header, bg=PANEL)
    title_box.pack(side="left", pady=15)
    tk.Label(title_box, text=APP_NAME, font=("Segoe UI", 19, "bold"), fg=TEXT, bg=PANEL).pack(anchor="w")
    tk.Label(title_box, text="A custom, safe Roblox bootstrapper", font=("Segoe UI", 10), fg=MUTED, bg=PANEL).pack(anchor="w")

    body = tk.Frame(root, bg=BG)
    body.pack(fill="both", expand=True, padx=34, pady=28)

    tk.Label(body, text="Welcome", font=("Segoe UI", 25, "bold"), fg=TEXT, bg=BG).pack(anchor="w")
    tk.Label(body, text="Install and launch your custom Roblox experience.", font=("Segoe UI", 11), fg=MUTED, bg=BG).pack(anchor="w", pady=(5, 25))

    card = tk.Frame(body, bg=PANEL, padx=22, pady=20)
    card.pack(fill="x")
    tk.Label(card, text="Roblox Custom Launcher", font=("Segoe UI", 14, "bold"), fg=TEXT, bg=PANEL).pack(anchor="w")
    tk.Label(card, text=f"Version {VERSION}  •  Official Roblox client", font=("Segoe UI", 10), fg=MUTED, bg=PANEL).pack(anchor="w", pady=(5, 0))

    button_row = tk.Frame(body, bg=BG)
    button_row.pack(fill="x", pady=24)

    def button(text: str, command, primary=False):
        return tk.Button(button_row, text=text, command=command, font=("Segoe UI", 11, "bold"),
                         bg=ACCENT if primary else PANEL, fg=TEXT, activebackground=ACCENT,
                         activeforeground=TEXT, relief="flat", bd=0, padx=24, pady=12, cursor="hand2")

    button("Install / Setup", install_message, True).pack(side="left")
    button("Open Roblox", lambda: launch("https://www.roblox.com/home")).pack(side="left", padx=10)
    button("GitHub", lambda: launch("https://github.com/carjam120443-netizen/roblox-custom-cli")).pack(side="left")

    tk.Label(body, text="Safe design: no credential storage, client injection, or Roblox security bypasses.",
             font=("Segoe UI", 9), fg=MUTED, bg=BG).pack(anchor="w", side="bottom")
    root.mainloop()


if __name__ == "__main__":
    main()
