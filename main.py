import os
import zipfile
import urllib.request
import tempfile
import getpass
import datetime
import tkinter as tk
from tkinter import filedialog, simpledialog, messagebox
import json
import pythoncom
import win32com.client

def log(message, log_path):
    timestamp = datetime.datetime.now().strftime("[%Y-%m-%d %H:%M:%S]")
    full_message = f"{timestamp} {message}"
    print(full_message)
    with open(log_path, "a") as log_file:
        log_file.write(full_message + "\n")

def ask_bo3_directory():
    root = tk.Tk()
    root.withdraw()
    messagebox.showinfo("Select Folder", "Please select your Call of Duty Black Ops 3 installation folder.")
    folder_selected = filedialog.askdirectory(title="Select BO3 Folder")
    return folder_selected

def download_file(url, destination, log_path):
    log(f"Downloading {url} to {destination}...", log_path)
    urllib.request.urlretrieve(url, destination)
    log("Download complete.", log_path)

def extract_zip(zip_path, target_dir, log_path):
    log(f"Extracting {zip_path} to {target_dir}...", log_path)
    with zipfile.ZipFile(zip_path, 'r') as zip_ref:
        zip_ref.extractall(target_dir)
    log("Extraction complete.", log_path)

def prompt_for_username():
    root = tk.Tk()
    root.withdraw()
    username = simpledialog.askstring("Player Name", "Enter your in-game player name:")
    return username.strip() if username else None

def create_properties_file(bo3_folder, player_name, log_path):
    players_dir = os.path.join(bo3_folder, "boiii_players")
    os.makedirs(players_dir, exist_ok=True)
    properties_path = os.path.join(players_dir, "properties.json")
    if not os.path.exists(properties_path):
        log(f"Creating {properties_path} with player name: {player_name}", log_path)
        with open(properties_path, "w") as f:
            json.dump({"playerName": player_name}, f)
    else:
        log("properties.json already exists. Not modifying.", log_path)

def create_desktop_shortcut(target_path, shortcut_name, description=""):
    desktop = os.path.join(os.path.join(os.environ['USERPROFILE']), 'Desktop')
    shortcut_path = os.path.join(desktop, f"{shortcut_name}.lnk")
    shell = win32com.client.Dispatch("WScript.Shell")
    shortcut = shell.CreateShortcut(shortcut_path)
    shortcut.TargetPath = target_path
    shortcut.WorkingDirectory = os.path.dirname(target_path)
    shortcut.Description = description
    shortcut.IconLocation = target_path
    shortcut.save()

def ask_create_shortcut(boiii_exe_path):
    root = tk.Tk()
    root.withdraw()
    result = messagebox.askyesno("Create Shortcut", "Do you want to create a desktop shortcut for Ezz BOIII?")
    root.destroy()
    if result:
        create_desktop_shortcut(boiii_exe_path, "Ezz BOIII", "Shortcut to Ezz BOIII executable")
        return True
    return False

def download_batch_file(destination_folder, log_path):
    batch_url = "https://raw.githubusercontent.com/flynnyt03/Boiii-patcher/main/change_name.bat"
    batch_path = os.path.join(destination_folder, "change_name.bat")
    try:
        log(f"Downloading change_name.bat to {batch_path}...", log_path)
        urllib.request.urlretrieve(batch_url, batch_path)
        log("change_name.bat downloaded successfully.", log_path)
    except Exception as e:
        log(f"Error downloading change_name.bat: {e}", log_path)

def wait_for_exit():
    window = tk.Tk()
    window.title("boiii Installer")
    window.geometry("300x120")
    label = tk.Label(window, text="Installation complete.", font=("Arial", 12))
    label.pack(pady=10)
    button = tk.Button(window, text="Close", command=window.destroy)
    button.pack()
    window.mainloop()

def main():
    user_name = getpass.getuser()
    local_appdata_dir = os.path.join("C:\\Users", user_name, "AppData", "Local")
    os.makedirs(local_appdata_dir, exist_ok=True)
    log_path = os.path.join(local_appdata_dir, "installer.log")
    log("Starting installer...", log_path)

    bo3_folder = ask_bo3_directory()
    if not bo3_folder or not os.path.isdir(bo3_folder):
        log("No folder selected. Exiting.", log_path)
        return

    boiii_exe_url = "https://github.com/Ezz-lol/boiii-free/releases/download/v1.0.7/boiii.exe"
    boiii_exe_path = os.path.join(bo3_folder, "boiii.exe")

    try:
        download_file(boiii_exe_url, boiii_exe_path, log_path)
        download_batch_file(bo3_folder, log_path)
    except Exception as e:
        log(f"Error downloading boiii.exe or batch file: {e}", log_path)
        return

    try:
        zip_url = "https://www.dropbox.com/scl/fi/432jt0d43y3zo7pn0txbb/boiii.zip?rlkey=j1zrcst5hykcl43l26axf82f2&st=qiqpsl3h&dl=1"
        tmp_zip_path = os.path.join(tempfile.gettempdir(), "boiii.zip")
        download_file(zip_url, tmp_zip_path, log_path)
        extract_zip(tmp_zip_path, local_appdata_dir, log_path)
    except Exception as e:
        log(f"Error handling zip: {e}", log_path)

    player_name = prompt_for_username()
    if player_name:
        create_properties_file(bo3_folder, player_name, log_path)
    else:
        log("No player name entered. Skipping properties.json creation.", log_path)

    if ask_create_shortcut(boiii_exe_path):
        log("Desktop shortcut created.", log_path)
    else:
        log("User declined desktop shortcut creation.", log_path)

    log("Installation complete. Waiting for user to close the window...", log_path)
    wait_for_exit()

if __name__ == "__main__":
    main()
