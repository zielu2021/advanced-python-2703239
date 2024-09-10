# Example file for Advanced Python: Hands On by Joe Marini
# Using the statistics package

import json
import statistics

# open the sample weather data file and use the json module to load and parse it
with open("../../sample-weather-history.json", "r") as weatherfile:
    weatherdata = json.load(weatherfile)

# select the days from the summer months from all the years
summers = ["-06-","-07-","-08-"]
summer_months = [d for d in weatherdata if any([month in d['date'] for month in summers])]
print(f"Data for {len(summer_months)} summer days")

# TODO: calculate the mean for both min and max temperatures
max_temp = [d['tmax'] for d in summer_months]
min_temp = [d['tmin'] for d in summer_months]

print(max_mean := statistics.mean(max_temp))
print(min_mean := statistics.mean(min_temp))


# TODO: calculate the median values for min and max temperatures
print(statistics.median(max_temp))
print(statistics.median(min_temp))

# TODO: use the standard deviation function to find outlier temperatures
upper_outlier = max_mean + (statistics.stdev(max_temp) * 2)
lower_outlier = min_mean - (statistics.stdev(min_temp) * 2)

print(upper_outlier)
print(lower_outlier)


max_outliers = [t for t in max_temp if t >= upper_outlier]
min_outliers = [t for t in min_temp if t <= lower_outlier]
print(max_outliers)
print(min_outliers)