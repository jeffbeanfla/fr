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
x = 0
for flight in flights:
    x += 1
    print(flight.number,flight.origin_airport_iata,flight.destination_airport_iata)
    #create canvas with text
    canvas = matrix.CreateFrameCanvas()
    graphics.DrawText(canvas, font, 15, 15, textColor, flight.origin_airport_iata)
    graphics.DrawText(canvas, font, 15, 25, textColor, flight.destination_airport_iata)

    matrix.Clear()
    matrix.SwapOnVSync(canvas)
    time.sleep(5)
    matrix.Clear()
    if x > 20 :
        break

