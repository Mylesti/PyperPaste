# PyperPaste

PyperPaste is a lightweight Windows utility that pastes clipboard contents by **simulating keystrokes** instead of using the standard paste operation.
It’s useful in environments where normal paste (`Ctrl+V`) is blocked, unreliable, or rate-limited.

The application runs with a simple Tkinter GUI and uses a global keyboard shortcut to type out whatever is currently in your clipboard.

# Features

* 📋 Reads text directly from the clipboard
* ⌨️ Types clipboard contents using simulated keystrokes
* 🔑 Configurable global hotkey
* ⏱ Adjustable typing speed (keystroke delay)
* 🖥 Simple Tkinter GUI
* 🔄 Automatically installs missing dependencies
* 🛡 Requests administrator privileges (required for global hotkeys)

# How It Works

1. You copy text normally (`Ctrl+C`)
2. Place your cursor where you want the text to appear
3. Press the configured shortcut (default: `Ctrl+B`)
4. PyperPaste reads the clipboard and **types the content character by character**

This bypasses applications that block or interfere with normal paste operations.

# Requirements

* **Operating System:** Windows
* **Python:** 3.8+
* **Administrator privileges** (required for the `keyboard` module)

# Python Dependencies

These are installed automatically at runtime if missing:

* `pyperclip`
* `keyboard`
* `pyautogui`

Standard library modules (no installation needed):

* `tkinter`
* `time`
* `os`
* `sys`
* `ctypes`

# Installation

Clone the repository:

```bash
git clone https://github.com/yourusername/PyperPaste.git
cd PyperPaste
```

Run the script:

```bash
python pyperpaste.py
```

If dependencies are missing, the script will install them automatically using `pip`.

> ⚠️ The script will restart itself with **administrator privileges** if not already running as admin.

---

# Usage

1. Run the program
2. Copy any text (`Ctrl+C`)
3. Click into the target application or text field
4. Press the displayed shortcut (`Ctrl+B` by default)
5. The text will be typed automatically

# Changing Settings

* Click **Change settings**
* Modify:

  * **Shortcut** (e.g. `ctrl+shift+v`)
  * **Keystroke delay** (recommended: `0.05 – 0.15`)
* Click **Apply**
* Changes take effect immediately

> Settings are **not saved permanently**. Restarting the program resets defaults.

---

# Notes & Limitations

* This tool **simulates keyboard input** — it is not instant like normal paste
* Large clipboard contents may take time to type
* Some applications may block simulated input
* Global hotkeys require administrator permissions
* Windows only (due to admin + input hook behavior)

---

# Security Considerations

* The application has access to clipboard contents
* It simulates keystrokes globally
* Only run code you trust
* Review the source before use

---

# Known Issues

* Invalid shortcuts can break hotkey registration until restart
* Extremely fast keystroke delays may cause dropped characters
* Tkinter UI is intentionally minimal and not themed

---

# License

MIT License

You are free to use, modify, and distribute this project.
No warranty is provided.
