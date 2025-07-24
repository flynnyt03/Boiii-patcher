**DOES NOT INCLUDE T7 GAME FILES**

# Boiii-Patcher
23/07/25
While installing EZZ BOIII, my friends and I ran into an issue that hasn’t been patched by the developers — the common “You need to have an online connection” error. Since we all experienced it, I created a patcher that fixes the problem. Just run the `.exe`, and it’ll take care of everything.

---
24/07/25
- 🗂️ **BO3 Folder Selection**: User-friendly prompt to choose your Black Ops 3 installation folder.
- 📥 **Automatic boiii.exe Download**: Installer pulls the latest `boiii.exe` from GitHub and places it directly into the game folder.
- 📦 **Patch Extraction**: Automatically downloads and extracts required files into your `AppData\Local` folder.
- 🧑 **Username Setup**: Prompt lets you choose your in-game player name and saves it to a new `boiii_players\properties.json` file.
- 📄 **Logging**: Creates an `installer.log` file with detailed logs for easier troubleshooting.
- 🎯 **Portable .exe**: Runs from anywhere — no need to install or modify system paths.
- 🖼️ **Custom Icon Support**: Now includes a custom icon for the `.exe` installer.

---
v3 – 24/07/2025

✨ New Feature: Added automatic download of change_name.bat from GitHub into the BO3 game folder.

🧑‍💻 change_name.bat: Simple batch script that allows users to update their in-game username by modifying boiii_players/properties.json.

🛠️ Improved Logging: All major events, including the .bat download, are now logged to installer.log for easier troubleshooting.

🧼 Cleanup: Better error handling during file downloads and extraction processes.

📌 Reminder: This installer does not include any T7 game files.
---

Just run the installer, follow the prompts, and you’re ready to play — no manual setup needed.
