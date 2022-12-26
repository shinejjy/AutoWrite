import pyautogui as pg
import pyperclip as pc
from pynput.keyboard import Key, Listener
import time
import threading


def on_press_start(key):
    if key == Key.ctrl_l:
        time.sleep(1)
        return False


def on_press_end(key):
    print(f'You press {key}')
    if key == Key.ctrl_r:
        return False


def press_start():
    with Listener(on_press=on_press_start) as listener:
        listener.join()


def press_end():
    with Listener(on_press=on_press_end) as listener:
        listener.join()


def auto_write():
    with open('将想要复制的内容写在我这儿.txt', 'r', encoding='utf-8') as f:
        lines = f.readlines()
        pg.typewrite('*')
        pg.press('backspace')
        for line in lines:
            print(line)
            for word in line:
                pc.copy(word)
                pg.hotkey('Ctrl', 'v')
                time.sleep(0.13)
        pg.typewrite('*')
        pg.press('backspace')


press_start()
t1 = threading.Thread(target=auto_write, daemon=True)
t1.start()
press_end()
