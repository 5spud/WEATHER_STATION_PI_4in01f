import epd4in01f
import time
from weather import *
from news import *
from display import *
import json
print("Starting shut down")
epd = epd4in01f.EPD()
epd.init()
time.sleep(1)
print("Clearing...")
epd.Clear()
time.sleep(2)
epd.init()
# print("Exiting !")
# doesn´t exit: epd.Dev_exit()
   # FRAME
    display = Display()
    display.draw_black.rectangle((5, 5, 795, 475), fill=255, outline=0, width=2)  # INNER FRAME
    display.draw_black.line((540, 5, 540, 350), fill=0, width=1)  # VERTICAL SEPARATION
    display.draw_black.line((350, 5, 350, 350), fill=0, width=1)  # VERTICAL SEPARATION slim
    display.draw_black.line((5, 350, 795, 350), fill=0, width=1)  # HORIZONTAL SEPARATION

print("Bye")
exit()
