import epd4in01f
import time
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
print("Bye")
exit()
