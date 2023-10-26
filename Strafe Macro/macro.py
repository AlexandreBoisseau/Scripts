from pynput import keyboard
from pynput.keyboard import Controller, Key
import time

kbd_controller = Controller()
counter_strafe_in_progress = False

def on_press(key):
    global counter_strafe_in_progress
    if counter_strafe_in_progress:
        if key == keyboard.KeyCode.from_char('s'):
            kbd_controller.release('f')
        elif key == keyboard.KeyCode.from_char('f'):
            kbd_controller.release('s')
        counter_strafe_in_progress = False

def on_release(key):
    global counter_strafe_in_progress
    if key == keyboard.KeyCode.from_char('s'):
        time.sleep(0.05)
        kbd_controller.press('f')
        counter_strafe_in_progress = True
    elif key == keyboard.KeyCode.from_char('f'):
        time.sleep(0.05)
        kbd_controller.press('s')
        counter_strafe_in_progress = True

with keyboard.Listener(on_press=on_press, on_release=on_release) as listener:
    listener.join()
