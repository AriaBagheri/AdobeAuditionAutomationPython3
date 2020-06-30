import json
import os
import subprocess
import time

import pyautogui

pyautogui.PAUSE = 2.5
pyautogui.FAILSAFE = True

CONFIG_FILE = "config.json"
FILE = "audio.wav"
FOLDER = f"{os.getcwd()}\\audios"
HOT_KEY = ["shift", "ctrl", "alt", "1"]

class ConfigFile:
    adobe_audition_location = ""
    configs_folder = "Config"
    files_folder = "audios"

    def __init__(self, config_file: str, configs_folder: str = None):
        config = json.load(open(config_file, "r"))
        self.adobe_audition_location = config["adobe_audition_location"]
        if configs_folder is not None:
            self.configs_folder = configs_folder

    def get_file_str(self, file: str):
        return f"{self.configs_folder}\\{file}"


def main():
    config = ConfigFile(CONFIG_FILE)

    location = pyautogui.locateCenterOnScreen(config.get_file_str("adobe_audition_icon.png"))

    while location is None:
        subprocess.Popen(config.adobe_audition_location)
        time.sleep(3)
        location = pyautogui.locateCenterOnScreen(config.get_file_str("adobe_audition_icon.png"))
    x, y = location
    pyautogui.click(x, y)

    pyautogui.hotkey("ctrlleft", "o")
    pyautogui.hotkey("alt", "d")
    pyautogui.hotkey("ctrl", "a")
    pyautogui.typewrite(f"{FOLDER}")
    pyautogui.press("enter")
    pyautogui.hotkey("alt", "d")
    pyautogui.press(["tab"]*4 + ["home"])
    pyautogui.press("enter")
    pyautogui.hotkey(*HOT_KEY)

    location = None
    while location is None:
        location = pyautogui.locateCenterOnScreen(config.get_file_str("save_text.png"))
        pyautogui.hotkey("ctrl", "shift", "s")
        time.sleep(2)
    pyautogui.press("enter")
    time.sleep(2)
    location = pyautogui.locateCenterOnScreen(config.get_file_str("yes_button.png"))
    x, y = location
    pyautogui.click(x, y)
    pyautogui.press("enter")
    pyautogui.hotkey("ctrl", "w")


if __name__ == '__main__':
    main()
