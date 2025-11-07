
import time
import datetime
from datetime import date
from datetime import datetime
import python_weather

import asyncio
import os

from FlightRadar24 import FlightRadar24API, Countries
import time
from rgbmatrix import RGBMatrix, RGBMatrixOptions, graphics
import operator
from datetime import datetime
import requests


options = RGBMatrixOptions()
options.chain_length = 1
options.cols = 64
options.rows = 32
options.parallel = 1
options.brightness = 50
options.disable_hardware_pulsing = True
options.drop_privileges = 1
options.gpio_slowdown = 1
options.hardware_mapping = 'adafruit-hat'
options.inverse_colors = False
options.led_rgb_sequence = "RGB"
options.multiplexing = 0
options.pixel_mapper_config = ''
options.pwm_bits = 11
options.pwm_dither_bits = 0
options.pwm_lsb_nanoseconds = 130
options.row_address_type = 0
options.scan_mode = 0
options.show_refresh_rate = 0
matrix = RGBMatrix(options = options) 

#create font
font = graphics.Font()
font.LoadFont("./fonts/7x13.bdf")
font.LoadFont("./fonts/6x10.bdf")
textColor1 = graphics.Color(0, 0, 255)
textColor2 = graphics.Color(255, 0, 0)

async def main():
    async with python_weather.Client(unit=python_weather.IMPERIAL) as client:
        weather = await client.get('Fort Lauderdale')
        #now=time.localtime()
        now=datetime.now()
        ftoday= now.strftime("%H:%M:%S")
        print ("Today:",date.today(),"At:",ftoday ,"Temp:", weather.temperature,  "Outlook: ", weather.kind)
        
        str=ftoday
        dstr=str
        
        str=date.today()
        dstr=str.isoformat()
        
        str=f"{weather.kind}"
        dstr=str
        
        str=f"{weather.temperature}"
        dstr=str
        
        canvas = matrix.CreateFrameCanvas()
        graphics.DrawText(canvas, font, 1, 10, textColor1, dstr)
        
#graphics.DrawText(canvas, font, 25, 10, textColor1, f.number)
#graphics.DrawText(canvas, font, 1, 20, textColor2, "Speed " + str(f.ground_speed))
#graphics.DrawText(canvas, font, 1, 30, textColor2, "Alt " + str(f.altitude))

    matrix.Clear()
    matrix.SwapOnVSync(canvas)
    time.sleep(5)
    matrix.Clear()
    
asyncio.run(main())