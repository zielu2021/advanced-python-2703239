import json 
from datetime import date, timedelta

with open("../../sample-weather-history.json", "r") as weatherfile:
    weatherdata = json.load(weatherfile)

#Task 1
"""Objective: Modify the weather code to find the warmest day based on the maximum temperature (tmax),
and then print the date in the format "Tue, 14 Dec 2021"."""
warmest_day = max(weatherdata, key=lambda d:d['tmax'])

warmest_day_date = date.fromisoformat(warmest_day['date'])
print(warmest_day_date)

converted_w_d_d = warmest_day_date.strftime("%a, %d %b %Y")
print(converted_w_d_d)


#Task 2: Get Weather Data for Specific Dates Using next()
"""Objective: Write a function that, given a list of dates, retrieves the weather data for those dates using next(). 
If a date is not found, it should return "No data available for [date]"."""

def get_weather_for_dates(dates, weatherdata):
    # Create a dictionary for quick lookup
    weather_dict = {day['date']: day for day in weatherdata}
    
    # Use list comprehension to get weather data or "No data available" messages
    results = [
        f"Weather for {date.fromisoformat(date_str).strftime('%a, %d %b %Y')}: {weather_dict.get(date_str, 'No data available')}"
        if date_str in weather_dict else f"No data available for {date_str}"
        for date_str in dates
    ]
    
    return results

# Example usage
dates_to_check = ["2023-12-14", "2021-12-15", "2021-12-16", "2021-12-20"]
results = get_weather_for_dates(dates_to_check, weatherdata)
for result in results:
    print(result)