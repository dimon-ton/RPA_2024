import webbrowser
import pyperclip
import pyautogui as pg
from datetime import datetime
import time

from songline import Sendline
import os

token = '4ED99HkYOoqVUEdd6SPN4OOegI3S7zqu5ZYYwi5QstA'

dir_path = os.path.dirname(os.path.abspath(__file__))

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


    d = datetime.now().strftime('%Y_%m_%d_%H_%M_%S')
    pg.screenshot('{}_{}.png'.format(d,contry_name))

    time.sleep(3)

   
    
    img_path = os.path.join(dir_path, '{}_{}.png'.format(d,contry_name))


    print(img_path)

    line_bot = Sendline(token)
    line_bot.sendimage_file(img_path)

    time.sleep(1)

    pg.hotkey('ctrl', 'w')

    pg.move(init_position)
    time.sleep(1)