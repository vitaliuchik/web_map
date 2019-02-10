import folium
import json

file = open('addresses.txt')
addresses = file.readlines()
file.close()
file = open('locations.txt')
coords = file.readlines()
file.close()

locations = dict()
for address, coord in zip(addresses, coords):
    try:
        coord = coord[:-1].split()
        coord = [float(coord[0]), float(coord[1])]
        locations[address[:-1]] = coord
    except ValueError:
        pass

file = open('years.json')
years = json.loads(file.readline())
file.close()

year = str(input('Input year: '))

map = folium.Map()


for movie in years[year]:
    if movie[1] != '':
        try:
            folium.Marker(locations[movie[1]], popup=movie[0]).add_to(map)
        except TypeError:
            pass
        except KeyError:
            pass

# population
###################
def color_creator(population):
    if population < 2000:
        return "green"
    elif 2000 <= population <= 3500:
        return "yellow"
    else:
        return "red"


fg_pp = folium.FeatureGroup(name="Population")

fg_pp.add_child(folium.GeoJson(data=open('world.json', 'r',
                             encoding='utf-8-sig').read(),
                             style_function=lambda x: {'fillColor':'green'
    if x['properties']['POP2005'] < 10000000
    else 'orange' if 10000000 <= x['properties']['POP2005'] < 20000000
    else 'red'}))

map.add_child(fg_pp)
map.add_child(folium.LayerControl())
map.save('Map.html')

