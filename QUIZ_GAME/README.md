
# 🎯 Quiz Game

A simple **Python-based Quiz Game** that tests the user's general knowledge and basic computer knowledge through multiple-choice questions.

The program asks the player to answer **10 questions** using options **A, B, C, or D**, calculates the score, and displays the final percentage and result.

## 🚀 Features

* 👤 Takes the player's name
* ❓ Contains 10 multiple-choice questions
* 🔤 Accepts answers using A, B, C, or D
* ✅ Checks answers automatically
* 📊 Calculates the final score
* 📈 Calculates percentage
* 🏆 Displays performance based on percentage
* ⚠️ Handles invalid answers
* 🎉 Provides a final result message

## 🛠️ Technologies Used

* **Python 3**
* Lists
* Dictionaries
* `for` loops
* `while` loops
* Conditional statements
* User input
* String methods
* Basic arithmetic

## 📂 Project Structure

```text
QUIZ_GAME/
│
├── quiz_game.py
└── README.md
```

## 🧠 How It Works

The questions are stored in a **list of dictionaries**.

Each question contains:

* Question
* Four options
* Correct answer

Example:

```python
{
    "question": "What is the capital of India?",
    "options": [
        "A. Mumbai",
        "B. New Delhi",
        "C. Kolkata",
        "D. Chennai"
    ],
    "answer": "B"
}
```

The program goes through each question using a `for` loop and asks the player to enter an answer.

## 🎮 Game Flow

### 1. Enter Player Name

The program first asks:

```text
Enter your name:
```

If the user does not enter a name, the program uses **Player** as the default name.

### 2. Answer Questions

Each question provides four options:

```text
A
B
C
D
```

The user's input is converted to uppercase so that both lowercase and uppercase answers work.

For example:

```text
b
B
```

are treated as the same answer.

### 3. Answer Validation

The program only accepts:

```text
A, B, C, D
```

If the user enters something else, the program displays:

```text
Invalid answer! Please enter A, B, C, or D.
```

and asks again.

### 4. Score Calculation

For every correct answer:

```python
score += 1
```

At the end, the program calculates:

```python
percentage = (score / total_questions) * 100
```

## 🏆 Result Classification

The final result is based on the percentage:

|   Percentage | Result                       |
| -----------: | ---------------------------- |
| 80% or above | Excellent! 🎉                |
|    60% – 79% | Very Good! 👍                |
|    40% – 59% | Good! Keep practicing.       |
|    Below 40% | Keep learning and try again! |

## 💻 Example Output

For example, if a player answers **9 out of 10 questions correctly**:

```text
==============================================
                QUIZ RESULT
==============================================
Player: Raksha
Total Questions: 10
Correct Answers: 9
Wrong Answers: 1
Score: 9 / 10
Percentage: 90.0 %
Result: Excellent! 🎉
==============================================
          Thank you for playing!
==============================================
```

## 📚 Topics Covered in the Quiz

The questions cover basic topics such as:

* 🇮🇳 General knowledge
* 🐍 Python
* 💻 Computer fundamentals
* 🌍 Geography
* 🔢 Mathematics
* 🖥️ Computer hardware
* 🧠 Basic programming concepts

## ▶️ How to Run

### Step 1: Open the project

Open the project folder in **VS Code**, **Google Colab**, or any Python-supported environment.

### Step 2: Run the Python file

```bash
python quiz_game.py
```

### Step 3: Enter your name

```text
Enter your name: Raksha
```

### Step 4: Answer the questions

Enter **A, B, C, or D** for each question.

## 🎯 Project Objective

The main objective of this project is to demonstrate how **Python can be used to create an interactive quiz application**.

This project provides practice with:

* Data structures
* Dictionaries
* Lists
* Loops
* Conditional statements
* Input validation
* String manipulation
* Score calculation
* Basic program flow

## 🔮 Future Improvements

The project can be improved by adding:

* 🔄 Replay option
* 📚 Multiple quiz categories
* 🎚️ Difficulty levels
* ⏱️ Timer for each question
* 🏅 High-score system
* 🎲 Randomized questions
* 📊 Detailed performance report
* 🖥️ Graphical User Interface (GUI)
* 💾 Save scores to a file

## 👩‍💻 Author

**Raksha**

### 🎯 Quiz Game

*A simple Python-based multiple-choice quiz application for learning and testing knowledge.*
