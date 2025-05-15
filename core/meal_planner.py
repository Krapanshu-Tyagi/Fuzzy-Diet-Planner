# core/meal_planner.py
import json
import random

def load_food_data(path='data/food_data.json'):
    with open(path, 'r') as f:
        return json.load(f)

def filter_foods(food_data, dietary_tags=[], excluded_tags=[]):
    filtered = []
    for item in food_data:
        tags = item.get('tags', [])
        if all(tag in tags for tag in dietary_tags) and not any(tag in tags for tag in excluded_tags):
            filtered.append(item)
    return filtered

def generate_meal_plan(calorie_target, protein_target, dietary_tags=[], excluded_tags=[]):
    food_data = load_food_data()
    foods = filter_foods(food_data, dietary_tags, excluded_tags)

    # Categorize by meal
    meals = {'breakfast': [], 'lunch': [], 'dinner': [], 'snack': []}
    for food in foods:
        meals[food['meal_type']].append(food)

    # Simple greedy planning — later we can optimize it
    daily_plan = {}
    for day in range(1, 8):
        plan = {'breakfast': [], 'lunch': [], 'dinner': [], 'snack': []}
        total_cal, total_protein = 0, 0

        for meal in ['breakfast', 'lunch', 'dinner']:
            if meals[meal]:
                choice = random.choice(meals[meal])
                plan[meal] = choice
                total_cal += choice['calories']
                total_protein += choice['protein']

        # Fill with snacks if under target
        while total_cal < calorie_target and meals['snack']:
            snack = random.choice(meals['snack'])
            plan['snack'].append(snack)
            total_cal += snack['calories']
            total_protein += snack['protein']
            if total_cal > calorie_target or total_protein > protein_target:
                break

        daily_plan[f'Day {day}'] = {
            'meals': plan,
            'totals': {
                'calories': total_cal,
                'protein': total_protein
            }
        }

    return daily_plan
