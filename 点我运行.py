import pyautogui as pg
import pyperclip as pc
import time
import threading
from main import keyboard_press, process_config


def auto_write():
    write_speed, by, long = process_config.process_json()
    with open('将想要复制的内容写在我这儿.txt', 'r', encoding='utf-8') as f:
        lines = f.readlines()
    pg.typewrite('*')
    pg.press('backspace')

    if by == 0:
        for line in lines:
            for index in range(0, len(line), long):
                content = line[index: index + long] if len(line) - index >= long else line[index:]
                print(str(content), end='')
                pc.copy(content)
                pg.hotkey('Ctrl', 'v')
                time.sleep(write_speed)
    elif by == 1:
        for index in range(0, len(lines), long):
            contents = lines[index: index + long] if len(lines) - index >= long else lines[index:]
            content = ''
            for line in contents:
                content += line
            print(str(content), end='')
            pc.copy(str(content))
            pg.hotkey('Ctrl', 'v')
            time.sleep(write_speed)
    else:
        contents = lines
        content = ''
        for line in contents:
            content += line
        print(str(content), end='')
        pc.copy(str(content))
        pg.hotkey('Ctrl', 'v')

    pg.typewrite('*')
    pg.press('backspace')


keyboard_press.press_start()
t1 = threading.Thread(target=auto_write, daemon=True)
t1.start()
keyboard_press.press_end()
