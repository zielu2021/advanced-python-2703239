import json
from collections import defaultdict
import pprint
from itertools import groupby

# open the sample weather data file and use the json module to load and parse it
with open("../../sample-weather-history.json", "r") as weatherfile:
    weatherdata = json.load(weatherfile)

# get all the measurements for a particular year
year = [day for day in weatherdata if "2022" in day['date']]

# pprint.pp(year,width=5)

year.sort(key= lambda d:d['prcp'])
# pprint.pp(year, width=5)

# datagroup = defaultdict(list)

# for d in year:
#     datagroup[d['prcp']].append(d['date'])

# print(f"{len(datagroup)} total precipitation groups")
# pprint.pp(datagroup)


#todo the same with func groupby-------------------

grouped = {k:list(v) for k,v in groupby(year, key=lambda d:d['prcp'])}

pprint.pp(grouped, width=5)

# for key, data in grouped.items():
#     print(f"Precip: {key}, # days: {len(data)}, Days: {list(map(lambda d:d['date'], data))}")

for key, data in grouped.items():
    print(f"{key}, days {len(data)}, days : {list(map(lambda d:d['date'], data))}")