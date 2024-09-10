# Python code​​​​​​‌​‌‌‌​‌‌​‌‌‌‌​‌‌​‌‌‌‌​​​‌ below
# Use print("messages...") to debug your solution.

import json
import random
import pprint


def select_days(year, month):
    # Your code goes here
    with open("../../sample-weather-history.json", "r") as weatherfile:
        weatherdata = json.load(weatherfile)

    yearmonth = year + "-" + month

    def yearmonthfilter(day):
        if yearmonth in day['date']:
            return True
        return False
    
    yearmonthdata = list(filter(yearmonthfilter, weatherdata))

    datalist = random.sample(yearmonthdata, k=5)

    return datalist

pprint.pp(select_days('2024','12'))