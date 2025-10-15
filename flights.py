from FlightRadar24 import FlightRadar24API,Countries
fr_api = FlightRadar24API()

flights =  fr_api.get_flights()
x = 0
for flight in flights:
    x += 1
    print({flight.callsign})
    if x > 10 :
        break
