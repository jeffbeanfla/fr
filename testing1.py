from FlightRadar24 import FlightRadar24API, Countries
import operator
import time
from datetime import datetime
import requests

fr_api = FlightRadar24API()
#airlines = fr_api.get_airlines()
#for airline in airlines:
#   print ({airline['ICAO']},{airline['Name']})

airports = fr_api.get_airports([Countries.UNITED_STATES])

for a in airports:
      if a.iata == 'MIA':
             #print(a.name,a.iata,a.icao,a.latitude,a.longitude)
             ar = a
             


#bounds=fr_api.get_bounds_by_point(25.795160,-80.279594,1000000)
bounds=fr_api.get_bounds_by_point(26.07365,-80.15153,100000)  #FLL
#time_left==0
#ft==0

min_lat=25.70#26.00
max_lat=25.80#26.20
min_lon=-80.25#-79.00
max_lon=-80.50#-80.60



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
    
    #if f.destination_airport_name == 'Miami International Airport' and operator.gt(distance,5):
    if f.destination_airport_iata == 'MIA' and operator.gt(distance,5):
            x += 1
            print("FlightNo",f.number, "From",f.origin_airport_iata,"To",f.destination_airport_iata,"Dist",distance, "Alt",f.altitude,"Speed",f.ground_speed,"Type",f.aircraft_model,"Time Left",ft,f.latitude, f.longitude)
            if min_lat<= f.latitude <=max_lat and min_lon>=f.longitude >=max_lon:
                print("Y")
    
    #x =  x + 1     
    if x > 20 :
                break
