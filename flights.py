from FlightRadar24 import FlightRadar24API, Countries
import time
from rgbmatrix import RGBMatrix, RGBMatrixOptions, graphics
import operator
from datetime import datetime
import requests

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

fr_api = FlightRadar24API()
flights =  fr_api.get_flights()
#airports = fr_api.get_airports([Countries.UNITED_STATES])

'''
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
            print(f.number,f.origin_airport_iata,f.destination_airport_iata,f.altitude)
 '''
airports = fr_api.get_airports([Countries.UNITED_STATES])

for a in airports:
      if a.iata == 'MIA':
             #print(a.name,a.iata,a.icao,a.latitude,a.longitude)
             ar = a
             
bounds=fr_api.get_bounds_by_point(25.7,-80.50,100000)
#bounds=fr_api.get_bounds_by_point(26.07365,-80.15153,100000)  #FLL
#time_left==0
#ft==0

min_lat=25.70#26.00
max_lat=26.00#26.20
min_lon=-80.25#-79.00
max_lon=-80.60#-80.60

flights=fr_api.get_flights(bounds = bounds)
x = 0
for flight in flights:

#   if flight.number == "DL188":
    f=flight
    d=fr_api.get_flight_details (f)
    distance=f.get_distance_from (ar)
    f.set_flight_details(d)
     
    time_left=time.time()-f.time

    try:
        minutes=(distance/f.ground_speed)*60
        tt=(distance/f.ground_speed)
    except:
        result=0
        
    ct=datetime.fromtimestamp(minutes)
    ft=ct.strftime('%M:%S')

    if f.destination_airport_iata == 'MIA' and operator.gt(distance,5) and min_lat<= f.latitude <=max_lat and min_lon>=f.longitude >=max_lon:
            x += 1
            print("FlightNo",f.number, "From",f.origin_airport_iata,"To",f.destination_airport_iata,"Dist",distance, "Alt",f.altitude,"Speed",f.ground_speed,"Type",f.aircraft_model,"Time Left",ft,f.latitude, f.longitude)
            #if min_lat<= f.latitude <=max_lat and min_lon>=f.longitude >=max_lon:
                #print("Y")


            #create canvas with text
            canvas = matrix.CreateFrameCanvas()
            graphics.DrawText(canvas, font, 1, 10, textColor1, f.origin_airport_iata)
            graphics.DrawText(canvas, font, 35, 10, textColor1, f.destination_airport_iata)
            graphics.DrawText(canvas, font, 1, 30, textColor2, f.number)
            graphics.DrawText(canvas, font, 35, 30, textColor2, str(f.altitude))

            matrix.Clear()
            matrix.SwapOnVSync(canvas)
            time.sleep(5)
            matrix.Clear()
            if x > 20 :
                break

