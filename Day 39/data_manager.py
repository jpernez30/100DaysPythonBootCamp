import requests
from pprint import pprint

update = "https://api.sheety.co/cadbae6f22de826dd76b436194851e39/copyOfFlightDeals/prices/"
class DataManager:
    #This class is responsible for talking to the Google Sheet.
    def __init__(self,data):
        for city in data:
            new_data = {
                "price": {
                    "iataCode": city["iataCode"]
                }
            }
            response = requests.put(
                url=f"{update}/{city['id']}",
                json=new_data
            )
            print(response.text)

