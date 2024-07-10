 Keystroke Logger with Active Window Tracking

 Overview
This Python script logs keystrokes and tracks active window titles. It is useful for monitoring which windows were active during specific keystrokes. The script captures both regular and special key presses and logs them into a file along with the active window title and process name.

 Features
- Logs every keystroke, including special keys like space, enter, and function keys.
- Tracks and logs the title and process name of the active window whenever it changes.
- Exits and stops logging when the `esc` key is pressed.
- Includes debugging statements for better understanding of the script's behavior.

 Prerequisites
Ensure you have the following Python libraries installed:
- `pynput`: For capturing keyboard events.
- `psutil`: For retrieving process information.
- `pygetwindow`: For retrieving the active window's title.

You can install the required libraries using `pip`:
```sh
pip install pynput psutil pygetwindow
