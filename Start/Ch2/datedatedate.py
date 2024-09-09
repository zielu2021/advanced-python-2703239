import json 
from datetime import date, timedelta

with open("../../sample-weather-history.json", "r") as weatherfile:
    weatherdata = json.load(weatherfile)


#datetime module converting string to date 
# dateobj = date.fromisoformat(weatherdata[0]['date'])
# print(dateobj)
# print(type(dateobj))

# print(dateobj.weekday())

#todo what was the warmest weekend day in the dataset?
# def is_weekend_day(d):
#     day = date.fromisoformat(d['date'])
#     return (day.weekday() == 5 or day.weekday() == 6)

# weekend_days = list(filter(is_weekend_day, weatherdata))
# warmest_day = max(weekend_days, key= lambda d:d['tmax'])
# print(date.fromisoformat(warmest_day['date']).strftime('%a, %d %b %Y'))



#todo find the coldest day and then 7 next days
coldest_day = min(weatherdata, key=lambda d:d['tmin'])
print(coldest_day)

coldest_date = date.fromisoformat(coldest_day['date'])
print(f"The coldest day of the year was {str(coldest_date)} ({coldest_day['tmin']} degrees )")

#looking for data for next 7 days
avg_temp = 0.0
next_date = coldest_date
for _ in range(7):
    next_date += timedelta(days=1)
    wd = next((day for day in weatherdata if day['date'] == str(next_date)), None)
    avg_temp += (wd['tmin'] + wd['tmax']) / 2

avg_temp = avg_temp / 7
print(f"The average temp for the next 7 days was {avg_temp}")