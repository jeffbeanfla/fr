from FlightRadar24 import FlightRadar24API, Countries
import operator
import time
from datetime import datetime

fr_api = FlightRadar24API()
#airlines = fr_api.get_airlines()
#for airline in airlines:
#   print ({airline['ICAO']},{airline['Name']})

airports = fr_api.get_airports([Countries.UNITED_STATES])

for a in airports:
      if a.iata == 'MIA':
             #print(a.name,a.iata,a.icao,a.latitude,a.longitude)
             ar = a
             


bounds=fr_api.get_bounds_by_point(25.795160,-80.279594,1000000)
#bounds=fr_api.get_bounds_by_point(26.07365,-80.15153,100000)  FLL
#time_left==0
#ft==0
flights=fr_api.get_flights(bounds = bounds)
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
            print(f.number, f.origin_airport_iata,f.destination_airport_iata,distance, f.altitude,f.ground_speed,f.aircraft_model,minutes,ft)
            

