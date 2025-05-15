# core/fuzzy_system.py
import numpy as np
import skfuzzy as fuzz
from skfuzzy import control as ctrl

# Input variables
age = ctrl.Antecedent(np.arange(10, 81, 1), 'age')
bmi = ctrl.Antecedent(np.arange(10, 50, 1), 'bmi')
goal = ctrl.Antecedent(np.arange(0, 3, 1), 'goal')  # 0: Weight Loss, 1: Maintenance, 2: Muscle Gain

# Output variables
calorie_need = ctrl.Consequent(np.arange(1000, 4001, 100), 'calorie_need')
protein_level = ctrl.Consequent(np.arange(0, 101, 1), 'protein_level')

# Membership functions for age
age['young'] = fuzz.trimf(age.universe, [10, 20, 30])
age['adult'] = fuzz.trimf(age.universe, [25, 40, 55])
age['senior'] = fuzz.trimf(age.universe, [50, 65, 80])

# Membership functions for BMI
bmi['underweight'] = fuzz.trimf(bmi.universe, [10, 16, 18.5])
bmi['normal'] = fuzz.trimf(bmi.universe, [18, 22, 24.9])
bmi['overweight'] = fuzz.trimf(bmi.universe, [25, 30, 35])
bmi['obese'] = fuzz.trimf(bmi.universe, [35, 40, 50])

# Membership functions for goal
goal['loss'] = fuzz.trimf(goal.universe, [0, 0, 1])
goal['maintain'] = fuzz.trimf(goal.universe, [0, 1, 2])
goal['gain'] = fuzz.trimf(goal.universe, [1, 2, 2])

# Output membership functions
calorie_need['low'] = fuzz.trimf(calorie_need.universe, [1000, 1600, 2200])
calorie_need['moderate'] = fuzz.trimf(calorie_need.universe, [2000, 2500, 3000])
calorie_need['high'] = fuzz.trimf(calorie_need.universe, [2800, 3400, 4000])

protein_level['low'] = fuzz.trimf(protein_level.universe, [0, 30, 50])
protein_level['medium'] = fuzz.trimf(protein_level.universe, [40, 60, 80])
protein_level['high'] = fuzz.trimf(protein_level.universe, [70, 85, 100])

# Define rules
rules = [
    ctrl.Rule(goal['loss'] & bmi['overweight'], calorie_need['low']),
    ctrl.Rule(goal['gain'] & bmi['underweight'], calorie_need['high']),
    ctrl.Rule(goal['maintain'] & bmi['normal'], calorie_need['moderate']),
    ctrl.Rule(goal['loss'] & age['senior'], protein_level['medium']),
    ctrl.Rule(goal['gain'] & age['young'], protein_level['high']),
]

# Control system
calorie_ctrl = ctrl.ControlSystem(rules)
calorie_simulator = ctrl.ControlSystemSimulation(calorie_ctrl)

def get_nutrition_plan(age_val, bmi_val, goal_val):
    calorie_simulator.input['age'] = age_val
    calorie_simulator.input['bmi'] = bmi_val
    calorie_simulator.input['goal'] = goal_val
    calorie_simulator.compute()
    
    return {
        "calorie_need": calorie_simulator.output['calorie_need'],
        "protein_level": calorie_simulator.output['protein_level'],
    }
