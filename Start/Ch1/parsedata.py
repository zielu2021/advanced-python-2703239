# Example file for Advanced Python: Hands On by Joe Marini
# Load and parse a JSON data file and determine some information about it
import json
import pprint
# TODO: open the sample weather data file and use the json module to load and parse it
with open("../../sample-weather-history.json", "r") as weatherfile:
    weatherdata = json.load(weatherfile)

# TODO: make sure the data loaded correctly by printing the length of the dataset
print(len(weatherdata))
# TODO: let's also take a look at the first item in the data

pprint.pp(weatherdata[0])
# TODO: How many days of data do we have for each year?

years = {}

for d in weatherdata:
    key = d['date'][0:4]
    if key in years:
        years[key] += 1
    else:
        years[key] = 1


# pprint.pp(years, width=5)


# TODO : Similar task with logic 1
salesdata = [
    {'date': '2021-01-15', 'amount': 150},
    {'date': '2021-07-21', 'amount': 200},
    {'date': '2022-02-05', 'amount': 300},
    {'date': '2022-12-22', 'amount': 250},
    {'date': '2023-03-13', 'amount': 100}
]

{
    '2021': 350,
    '2022': 550,
    '2023': 100
}


# TODO : Similar task with logic 2
activities = [
    {'timestamp': '2023-01-15T08:30:00', 'duration': 45},
    {'timestamp': '2023-01-22T10:00:00', 'duration': 30},
    {'timestamp': '2023-02-05T11:15:00', 'duration': 60},
    {'timestamp': '2023-02-22T14:00:00', 'duration': 90},
    {'timestamp': '2023-03-13T09:00:00', 'duration': 40}
]

{
    '2023-01': 75,
    '2023-02': 150,
    '2023-03': 40
}

monthly_duration = {}

for d in activities:
    key = d['timestamp'][0:7]
    if key in monthly_duration:
        monthly_duration[key] += d['duration']
    else:
        monthly_duration[key] = d['duration']


# pprint.pp(monthly_duration, width=5)

# TODO : Similar task with logic 3
activities = [
    {'timestamp': '2023-01-15T08:30:00', 'activity_type': 'exercise', 'duration': 45},
    {'timestamp': '2023-01-22T10:00:00', 'activity_type': 'study', 'duration': 30},
    {'timestamp': '2023-02-05T11:15:00', 'activity_type': 'exercise', 'duration': 60},
    {'timestamp': '2023-02-22T14:00:00', 'activity_type': 'study', 'duration': 90},
    {'timestamp': '2023-03-13T09:00:00', 'activity_type': 'leisure', 'duration': 40},
    {'timestamp': '2023-03-25T17:00:00', 'activity_type': 'exercise', 'duration': 50}
]

{
    '2023-01': {
        'exercise': 45,
        'study': 30
    },
    '2023-02': {
        'exercise': 60,
        'study': 90
    },
    '2023-03': {
        'leisure': 40,
        'exercise': 50
    }
}

daily_activities = {}

for d in activities:
    key = d['timestamp'][0:7]
    activity_type = d['activity_type']
    duration = d['duration']

    if key not in daily_activities:
        daily_activities[key] = {}

    if activity_type in daily_activities[key]:
        daily_activities[key][activity_type] += duration
    else:
        daily_activities[key][activity_type] = duration

# pprint.pp(daily_activities, width=40)




# TODO : Similar task with logic 4
tasks = [
    {'timestamp': '2023-01-15T08:30:00', 'project_name': 'Project A', 'task_type': 'development', 'duration': 120},
    {'timestamp': '2023-01-22T10:00:00', 'project_name': 'Project A', 'task_type': 'meeting', 'duration': 60},
    {'timestamp': '2023-01-30T14:00:00', 'project_name': 'Project B', 'task_type': 'development', 'duration': 90},
    {'timestamp': '2023-02-05T11:15:00', 'project_name': 'Project A', 'task_type': 'testing', 'duration': 45},
    {'timestamp': '2023-02-20T09:00:00', 'project_name': 'Project B', 'task_type': 'development', 'duration': 120},
    {'timestamp': '2023-03-13T09:00:00', 'project_name': 'Project C', 'task_type': 'meeting', 'duration': 50},
    {'timestamp': '2023-03-25T17:00:00', 'project_name': 'Project A', 'task_type': 'development', 'duration': 70}
]

{
    '2023-01': {
        'Project A': {
            'development': 120,
            'meeting': 60
        },
        'Project B': {
            'development': 90
        }
    },
    '2023-02': {
        'Project A': {
            'testing': 45
        },
        'Project B': {
            'development': 120
        }
    },
    '2023-03': {
        'Project A': {
            'development': 70
        },
        'Project C': {
            'meeting': 50
        }
    }
}


monthly_activity_duration = {}

for d in tasks:
    key = d['timestamp'][0:7]
    project_name = d['project_name']
    task_type = d['task_type']
    duration = d['duration']

    if key not in monthly_activity_duration:
        monthly_activity_duration[key] = {}

    if project_name not in monthly_activity_duration[key]:
        monthly_activity_duration[key][project_name] = {}
    
    if task_type in monthly_activity_duration[key][project_name]:
        monthly_activity_duration[key][project_name][task_type] += duration
    else:
        monthly_activity_duration[key][project_name][task_type] = duration

# pprint.pp(monthly_activity_duration, width=40)