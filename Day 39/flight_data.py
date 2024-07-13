import requests

SHEETY_URL = "https://api.sheety.co/cadbae6f22de826dd76b436194851e39/copyOfFlightDeals/prices"
class FlightData:
    def __init__(self):
        #This class is responsible for structuring the flight data.
        self.data = requests.get(SHEETY_URL).json()['prices']

