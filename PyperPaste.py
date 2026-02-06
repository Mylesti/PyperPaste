import sys
import subprocess

def ensure_package(pkg_name, import_name=None):
    try:
        __import__(import_name or pkg_name)
    except ImportError:
        print(f"[+] Installing missing package: {pkg_name}")
        subprocess.check_call([
            sys.executable, "-m", "pip", "install", pkg_name
        ])

ensure_package("pyperclip")
ensure_package("keyboard")
ensure_package("pyautogui")

import tkinter as tk
import pyperclip
import keyboard
import time
import os
import ctypes
import sys
import pyautogui

class PyperPaste:
    def __init__(self, root):
        self.root = root
        self.root.title("PyperPaste")
        self.root.geometry("500x600")
        self.root.resizable(False, False)
        self.shortcut = "ctrl+b"
        self.interval = 0.10

        #Title 

        self.title = tk.Label(
            text="PyperPaste",
            font=("utopia", 15),
            width=15,
            relief="raised"
        )
        self.shortcut_display = tk.Entry(
            width=25
        )
        # End titletext

        #Buttons
        self.change_shortcut_button = tk.Button(
            text="Change settings",
            width="15",
            command=self.settings
        )
        self.howtouse_button = tk.Button(
            text="How to use",
            width="15",
            command=self.howto
        )
        #End buttons

        #Shell
        self.shell_label = tk.Label(
            text="Output"
        )
        self.shell_window = tk.Text(
            width=30,
            height=10
        )
        self.shell_window.config(state="disabled")
        #End Shell

        self.title.pack(pady=10)
        self.shortcut_display.pack(pady=30)
        self.shortcut_display.insert(0, f"Shortcut = {self.shortcut}")
        self.shortcut_display.config(state="disabled")

        self.change_shortcut_button.pack()
        self.howtouse_button.pack(pady=5)

        self.shell_label.pack(pady=5)
        self.shell_window.pack()
        self.shell_starter()
        #End TKINTER

    def shell_starter(self):
        self.shell_window.config(state="normal")
        try:
            keyboard.add_hotkey(self.shortcut, self.printer)
        except:
            self.shell_window.insert("end", "Cloudnt start...")
            self.shell_window.config(state="disabled")
        else:
            self.shell_window.insert("end", "Active...")
            self.shell_window.config(state="disabled")

    def printer(self):
        self.shell_window.config(state="normal") 
        self.shell_window.delete("1.0", tk.END)
        time.sleep(0.3)
        self.shell_window.insert("end", "Sending...")
        time.sleep(0.2)
        contents = pyperclip.paste()
        try:
            pyautogui.write(contents, interval=self.interval)
        except:
            self.shell_window.insert("end", "\nCouldnt send keystrokes..")
        else:
            self.shell_window.insert("end", "\nSuccessfully sendt.")
        self.shell_window.config(state="disabled")

    def settings(self):
        self.settings_window = tk.Toplevel(root)
        self.settings_window.title("Settings")
        self.settings_window.geometry("500x500")
        self.shortcut_label = tk.Label(
            text="Shortcut",
            master=self.settings_window
        )
        self.shortcut_var = tk.Entry(
            master=self.settings_window
        )
        self.keystroke_label = tk.Label(
            text="Keystroke Delay",
            master=self.settings_window
        )
        self.keystroke_var = tk.Entry(
            master=self.settings_window,
        )
        self.exit_button = tk.Button(
            text="Apply",
            command=self.saver,
            master=self.settings_window,
            width=10
        )
        self.shortcut_label.pack(pady=5)
        self.shortcut_var.pack(pady=10)
        self.keystroke_label.pack(pady=5)
        self.keystroke_var.pack()
        self.exit_button.pack(pady=100)
        self.shortcut_var.insert(0, self.shortcut)
        self.keystroke_var.insert(0, self.interval)

    def saver(self):
        self.shortcut = self.shortcut_var.get()
        self.interval = self.keystroke_var.get()
        self.shortcut_display.config(state="normal")
        self.shortcut_display.delete(0, tk.END)
        self.shortcut_display.insert(0, f"Shortcut = {self.shortcut}")
        self.shortcut_display.config(state="disabled")
        self.settings_window.destroy()
        keyboard.remove_all_hotkeys()
        keyboard.add_hotkey(self.shortcut, self.printer)

    def howto(self):
        self.howto_window = tk.Toplevel(root)
        self.howto_window.title("How to use")
        self.howto_window.resizable(False, False)
        self.howto_window.geometry("1000x1000")

        self.howto_label = tk.Label(
            text="To use PyperPaste, make sure the program is running and active.\n\nCopy any text using Ctrl+C, then click where you want the text to appear. \nWhen your cursor is in the correct place, press the shortcut shown at the top of the window. \nPyperPaste will read your clipboard and type the text automatically. \nTo change the shortcut or typing speed, click the Change settings button. \n\nEnter a new shortcut using a simple format like ctrl+b or ctrl+shift+v. \nAvoid using very common shortcuts. \n\nThe keystroke delay controls how fast the text is typed. \nSmaller numbers are faster, larger numbers are slower. \nA value around 0.05 to 0.15 works well, use larger number for\n larger clipboard contents. \n\nClick Apply to use the new settings. \nChanges take effect immediately. \n\nYour settings are not saved permanently. \n\nIf you enter a bad shortcut or something stops working, \njust restart the program and try again. \nThis will reset everything to the default values.\n\n\nThank you for using PyperPaste!",
            master=self.howto_window
        )
        self.howto_label.pack()
        self.howto_window.mainloop()
def is_admin():
    try:
        return ctypes.windll.shell32.IsUserAnAdmin()
    except:
        return False

if not is_admin():
    ctypes.windll.shell32.ShellExecuteW(
        None,
        "runas",        
        sys.executable, 
        " ".join(sys.argv),
        None,
        1
    )
    sys.exit(0)

root = tk.Tk()     
app = PyperPaste(root)
root.mainloop()