# Python code​​​​​​‌​‌‌‌​‌‌‌​​​‌‌‌‌​​​‌‌​‌‌‌ below
# Use print("messages...") to debug your solution.


def count_days():
    import json
    import statistics

    # open the sample weather data file and use the json module to load and parse it
    with open("../../sample-weather-history.json", "r") as weatherfile:
        weatherdata = json.load(weatherfile)

    def average_temp(day):
        return (day['tmin'] + day['tmax']) / 2
    
    #select the days from the winter months from all the years
    winters = ['-12-', '-01-', '-02-']
    winter_months = [d for d in weatherdata if any([month in d['date'] for month in winters])]

    avg_temps = [average_temp(day) for day in winter_months]
    avg_mean = statistics.mean(avg_temps)

    outlier_temp = avg_mean + statistics.stdev(avg_temps) * 2
    outliers = [day for day in winter_months if average_temp(day) >= outlier_temp]


    return len(outliers)
