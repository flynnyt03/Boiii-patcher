import os
import zipfile
import urllib.request
import tempfile
import getpass
import datetime
import tkinter as tk

def log(message, log_path):
    timestamp = datetime.datetime.now().strftime("[%Y-%m-%d %H:%M:%S]")
    full_message = f"{timestamp} {message}"
    print(full_message)
    with open(log_path, "a") as log_file:
        log_file.write(full_message + "\n")

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
    url = 'https://www.dropbox.com/scl/fi/6brskgm6j014jkzjw5jjl/boiii.zip?rlkey=3gn18pdgbhmh1qyyyykfrc5pg&st=7baajqd9&dl=1'  

    user_name = getpass.getuser()
    target_dir = os.path.join("C:\\Users", user_name, "AppData", "Local")
    os.makedirs(target_dir, exist_ok=True)

    log_path = os.path.join(target_dir, "installer.log")
    log("Starting installation...", log_path)

    try:
        tmp_zip_path = os.path.join(tempfile.gettempdir(), "boiii.zip")
        log(f"Downloading file from {url}...", log_path)
        urllib.request.urlretrieve(url, tmp_zip_path)
        log("Download complete.", log_path)

        log(f"Extracting to {target_dir}...", log_path)
        with zipfile.ZipFile(tmp_zip_path, 'r') as zip_ref:
            zip_ref.extractall(target_dir)
        log("Extraction complete.", log_path)

    except Exception as e:
        log(f"Error: {str(e)}", log_path)

    log("Installation complete. Waiting for user to close the window...", log_path)
    wait_for_exit()

if __name__ == "__main__":
    main()
