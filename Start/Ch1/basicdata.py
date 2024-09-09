# Example file for Advanced Python: Hands On by Joe Marini
# Introspect the data to make some determinations

import json
import pprint

# open the sample weather data file and use the json module to load and parse it
with open("../../sample-weather-history.json", "r") as weatherfile:
    weatherdata = json.load(weatherfile)

# TODO: What was the warmest day in the data set?
warmday = max(weatherdata, key=lambda x : x['tmax'])
print(f"The warmest day was {warmday['date']} at {warmday['tmax']} degrees")

# TODO: What was the coldest day in the data set?
coldday = min(weatherdata, key=lambda x : x['tmin'])
print(f"The coldest day was {coldday['date']} at {coldday['tmin']} degrees")

# TODO: How many days had snowfall?
# snowdays = 0
# for day in weatherdata:
#     if day['snow'] > 0:
#         snowdays += 1
#     else:
#         continue

# print(snowdays)

snowdays = [day for day in weatherdata if day['snow'] > 0]
print(f"Snow fell on {len(snowdays)} days.")
# pprint.pp(snowdays)


# TODO: What was the average snowfall across all days?
total_snow = sum(day['snow'] for day in weatherdata)
average_snow = total_snow / len(weatherdata)
print(f"The average snowfall across all days was {average_snow:.2f} inches.")

# TODO: What was the windiest day in the data set? - float error!!!!
# try:
#     windiest_day = max(weatherdata, key=lambda x: (x['awnd']))
#     print(f"The windiest day was {windiest_day['date']} with a wind speed of {windiest_day['awnd']} mph.")
# except TypeError as Er:
#     print(f"{Er} - read the error and modify data")


windiest_day = max(weatherdata, key=lambda x: x['awnd'] if x['awnd'] is not None else 0)
print(f"The windiest day was {windiest_day['date']} with a wind speed of {windiest_day['awnd']} mph.")

# TODO: How many days had no precipitation?
dry_days = [day for day in weatherdata if day['prcp'] == 0]
print(f"There were {len(dry_days)} dry days.")
# pprint.pp(dry_days)

# TODO: Which day had the largest temperature difference?
largest_diff_day = max(weatherdata, key=lambda x: x['tmax'] - x['tmin'])
temp_diff = largest_diff_day['tmax'] - largest_diff_day['tmin']
# print(f"The day with the largest temperature difference was {largest_diff_day['date']} with a difference of {temp_diff} degrees.")



