
# 🍔 Food Mood Recommendation System

A simple **Python-based food recommendation system** that suggests food items according to the user's **mood, food preference, and budget**.

The project is completely menu-driven and helps users find suitable food from a predefined list of food items.

## 🚀 Features

* 😊 Takes the user's current mood
* 🥗 Supports Veg and Non-Veg preferences
* 💰 Filters food according to the user's maximum budget
* 🍕 Provides personalized food recommendations
* 📋 Allows users to view all available food items
* ⚠️ Handles invalid menu choices and invalid budget input
* 🐍 Built using basic Python concepts

## 🧠 How It Works

The user first gets a menu with three options:

```text
1. Get Food Recommendation
2. View All Food Items
3. Exit
```

If the user selects **Get Food Recommendation**, the program asks for:

1. **Mood** — happy, sad, hungry, excited, relaxed, or bored
2. **Food Type** — Veg or Non-Veg
3. **Maximum Budget**

The program then checks every food item and recommends only those that satisfy **all three conditions**.

### Recommendation Logic

A food item is recommended when:

```text
Mood matches
       AND
Food type matches
       AND
Price is within budget
```

## 🍽️ Available Food Items

| Food                 | Price | Type    | Cuisine      |
| -------------------- | ----: | ------- | ------------ |
| Cheese Pizza         |  ₹250 | Veg     | Italian      |
| Chicken Biryani      |  ₹220 | Non-Veg | Indian       |
| Paneer Butter Masala |  ₹200 | Veg     | Indian       |
| Chocolate Cake       |  ₹180 | Veg     | Dessert      |
| French Fries         |  ₹120 | Veg     | Fast Food    |
| Veg Burger           |  ₹150 | Veg     | Fast Food    |
| Ice Cream            |  ₹100 | Veg     | Dessert      |
| Masala Dosa          |  ₹140 | Veg     | South Indian |
| Pasta                |  ₹190 | Veg     | Italian      |
| Chicken Roll         |  ₹160 | Non-Veg | Fast Food    |

## 🛠️ Technologies Used

* **Python 3**
* Lists
* Dictionaries
* Functions
* Loops
* Conditional statements
* User input
* Exception handling

## 📚 Python Concepts Used

### 1. List of Dictionaries

Food information is stored using a list containing dictionaries.

```python
foods = [
    {
        "name": "Cheese Pizza",
        "price": 250,
        "type": "Veg",
        "cuisine": "Italian"
    }
]
```

### 2. Functions

The project is divided into separate functions:

* `display_food()` — displays food details
* `recommend_food()` — finds suitable food
* `view_all_food()` — displays all food items
* `main()` — controls the main menu

### 3. Conditional Filtering

The program checks:

```python
mood_match
type_match
budget_match
```

Only food satisfying all conditions is added to the recommendation list.

### 4. Exception Handling

The program uses `try-except` to handle invalid budget input.

```python
try:
    budget = float(input("Enter your maximum budget (₹): "))
except ValueError:
    print("Please enter a valid budget!")
```

## ▶️ How to Run

### Step 1: Open the project folder

Open the project in **VS Code**, **Google Colab**, or any Python-supported environment.

### Step 2: Run the Python file

```bash
python food_mood.py
```

### Step 3: Select an option

```text
Enter your choice (1-3):
```

Then follow the instructions displayed by the program.

## 💡 Example

Suppose the user enters:

```text
Mood: bored
Food Type: Veg
Budget: ₹150
```

The program recommends:

```text
French Fries — ₹120
Veg Burger — ₹150
```

because both items match the user's mood, are Veg, and are within the ₹150 budget.

## 🎯 Project Objective

The main objective of this project is to demonstrate how **Python can be used to build a simple rule-based recommendation system**.

It combines multiple user preferences and filters a dataset to provide personalized results.

## 🌟 Future Improvements

The project can be extended by adding:

* ⭐ Food ratings
* 🔍 Search functionality
* 📊 Popular food recommendations
* 🧾 Order and bill generation
* 📍 Restaurant/location-based recommendations
* 🗃️ Database integration
* 🤖 AI-based food recommendations
* 🖥️ Graphical User Interface (GUI)

## 📂 Project Structure

```text
FOOD_MOOD_RECOMMENDATION/
│
├── food_mood.py
└── README.md
```

## 👩‍💻 Author

**Raksha Sahu**

### 🍴 Food Mood Recommendation System

*A simple Python project that recommends food based on mood, preference, and budget.*
