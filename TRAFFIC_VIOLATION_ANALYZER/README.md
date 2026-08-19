# 🚦 Traffic Violation Analyzer

A **Python-based Traffic Violation Analyzer** that manages traffic violation records and provides useful analysis based on vehicles, locations, violation types, fines, and high-risk cases.

The project is a **menu-driven console application** designed as a Python minor project. It allows users to add, search, analyze, and manage traffic violation data.

## 🚀 Features

* 📋 Display all traffic violations
* ➕ Add new violation records
* 🔎 Search violations by vehicle number
* 📊 Analyze violation statistics
* 📍 Perform location-based analysis
* ⚠️ Identify high-risk violations
* 🚗 Analyze frequently violating vehicles
* 📈 Display an overall dashboard
* 💰 Calculate total and average fines
* 📅 Validate violation dates
* ❌ Handle invalid menu choices and inputs

## 🛠️ Technologies Used

* **Python 3**
* `datetime` module
* Lists
* Dictionaries
* Sets
* Loops
* Conditional statements
* Functions
* `lambda`
* String methods
* Basic data analysis

## 📂 Project Structure

```text
TRAFFIC_VIOLATION_ANALYZER/
│
├── traffic_violation_analyzer.py
└── README.md
```

## 🧠 How It Works

The project stores traffic violation records in a **list of dictionaries**.

Each record contains:

* Vehicle number
* Location
* Violation type
* Date
* Fine

Example:

```python
{
    "vehicle": "DL01AB1234",
    "location": "Delhi",
    "violation": "No Helmet",
    "date": "01-08-2026",
    "fine": 1000
}
```

The program uses separate functions for different operations and provides all functions through a main menu.

## 📋 Main Menu

The application provides the following options:

```text
1. Display All Violations
2. Add New Violation
3. Search Vehicle
4. Violation Statistics
5. Location Analysis
6. High-Risk Analysis
7. Vehicle Analysis
8. Dashboard
9. Exit
```

## 🔍 Main Functionalities

### 1. Display All Violations

Displays every stored traffic violation with:

* Vehicle number
* Location
* Violation
* Date
* Fine

### 2. Add New Violation

The user can add a new traffic violation by entering:

```text
Vehicle Number
Location
Violation Type
Date
```

Available violation types include:

* No Helmet
* No Seat Belt
* Overspeeding
* Red Light Jump
* Drunk Driving
* Wrong Parking

The program automatically assigns the corresponding fine.

### 3. Search Vehicle

The user can enter a vehicle number and view all violations associated with that vehicle.

It also calculates:

* Total number of violations
* Total fine

### 4. Violation Statistics

This feature calculates:

* Frequency of each violation
* Most common violation
* Total violations
* Total fine collected

### 5. Location Analysis

The program counts violations according to location and identifies the location having the highest number of violations.

Example locations:

```text
Delhi
Noida
Gurugram
```

### 6. High-Risk Analysis

The program identifies high-risk violations such as:

* Drunk Driving
* Red Light Jump
* Overspeeding

These records are displayed separately for easier analysis.

### 7. Vehicle Analysis

The program counts how many violations are associated with each vehicle.

It then sorts the vehicles based on the number of violations and identifies the most frequently violating vehicle.

### 8. Dashboard

The dashboard provides a quick summary of the complete dataset:

```text
Total Violations
Unique Vehicles
Total Fine
High-Risk Cases
Average Fine
```

## 💰 Fine Structure

| Violation      |    Fine |
| -------------- | ------: |
| No Helmet      |  ₹1,000 |
| No Seat Belt   |  ₹1,000 |
| Overspeeding   |  ₹2,000 |
| Red Light Jump |  ₹5,000 |
| Drunk Driving  | ₹10,000 |
| Wrong Parking  |    ₹500 |

## 📅 Date Validation

The project uses Python's `datetime` module to validate dates in:

```text
DD-MM-YYYY
```

If the user leaves the date empty, the program automatically uses the current date.

## 📊 Example Dashboard

For the sample data, the dashboard can provide information such as:

```text
🚦 TRAFFIC VIOLATION DASHBOARD
======================================================================

📊 SUMMARY
--------------------------------------------------
Total Violations : 8
Unique Vehicles  : 8
Total Fine       : ₹ 31000
High-Risk Cases  : 5
Average Fine     : ₹ 3875.0

======================================================================
```

## ▶️ How to Run

### Step 1: Open the project

Open the project in **VS Code**, **Google Colab**, or another Python-supported environment.

### Step 2: Run the Python file

```bash
python traffic_violation_analyzer.py
```

### Step 3: Select an option

For example:

```text
Enter your choice (1-9): 8
```

The dashboard will display the overall traffic violation summary.

## 🎯 Project Objective

The main objective of this project is to demonstrate how **Python can be used to manage and analyze structured traffic violation data**.

This project provides practical understanding of:

* Data structures
* Functions
* Lists and dictionaries
* Searching
* Sorting
* Data aggregation
* Date validation
* Sets
* Conditional logic
* Menu-driven applications
* Basic data analysis

## 🔮 Future Improvements

The project can be extended by adding:

* 💾 Save records permanently using CSV/JSON
* 📊 Graphs and charts using Matplotlib
* 🗄️ Database integration using SQLite
* 🌐 Web-based interface
* 📈 Monthly and yearly trend analysis
* 🚨 Automatic high-risk alerts
* 🔐 Admin login system
* 📍 Map-based location visualization
* 📑 Generate violation reports

## 👩‍💻 Author

**Raksha**

### 🚦 Traffic Violation Analyzer

*A Python-based application for managing, searching, and analyzing traffic violation data.*
