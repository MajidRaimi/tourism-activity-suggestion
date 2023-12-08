
import random
import csv

def load_activities_from_csv(file_path):
    activities = {"outdoor": {}, "indoor": {}}
    with open(file_path, mode='r', encoding='utf-8') as file:
        csv_reader = csv.DictReader(file)
        for row in csv_reader:
            type_key = row["Type"]
            weather_key = row["Weather"]
            activity = row["Activity"]

            if weather_key in activities:
                if type_key not in activities[weather_key]:
                    activities[weather_key][type_key] = []
                activities[weather_key][type_key].append(activity)
    return activities

def suggest_tourism_activity(activities, weather_preference, activity_type):
    if weather_preference in ["outdoor", "indoor"]:
        if activity_type in activities[weather_preference]:
            return random.choice(activities[weather_preference][activity_type])
        else:
            return "Explore the city"
    else:
        all_activities = []
        for category in activities.values():
            all_activities.extend(category.get(activity_type, []))
        return random.choice(all_activities) if all_activities else "Explore the city"