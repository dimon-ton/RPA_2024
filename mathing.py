import pyautogui as pg
import time


rect_center = pg.locateCenterOnScreen('rect.png')


pg.click(rect_center)

pg.moveRel(100, -30, duration=1)



pg.dragRel(200, 150, duration=2)