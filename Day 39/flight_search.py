class FlightSearch:
    #This class is responsible for talking to the Flight Search API.
    def __init__(self,data):
        data['iataCode'] = 'TESTING'