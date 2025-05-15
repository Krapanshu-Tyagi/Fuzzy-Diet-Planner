
# 🥗 Fuzzy Diet Planner

**Fuzzy Diet Planner** is a personalized diet recommendation system built using fuzzy logic. It provides tailored dietary suggestions based on user inputs like age, height, weight, BMI, activity level, food preferences, and optionally gender, medical conditions, and health goals.


---

## 🚀 Features

- 🧠 **Fuzzy Logic-Based Recommendations**
- 📊 **BMI Calculation & Categorization**
- 🥦 Food recommendations based on:
  - Age, Weight, Height
  - Activity Level
  - Vegetarian/Non-Vegetarian preference
  - Gender (optional)
  - Medical conditions (optional)
  - Health goals (e.g., weight loss/gain) (optional)
- 💻 **Streamlit GUI** for easy interaction
- 📁 Modular code structure for easy maintenance and scalability

---

## 📂 Folder Structure

```
Fuzzy-Diet-Planner/
│
├── data/
│   └── food_data.json                   # Food items categorized by preference
│
├── core/
│   ├── fuzzy_system.py                 # Fuzzy rules for inference and Membership Functions
│   ├── meal_planner.py                 # Data processing and meal generation                      
│   └── nutrition_engine.py             # Calculation for all required feilds (like bmi)
│
├── app.py                          # Streamlit GUI for user input and result display
│
├── requirements.txt                    # Python dependencies
└── README.md                           # Project documentation (you're here!)
```

---

## ⚙️ Setup Instructions

1. **Clone the repository**
   ```bash
   git clone https://github.com/Krapanshu-Tyagi/Fuzzy-Diet-Planner.git
   cd Fuzzy-Diet-Planner
   ```

2. **Create and activate a virtual environment**
   ```bash
   python -m venv venv
   source venv/bin/activate   # On Windows: venv\Scripts\activate
   ```

3. **Install dependencies**
   ```bash
   pip install -r requirements.txt
   ```

4. **Run the Streamlit app**
   ```bash
   streamlit run app.py
   ```

---

## 🧠 Tech Stack

- **Python**
- **Fuzzy Logic (via skfuzzy / sckitlearn)**
- **Streamlit** (for UI)
- **JSON** (data handling)

---

## 📌 Future Improvements

- Integrate nutritional databases (e.g., USDA API)
- Add support for multiple languages
- Enable export of diet plans as PDF
- Improve fuzzy rule optimization using machine learning

---

## 📜 License

This project is for academic and personal learning purposes.

---

## 👨‍💻 Author

**Krapanshu Tyagi**  
B.Tech CSE Core @ VIT-AP  
🌐 [LinkedIn](https://www.linkedin.com/in/krapanshutyagi)  
🐙 [GitHub](https://github.com/Krapanshu-Tyagi)

---

*Built with ❤️ for smarter health decisions using fuzzy intelligence.*
