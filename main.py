import webbrowser
import pyperclip
import pyautogui as pg

import time

pg.FAILSAFE = False

contries_list = [
    "ประเทศญี่ปุ่น",
    "ประเทศสวิตเซอร์แลนด์",
    "ประเทศอิตาลี",
    "ประเทศนิวซีแลนด์",
    "ประเทศแคนาดา"
]

for i in range(len(contries_list)):

    init_position = pg.position()
    webbrowser.open('https://www.google.com')

    time.sleep(3)

    cord  =pg.locateOnScreen('searchPic.png', confidence=0.9)

    centerSearch = pg.center(cord)
    pg.click(centerSearch, duration=1)


    contry_name = contries_list[i]

    print(contry_name)

    pyperclip.copy(contry_name)

    time.sleep(2)

    pg.hotkey('ctrl', 'v')
    pg.hotkey('enter')

    time.sleep(2)

    pg.screenshot('{}.png'.format(contry_name))

    time.sleep(1)

    pg.hotkey('ctrl', 'w')

    pg.move(init_position)
    time.sleep(1)