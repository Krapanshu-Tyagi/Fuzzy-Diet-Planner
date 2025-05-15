# core/nutrition_engine.py

def calculate_bmi(height_cm, weight_kg):
    height_m = height_cm / 100
    return round(weight_kg / (height_m ** 2), 2)


def calculate_bmr(age, gender, height_cm, weight_kg):
    if gender.lower() == 'male':
        # Mifflin-St Jeor Equation for Men
        return 10 * weight_kg + 6.25 * height_cm - 5 * age + 5
    else:
        # For Women
        return 10 * weight_kg + 6.25 * height_cm - 5 * age - 161


def calculate_tdee(bmr, activity_level):
    # Activity multipliers:
    activity_factors = {
        'sedentary': 1.2,
        'light': 1.375,
        'moderate': 1.55,
        'active': 1.725,
        'very active': 1.9
    }
    return bmr * activity_factors.get(activity_level.lower(), 1.2)

def get_personalized_nutrition(age, height, weight, gender, goal, activity):
    # Dummy sample for structure (replace with real logic)
    bmi = weight / ((height / 100) ** 2)
    bmr = 10 * weight + 6.25 * height - 5 * age + (5 if gender.lower() == 'male' else -161)
    
    tdee_map = {
        "Sedentary": 1.2, "Light": 1.375, "Moderate": 1.55,
        "Active": 1.725, "Very Active": 1.9
    }
    tdee = bmr * tdee_map.get(activity, 1.2)

    calorie_targets = [tdee - 500, tdee, tdee + 300]  # [loss, maintain, gain]
    fuzzy_calories = calorie_targets[goal]
    fuzzy_protein = weight * 1.6  # Simplified

    return {
        "bmi": round(bmi, 2),
        "bmr": round(bmr),
        "tdee": round(tdee),
        "fuzzy_calories": round(fuzzy_calories),
        "fuzzy_protein": round(fuzzy_protein)
    }
