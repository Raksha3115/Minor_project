# 🔐 Password Strength Analyzer

A simple **Python-based Password Strength Analyzer** that checks the strength of a password based on multiple security criteria.

The program analyzes the password and provides a **strength rating, score, and suggestions for improvement**.

## 🚀 Features

* 🔢 Checks password length
* 🔠 Checks for uppercase letters
* 🔡 Checks for lowercase letters
* 🔢 Checks for numbers
* 🔣 Checks for special characters
* 📊 Calculates a password strength score out of 5
* 🛡️ Classifies passwords as Weak, Medium, or Strong
* 💡 Provides suggestions to improve weak passwords
* ⚠️ Handles empty password input

## 🛠️ Technologies Used

* **Python 3**
* `string` module
* Functions
* Lists
* Conditional statements
* Loops
* Built-in functions

## 📂 Project Structure

```text
PASSWORD_STRENGTH_ANALYZER/
│
├── password_strength.py
└── README.md
```

## 🧠 How It Works

The program checks the password against **five criteria**:

| Criteria              | Score |
| --------------------- | ----: |
| At least 8 characters |    +1 |
| Uppercase letter      |    +1 |
| Lowercase letter      |    +1 |
| Number                |    +1 |
| Special character     |    +1 |

The maximum score is **5**.

### Strength Classification

```text
0–2  → Weak
3–4  → Medium
5    → Strong
```

## 🔧 Main Function

### `analyze_password(password)`

This function analyzes the entered password.

It:

1. Checks the password length.
2. Checks for an uppercase character.
3. Checks for a lowercase character.
4. Checks for a digit.
5. Checks for a special character.
6. Calculates the total score.
7. Determines the password strength.
8. Generates suggestions for missing criteria.

The function returns:

```text
score
strength
suggestions
```

## 📚 Python Concepts Used

### `any()`

The program uses `any()` to check whether at least one character satisfies a condition.

Example:

```python
any(char.isupper() for char in password)
```

### `string.punctuation`

The `string` module provides a collection of punctuation characters that can be used to detect special characters.

### Functions

The password analysis logic is separated into the `analyze_password()` function, making the program easier to understand and reuse.

### Lists

A `suggestions` list stores recommendations for improving the password.

## ▶️ How to Run

### Step 1: Open the project folder

Open the project in **VS Code** or any Python-supported environment.

### Step 2: Run the Python file

```bash
python password_strength.py
```

### Step 3: Enter a password

The program will analyze the password and display its strength.

## 💻 Example

### Input

```text
Enter your password: Raksha@123
```

### Output

```text
==========================================
              ANALYSIS RESULT
==========================================
Password Length : 10
Strength        : Strong
Score           : 5 / 5
Your password has good strength!
==========================================
```

## ⚠️ Example of a Weak Password

If a password does not satisfy some criteria, the program displays suggestions such as:

```text
Suggestions:
- Use at least 8 characters.
- Add at least one uppercase letter.
- Add at least one number.
- Add at least one special character.
```

## 🎯 Project Objective

The main objective of this project is to demonstrate how **Python can be used to analyze password characteristics using simple security rules**.

This project helps understand:

* String processing
* Character checking
* Conditional logic
* Functions
* Lists
* Loops
* Input validation

## 🔮 Future Improvements

The project can be improved by adding:

* 📈 A visual strength meter
* 🔒 Detection of commonly used passwords
* 🧠 Detection of repeated characters
* ⚠️ Detection of easily guessable patterns
* 🎨 A graphical user interface
* 🌐 A web-based version
* 🔑 Secure password generator
* 📊 More detailed password analysis

## 👩‍💻 Author

**Raksha**

### 🔐 Password Strength Analyzer

*A simple Python project for analyzing password strength and providing security suggestions.*
