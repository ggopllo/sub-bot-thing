#you need to install pyautogui for to work
import time
import pyautogui as pg
import webbrowser
url = ("https://www.youtube.com/channel/UCvV663CnZxx1pREz_Qy2b6Q?sub_confirmation=1")
webbrowser.open_new(url)
True
pg.moveTo(1415,613,2)
pg.click()
