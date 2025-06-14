class FlightData:
    #This class is responsible for structuring the flight data.
    def __init__(self, origin_airport, dest_airport, leave_date, return_date, price):        
        self.origin_airport = origin_airport
        self.destination_airport = dest_airport
        self.out_date = leave_date
        self.return_date = return_date
        self.price = price

    def find_cheapest_flight(self, data):            
        if data is None or not data['data']:
            print("No flight data")
            return FlightData("N/A", "N/A", "N/A", "N/A", "N/A")
        first_flight = data['data'][0]    
        origin = first_flight["itineraries"][0]["segments"][0]["departure"]["iataCode"]
        dest = first_flight["itineraries"][0]["segments"][0]["arrival"]["iataCode"]
        out_date = first_flight["itineraries"][0]["segments"][0]["departure"]["at"].split("T")[0]
        return_date = first_flight["itineraries"][1]["segments"][0]["departure"]["at"].split("T")[0]    
        lowest_price = float(first_flight["price"]["grandTotal"])
        cheapest_flight = FlightData(origin, dest, out_date, return_date, lowest_price)

        for flight in data["data"]:
            price = float(flight["price"]["grandTotal"])
            if price < lowest_price:                
                origin = flight["itineraries"][0]["segments"][0]["departure"]["iataCode"]
                dest = flight["itineraries"][0]["segments"][0]["arrival"]["iataCode"]
                out_date = flight["itineraries"][0]["segments"][0]["departure"]["at"].split("T")[0]
                return_date = flight["itineraries"][1]["segments"][0]["departure"]["at"].split("T")[0]
                cheapest_flight = FlightData(origin, dest, out_date, return_date, lowest_price)
                lowest_price = price        

        return cheapest_flight