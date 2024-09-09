import json
from datetime import date, timedelta

with open("../../sample-weather-history.json", "r") as weatherfile:
    weatherdata = json.load(weatherfile)

# Find the coldest day
coldest_day = min(weatherdata, key=lambda d: d['tmin'])
print(coldest_day)

coldest_date = date.fromisoformat(coldest_day['date'])
print(f"The coldest day of the year was {str(coldest_date)} ({coldest_day['tmin']} degrees )")

# Looking for data for the next 7 days
avg_temp = 0.0
next_date = coldest_date

# Loop through the next 7 days
for _ in range(7):
    next_date += timedelta(days=1)
    
    # Manually search for the weather data matching the next_date
    wd = None
    for day in weatherdata:
        if day['date'] == str(next_date):
            wd = day
            break  # Exit loop once we find the matching day
    
    # If the day is found, calculate average temperature
    if wd:
        avg_temp += (wd['tmin'] + wd['tmax']) / 2
    else:
        print(f"No data for {next_date}")

# Calculate the average temperature over the 7 days
avg_temp = avg_temp / 7
print(f"The average temp for the next 7 days was {avg_temp}")
