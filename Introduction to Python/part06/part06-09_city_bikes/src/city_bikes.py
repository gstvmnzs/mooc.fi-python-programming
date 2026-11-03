def get_station_data(filename: str):
    locations = {}
    with open(filename) as file:
        for line in file:
            line = line.strip()
            line = line.split(";")
            if "Longitude" in line:
                continue
            
            locations[line[3]] = (float(line[0]), float(line[1]))
    return locations
    
def distance(stations:dict, station1:str, station2:str):
    from math import sqrt
    
    longitude1 = stations[station1][0]
    latitude1 = stations[station1][1]
    longitude2 = stations[station2][0]
    latitude2 = stations[station2][1]
    
    x_km = (longitude1 - longitude2) * 55.26
    y_km = (latitude1 - latitude2) * 111.2
    distance_km = sqrt(x_km**2 + y_km**2)
    
    return distance_km

def greatest_distance(stations:dict):
    greatest = None
    station1 = None
    station2 = None
    
    for test1 in stations:
        for test2 in stations:
            if test1 == test2:
                continue
            distance_between = distance(stations, test1, test2)
            if greatest == None or distance_between > greatest:
                station1 = test1
                station2 = test2
                greatest = distance_between
    return (station1, station2, greatest)