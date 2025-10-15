from FlightRadar24 import FlightRadar24API,Countries
fr_api = FlightRadar24API()

flights =  fr_api.get_flights()

for flight in flights:
    print({flight.id})

