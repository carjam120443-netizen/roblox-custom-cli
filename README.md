# 🎮 Roblox Custom Launcher

**A custom, safe Roblox bootstrapper built for people who want more control over how they launch Roblox.**

Roblox Custom Launcher (**RCL**) is a lightweight, custom-branded launcher inspired by the general design and functionality of projects like Fishstrap, while being independently implemented.

> **RCL — Your launcher. Your setup. Roblox's client.** 🎮🔥

## ✨ Features

- 🖥️ **Custom GUI launcher**
- 🚀 **Direct Roblox client launching** through the official Windows protocol
- 🔍 **Roblox installation detection**
- 📊 **Launcher diagnostics**
- ⭐ **Favorites**
- 🕘 **Launch history**
- 👤 **Launcher profiles**
- 💻 **CLI support**
- 📦 **Standalone Windows `.exe` builds**
- 🤖 **Automated GitHub Actions builds**
- 📁 **Portable source code**
- 🎨 **Custom RCL branding**

## 🔐 Safety

RCL is designed to work **with the official Roblox client**, rather than modifying it.

It does **not**:

- ❌ Collect Roblox passwords
- ❌ Read `.ROBLOSECURITY` cookies
- ❌ Extract session tokens
- ❌ Inject into Roblox
- ❌ Patch the Roblox client
- ❌ Bypass Roblox security

Authentication remains handled by Roblox itself.

## 🚀 Launching Roblox

The GUI does **not** open `roblox.com` when you click **Launch Roblox**.

On Windows, RCL invokes the official `roblox-player:` protocol registered by the Roblox client, allowing Windows to hand the launch request directly to Roblox.

If Roblox is not installed or its protocol registration is unavailable, the launcher reports the installation status rather than attempting to replace Roblox with an unofficial client.

## 🛠️ Built With

- 🐍 Python
- 🖥️ Tkinter
- 📦 PyInstaller
- ⚙️ GitHub Actions

## 📦 Windows Builds

GitHub Actions can build the launcher automatically and package:

- `RobloxCustomLauncher.exe` — GUI launcher
- `RobloxCustomCLI.exe` — CLI launcher
- Python source files
- Documentation

A separate workflow packages the complete project into a Windows ZIP artifact.

## 🎯 Project Goal

The goal of RCL is to build a **fully custom Roblox launcher experience** with useful tools and a polished interface while keeping the actual Roblox client untouched.

The project can grow with features such as local profiles, launch history, favorites, diagnostics, shortcuts, and additional launcher configuration.

## 🐟 Fishstrap-inspired direction

RCL takes inspiration from the **launcher/bootstrapper concept and UX direction** of Fishstrap, but its implementation and branding are independent. It is not intended to reproduce Fishstrap's source code or impersonate the project.

Features that modify or bypass the Roblox client, defeat security controls, automate account credentials, or interfere with anti-cheat are intentionally out of scope.

## ⚠️ Disclaimer

Roblox Custom Launcher is an independent community project and is **not affiliated with Roblox Corporation or Fishstrap**.

## 📄 License

See the repository license for the terms governing this project.
