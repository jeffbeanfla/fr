from FlightRadar24 import FlightRadar24API, Countries
import time
from rgbmatrix import RGBMatrix, RGBMatrixOptions, graphics
import operator
from datetime import datetime
import requests

while True:
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
    font.LoadFont("./fonts/6x10.bdf")
    textColor1 = graphics.Color(0, 0, 255)
    textColor2 = graphics.Color(255, 0, 0)
    textColor3 = graphics.Color(0,255,0)
    
    start_time=time.time()

    fr_api = FlightRadar24API()
    flights =  fr_api.get_flights()

    ap = "FLL"

    match ap:

     case "MIA":

        bounds=fr_api.get_bounds_by_point(25.7,-80.50,20000)
        min_lat=25.70
        max_lat=26.00
        min_lon=-80.25
        max_lon=-80.60    
        ar = fr_api.get_airport(ap) 

     case "FLL":

        bounds=fr_api.get_bounds_by_point(26.07365,-80.15153,20000)
        min_lat=25.90
        max_lat=26.20
        min_lon=-80.00
        max_lon=-80.60     
        ar = fr_api.get_airport(ap)

    flights=fr_api.get_flights(bounds = bounds)
    x = 0
    for flight in flights:

    #   if flight.number == "DL188":
        f=flight
        d=fr_api.get_flight_details (f)
        distance=f.get_distance_from (ar)
        f.set_flight_details(d)
         
        #try:
        #    minutes=(distance/f.ground_speed)*60
        #    tt=(distance/f.ground_speed)
        #except:
        #    result=0 
            
        #ct=datetime.fromtimestamp(minutes)
        #ft=ct.strftime('%M:%S')

        if f.destination_airport_iata == ar.iata and f.altitude > 50: #  and min_lat<= f.latitude <=max_lat and min_lon>=f.longitude >=max_lon:
                x += 1
                print("FlightNo",f.number, "From",f.origin_airport_iata,"To",f.destination_airport_iata, "Alt",f.altitude,"Speed",f.ground_speed,"Dist", distance,"Type",f.aircraft_model,f.latitude, f.longitude)
                    
                #create canvas with text
                canvas = matrix.CreateFrameCanvas()
                graphics.DrawText(canvas, font, 1, 10, textColor1, f.origin_airport_iata)
                graphics.DrawText(canvas, font, 25, 10, textColor1, f.number)
                graphics.DrawText(canvas, font, 1, 20, textColor2, "Speed " + str(f.ground_speed))
                graphics.DrawText(canvas, font, 1, 30, textColor3, "Alt " + str(f.altitude))

                matrix.Clear()
                matrix.SwapOnVSync(canvas)
                time.sleep(5)
                matrix.Clear()
                if x > 20 :
                    break
    end_time=time.time()
    print(end_time-start_time)
time.sleep(60)

