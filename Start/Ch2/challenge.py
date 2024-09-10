# Python code​​​​​​‌​‌‌‌​‌‌​​‌‌‌​‌​​​​‌‌‌‌​‌ below


import json
from functools import reduce

def miserable_day():
    with open("../../sample-weather-history.json", "r") as weatherfile:
        weatherdata = json.load(weatherfile)

        result = reduce(day_rank, weatherdata)
        return result

def misery_score(day):
    wind = 0 if day['awnd'] is None else day['awnd']
    temp = day['tmax'] * 0.8
    rain = day['prcp'] * 10
    
    score = (temp + rain + wind) / 3
    return score

def day_rank(acc, elem):
    return acc if misery_score(acc) >= misery_score(elem) else elem


print(miserable_day())