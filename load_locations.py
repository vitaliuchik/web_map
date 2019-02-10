from geopy.geocoders import MapBox
from geopy.exc import GeocoderServiceError
geolocator = MapBox(api_key='pk.eyJ1Ijoicm9tYW4yMjIzNCIsImEiOiJjanJ1b2lkdmgxNWhoNDNxc3B4Y2o0dnE4In0.-o_eVMh-dV2YuhI8qbtp-Q')


file = open('addresses.txt', encoding='latin-1')
addresses = file.readlines()
file.close()

file = open('locations.txt', 'w', encoding='latin-1')
for address in addresses:
    address = address[:-1]
    try:
        location = geolocator.geocode(address)
        print(location.latitude, location.longitude, file=file)
    except AttributeError as err:
        print(err, file=file)
    except NameError as err:
        print(err, file=file)
    except GeocoderServiceError as err:
        print(err, file=file)
file.close()