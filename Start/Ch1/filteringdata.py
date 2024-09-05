# Example file for Advanced Python: Hands On by Joe Marini
# Filter values out of a data set based on some criteria

import json
import pprint

# open the sample weather data file and use the json module to load and parse it
# with open("../../sample-weather-history.json", "r") as weatherfile:
    # weatherdata = json.load(weatherfile)

# the filter() function gives us a way to remove unwanted data points
# TODO: create a subset of the data for days that had snowfall
# snowdays = list(filter(lambda d:d['snow'] > 0.0, weatherdata))
# print(len(weatherdata))
# print(len(snowdays))

# TODO: pretty-print the resulting data set
# pprint.pp(snowdays)

# filter can also be used on non-numerical data, like strings
# TODO: create a subset that contains summer days with heavy rain (more than 1 in, about 2.5cm)
# def is_summer_rain_day(d):
#     summer_months = ['-07-', '-08-']
#     if any([m in d['date']for m in summer_months]) and d['prcp'] >= 2.5:
#         return True
#     return False

# summerraindays = list(filter(is_summer_rain_day, weatherdata))

# print(len(weatherdata))
# print(len(summerraindays))

# pprint.pp(summerraindays)

#TODO: create a subset that contains winter days with heavy rain (more then 1.5cm)
def is_winter_rain_day(d):
    winter_months = ['-01-','-02','-11-','-12-']
    if any([m in d['date'] for m in winter_months]) and d['prcp'] > 1.5:
        return True
    return False

# winterrainydays = list(filter(is_winter_rain_day, weatherdata))

# print(len(winterrainydays))
# pprint.pp(winterrainydays)




#challenge

import json 
import pprint
def get_cold_windy_rainy_days():
    with open("../../sample-weather-history.json", "r") as weatherfile:
        weatherdata = json.load(weatherfile)

    def is_coldwindyrainyday(d):
        avg_temp = (d['tmax'] + d['tmin']) / 2
        total_prcp = d['snow'] + d['prcp']
        if avg_temp < 45 and total_prcp > 0.7 and d['awnd'] >= 10.0:
            return True
        return False

    blustery_days = list(filter(is_coldwindyrainyday, weatherdata))
    return blustery_days


print(get_cold_windy_rainy_days())

print(f"list of this days cotains {len(get_cold_windy_rainy_days())} days")