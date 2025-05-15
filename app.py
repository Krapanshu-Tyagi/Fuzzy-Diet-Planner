# app.py
import streamlit as st
from core.nutrition_engine import get_personalized_nutrition
from core.meal_planner import generate_meal_plan

st.set_page_config(page_title="Fuzzy Diet Planner", layout="centered")

st.title("🥗 Personalized Diet Planner")
st.write("Powered by Fuzzy Logic & Soft Computing")

# 1. Collect inputs
with st.form("user_input"):
    col1, col2 = st.columns(2)
    age = col1.number_input("Age", 10, 80, 25)
    gender = col2.selectbox("Gender", ["Male", "Female"])
    
    height = col1.number_input("Height (cm)", 100, 250, 170)
    weight = col2.number_input("Weight (kg)", 30, 200, 65)
    
    goal = st.selectbox("Goal", ["Weight Loss", "Maintain", "Muscle Gain"])
    activity = st.selectbox("Activity Level", ["Sedentary", "Light", "Moderate", "Active", "Very Active"])
    
    dietary = st.multiselect("Dietary Preferences", ["vegetarian", "vegan", "gluten-free", "high-protein"])
    restrictions = st.multiselect("Restrictions", ["lactose", "gluten", "nuts"])
    
    submitted = st.form_submit_button("Generate Diet Plan")

# 2. Run core engine
if submitted:
    goal_map = {"Weight Loss": 0, "Maintain": 1, "Muscle Gain": 2}
    plan = get_personalized_nutrition(age, height, weight, gender, goal_map[goal], activity)
    
    st.subheader("🧠 Fuzzy Output Summary")
    st.write(f"**BMI:** {plan['bmi']} | **BMR:** {plan['bmr']} | **TDEE:** {plan['tdee']}")
    st.write(f"**Fuzzy Recommended Calories:** {plan['fuzzy_calories']} kcal")
    st.write(f"**Fuzzy Recommended Protein:** {plan['fuzzy_protein']} g")
    
    # 3. Create meal plan
    st.subheader("📅 7-Day Personalized Meal Plan")
    meal_plan = generate_meal_plan(
        calorie_target=plan["fuzzy_calories"],
        protein_target=plan["fuzzy_protein"],
        dietary_tags=dietary,
        excluded_tags=restrictions
    )
    
    for day, details in meal_plan.items():
        with st.expander(day):
            meals = details["meals"]
            for meal_type in ["breakfast", "lunch", "dinner", "snack"]:
                item = meals.get(meal_type)
                if isinstance(item, list):
                    for snack in item:
                        st.write(f"🥜 {meal_type.title()}: {snack['name']} ({snack['calories']} kcal, {snack['protein']}g protein)")
                elif item:
                    st.write(f"🍽️ {meal_type.title()}: {item['name']} ({item['calories']} kcal, {item['protein']}g protein)")
            st.write(f"**Total Calories:** {details['totals']['calories']} kcal | **Protein:** {details['totals']['protein']}g")

