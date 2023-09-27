import requests
import os
import folium
import time
import xml.etree.ElementTree as ET
from decouple import config

url = config('API_KEY')


def getNextStop(route):
    attribute = 'next'
    stop_ids = []
    stop_names = []

    response = requests.get(url)

    if response.status_code == 200:
        bus_data = response.text
        root = ET.fromstring(bus_data) 
        bus_elements = root.findall(".//bus")

        for bus_element in bus_elements:
            attribute_value = bus_element.get(attribute)
            if bus_element.get('code') != 4: # checks if bus is active
        
                if bus_element.get('route') == str(route):
                    stop_ids.append(attribute_value)
            with open(os.path.abspath(os.path.dirname(__file__))+'/gtfs/stops.txt', 'r', encoding='utf-8') as file:

                file_content = file.read()
                for line in file_content.splitlines():
                    line = line.split(',')
                    if line[0] in stop_ids:
                        stop_names.append(line[1])

            return stop_names
    else:
        return f'failed to retrieve data. Status code: {response.status_code}'

def getBusCoordinates(route = 0):
    coordinates = {}
    response = requests.get(url)

    if response.status_code == 200:
        bus_data = response.text
        root = ET.fromstring(bus_data) 
        bus_elements = root.findall(".//bus")

        for bus_element in bus_elements:
            latitude_value = bus_element.get('lat')
            longitude_value = bus_element.get('lon')
            bus_route = bus_element.get('route')  

            if route == 0 or bus_route == str(route):
                c = (latitude_value, longitude_value)

                if bus_route in coordinates: # if the route alr exists in the dict it just appends the coords to the route otherwise it creates the route in the dict
                    coordinates[bus_route].append(c)  
                else:
                    coordinates[bus_route] = [c]  

        return coordinates

    else:
        return f'failed to retrieve data. Status code: {response.status_code}'

latitude = 64.117927
longitude = -21.791984

while True:
    mymap = folium.Map(location=[latitude, longitude], zoom_control=15, min_zoom=7)
    coordinates = getBusCoordinates()

    for route, coords in coordinates.items():
        for coord in coords:
            try:
                folium.Marker(coord, 
                            popup='click', 
                            tooltip=route, 
                            icon=folium.CustomIcon(icon_image=f'straeto/assets/icons/{route}.png', icon_size=(32, 32))).add_to(mymap)
            except FileNotFoundError:
                print(f'{route}, icon not found')

    mymap.save('straeto/web/map.html')
    time.sleep(5)
