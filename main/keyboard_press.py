from pynput.keyboard import Key, Listener
import time
import threading


def on_press_start(key):
    if key == Key.ctrl_l:
        time.sleep(1)
        return False


def on_press_end(key):
    # print(f'You press {key}')
    if key == Key.ctrl_r:
        return False


def press_start():
    with Listener(on_press=on_press_start) as listener:
        listener.join()


def press_end():
    with Listener(on_press=on_press_end) as listener:
        listener.join()
