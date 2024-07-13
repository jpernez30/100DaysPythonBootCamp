from pprint import pprint
from flight_data import *
from flight_search import *
from data_manager import *

sheet_data = FlightData()

for x in sheet_data.data:
       x =FlightSearch(x)

DataManager(sheet_data.data)

# DataManager(sheet_data.data)


