# ✊📄✂️ Rock-Paper-Scissors Game

## 📌 Project Overview

**Rock-Paper-Scissors** is a simple Python-based game where the user plays against the computer. The computer randomly selects Rock, Paper, or Scissors, and the program determines the winner according to the game rules.

This project demonstrates the use of **Python loops, conditional statements, lists, user input, exception handling, and the `random` module**.

---

## ✨ Features

* 🎮 User vs Computer gameplay
* 🎲 Random computer choices
* 🪨 Rock, 📄 Paper, and ✂️ Scissors options
* 🏆 Automatically determines the winner
* 🤝 Detects tie situations
* ⚠️ Handles invalid user input
* 🔄 Option to play multiple rounds
* ❌ Easy exit option

---

## 🛠️ Technologies Used

* **Python 3**
* `random` module
* Lists
* `while` loops
* `if-elif-else` statements
* `try-except` exception handling
* User input

---

## 📂 Project Structure

```text
ROCK_PAPER_SCISSORS/
│
├── rock_paper_scissors.py
└── README.md
```

---

## ▶️ How to Run

### 1. Check Python installation

```bash
python --version
```

### 2. Run the program

```bash
python rock_paper_scissors.py
```

---

## 🎯 Game Rules

The game follows these rules:

```text
Rock vs Paper     → Paper wins
Rock vs Scissors  → Rock wins
Paper vs Scissors  → Scissors wins
Same choices      → Tie
```

---

## 🧠 How It Works

The program first creates a list containing the three choices:

```python
choices = ["Rock", "Paper", "Scissors"]
```

The user selects a number from **1 to 3**.

The computer randomly selects its choice using:

```python
random.randint(1, 3)
```

The program then compares the user's choice with the computer's choice and determines whether the result is:

* **User Wins**
* **Computer Wins**
* **Tie**

The `try-except` block handles invalid inputs such as letters instead of numbers.

The user can also choose whether to play another round.

---

## 🖥️ Sample Output

```text
Welcome to Rock-Paper-Scissors!

Winning Rules:
Rock vs Paper -> Paper wins
Rock vs Scissors -> Rock wins
Paper vs Scissors -> Scissors wins

Choose an option:
1 - Rock
2 - Paper
3 - Scissors

Enter your choice: 2

User choice is: Paper
Now it's Computer's Turn...
Computer choice is: Rock

Paper vs Rock
<== User Wins! ==>
```

The program then asks:

```text
Do you want to play again? (Y/N):
```

---

## 🎓 Learning Objectives

This project helps in understanding:

* Python `random` module
* Lists and indexing
* User input handling
* `while` loops
* Conditional logic
* Exception handling using `try-except`
* Input validation
* Building an interactive console application

---

## 🚀 Future Improvements

The game can be enhanced by adding:

* 📊 Score tracking
* 🏅 Best-of-3 or Best-of-5 mode
* 👥 Two-player mode
* 🖥️ GUI using Tkinter
* 📈 Game statistics
* 🎨 Better graphical interface

---

## 👩‍💻 Author

**Raksha**

### 📌 Project

**Rock-Paper-Scissors Game**

### 💻 Language

**Python**
