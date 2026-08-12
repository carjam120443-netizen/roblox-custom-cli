# Roblox Custom CLI 🎮

A lightweight, safe Roblox launcher inspired by the **idea** of Fishstrap: provide a convenient alternative launcher interface and useful local features without modifying the Roblox client.

## What it does

- 🚀 Opens Roblox Home from the CLI
- 🎮 Launches games through their official `roblox.com/games/<placeId>` page
- ⭐ Stores a small local favorites list
- 🧩 Accepts either a place ID or an official Roblox game URL
- 🔐 Never asks for or stores Roblox passwords, cookies, session tokens, or access tokens
- 🛡️ Does not inject code, patch Roblox binaries, bypass authentication, or evade Roblox security
- 📦 Uses Python's standard library only

## Usage

```text
python roblox_cli.py
```

Or use commands directly:

```text
python roblox_cli.py home
python roblox_cli.py launch 1818
python roblox_cli.py launch https://www.roblox.com/games/1818/
python roblox_cli.py favorite 1818
```

The launcher opens the official Roblox game page in the default browser. Roblox's own website/client handles authentication, updates, and the actual game launch.

## Fishstrap-inspired direction

The project takes inspiration from the **launcher/bootstrapping concept** of Fishstrap, not by copying its source code. Future versions can add safe launcher conveniences such as:

- per-user local profiles
- launch history
- favorite games
- configurable Roblox website URLs
- diagnostics that only inspect local launcher state
- optional Windows shortcuts
- a GUI around the same safe launcher core

Features that modify or bypass the Roblox client, defeat security controls, automate account credentials, or interfere with anti-cheat are intentionally out of scope.

## License

This project is independent and is not affiliated with Roblox Corporation or Fishstrap.
