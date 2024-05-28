from geopy.distance import geodesic
from geopy.geocoders import Nominatim

# растояние между кординатами
def get_dist(start, finish):
    distance = geodesic(start, finish).meters
    return f'{distance:2f}'

#print(get_dist(start,finish))

geo1 = (44.6074444444444, 40.1074166666666)
geo2 = (46.32112814, 44.28560673)

# поиск адреса по кординатам
def get_address(point):
    geolocator = Nominatim(user_agent="GetLoc")
    location = geolocator.reverse(point)
    return location.address

print(get_dist(geo1,geo2))