from pynput import keyboard
import time

def on_release(key):
    print(key)

listener = keyboard.Listener(on_release=on_release)
listener.start()

while True:
    # do whatever you need here)
    key = listener