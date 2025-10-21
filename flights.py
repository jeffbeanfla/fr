from FlightRadar24 import FlightRadar24API, Countries
import time
from rgbmatrix import RGBMatrix, RGBMatrixOptions, graphics

# rbg options
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
textColor = graphics.Color(175, 175, 0)


fr_api = FlightRadar24API()
flights =  fr_api.get_flights()
#airports = fr_api.get_airports([Countries.UNITED_STATES])


x = 0
for f in flights:
    #d=fr_api.get_flight_details (f)
    #for a in airports:
    #  if a.iata == f.destination_airport_iata:
             #print(a.name,a.iata,a.icao,a.latitude,a.longitude)
    #         ar = a
    #distance=f.get_distance_from (f.destination_airport_iata)
 
        if f.origin_airport_iata and f.altitude > 0:
            x += 1
            print(f.number,f.origin_airport_iata,f.destination_airport_iata,f.altitude,x)
        
            #create canvas with text
            canvas = matrix.CreateFrameCanvas()
            graphics.DrawText(canvas, font, 1, 10, textColor, f.origin_airport_iata)
            graphics.DrawText(canvas, font, 35, 10, textColor, f.destination_airport_iata)
            graphics.DrawText(canvas, font, 1, 30, textColor, f.number)
            graphics.DrawText(canvas, font, 35, 30, textColor, str(f.altitude))

            matrix.Clear()
            matrix.SwapOnVSync(canvas)
            time.sleep(5)
            matrix.Clear()
            if x > 20 :
                break

