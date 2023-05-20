import epd4in01f
import time
from weather import *
from news import *
from display import *
from PIL import Image,ImageDraw,ImageFont
import json
print("Starting shut down")
#wait for input
epd = epd4in01f.EPD()
input()
print("\n epd creation has been executed successfully.")
epd.init()
input()
print("\n init.")
time.sleep(1)
print("Clearing...")
epd.Clear()
#time.sleep(2)
#epd.init()
# print("Exiting !")
# doesn´t exit: epd.Dev_exit()
   # FRAME
   input()
print("\nDisplay")
    display = Display()
    display.draw_black.rectangle((5, 5, 795, 475), fill=255, outline=0, width=2)  # INNER FRAME
    display.draw_black.line((540, 5, 540, 350), fill=0, width=1)  # VERTICAL SEPARATION
    display.draw_black.line((350, 5, 350, 350), fill=0, width=1)  # VERTICAL SEPARATION slim
    display.draw_black.line((5, 350, 795, 350), fill=0, width=1)  # HORIZONTAL SEPARATION

 font24 = ImageFont.truetype(os.path.join(picdir, 'Font.ttc'), 24)
    font18 = ImageFont.truetype(os.path.join(picdir, 'Font.ttc'), 18)
    font30 = ImageFont.truetype(os.path.join(picdir, 'Font.ttc'), 40)
    
    # Drawing on the Horizontal image
    logging.info("1.Drawing on the Horizontal image...")
    Himage = Image.new('RGB', (epd.width, epd.height), 0xffffff)  # 255: clear the frame
    draw = ImageDraw.Draw(Himage)
    draw.text((10, 0), 'hello world', font = font24, fill = 0)
    draw.text((10, 20), '4.01inch e-Paper', font = font24, fill = 0)
    draw.text((10, 160), 'BLACK', font = font30, fill = epd.BLACK)
    draw.text((10, 200), u'OTANVCE', font = font30, fill = epd.ORANGE)
    draw.text((10, 240), u'GTRERN', font = font30, fill = epd.GREEN)
    draw.text((10, 280), u'BLUE', font = font30, fill = epd.BLUE)
    draw.text((10, 320), u'RED', font = font30, fill = epd.RED)
    draw.text((10, 360), u'YELLOW', font = font30, fill = epd.YELLOW)      
    # CLOSE?  
      
print("Bye")
exit()
