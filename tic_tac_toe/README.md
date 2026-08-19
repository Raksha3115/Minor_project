# ❌⭕ Tic-Tac-Toe Game

## 📌 Project Overview

**Tic-Tac-Toe** is a simple two-player Python-based game played on a 3×3 grid. Two players take turns placing **X** and **O** on the board. The player who successfully places three of their symbols in a horizontal, vertical, or diagonal row wins the game.

This project demonstrates the use of **Python functions, lists, loops, conditional statements, input validation, and game logic**.

---

## ✨ Features

* 🎮 Two-player gameplay
* ❌ Player X and ⭕ Player O
* 🧩 3×3 game board
* 🏆 Automatic winner detection
* 🤝 Detects tie games
* ⚠️ Handles invalid inputs
* 🚫 Prevents players from selecting occupied slots
* 🔄 Automatically switches turns between players

---

## 🛠️ Technologies Used

* **Python 3**
* Lists
* Functions
* `while` loop
* `if-else` statements
* `try-except` exception handling
* Boolean logic
* User input

---

## 📂 Project Structure

```text
TIC_TAC_TOE/
│
├── tic_tac_toe.py
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
python tic_tac_toe.py
```

---

## 🎯 Game Rules

The board contains 9 positions:

```text
 1 | 2 | 3
---|---|---
 4 | 5 | 6
---|---|---
 7 | 8 | 9
```

Players select a position from **1 to 9**.

A player wins by placing three identical symbols in:

* ➡️ A horizontal row
* ⬇️ A vertical column
* ↘️ A diagonal

If all positions are filled and nobody wins, the game ends in a **tie**.

---

## 🧠 How It Works

### `print_board()`

Displays the current 3×3 game board.

### `check_winner()`

Checks all possible winning combinations:

```python
[0, 1, 2]
[3, 4, 5]
[6, 7, 8]
[0, 3, 6]
[1, 4, 7]
[2, 5, 8]
[0, 4, 8]
[2, 4, 6]
```

It uses `any()` and `all()` to determine whether a player has completed a winning combination.

### `is_board_full()`

Checks whether all nine positions are occupied by either `X` or `O`.

### `tic_tac_toe()`

This is the main function that controls the complete game:

1. Creates the board.
2. Starts with Player X.
3. Takes player input.
4. Validates the selected position.
5. Places the player's symbol.
6. Checks for a winner or tie.
7. Switches turns between X and O.

---

## 🖥️ Sample Output

```text
Welcome to Tic-Tac-Toe!

 1 | 2 | 3
---|---|---
 4 | 5 | 6
---|---|---
 7 | 8 | 9

Player X, enter a slot (1-9): 8

Player O, enter a slot (1-9): 5

Player X, enter a slot (1-9): 9

Player O, enter a slot (1-9): 1

Player X, enter a slot (1-9): 7

 O | 2 | 3
---|---|---
 4 | O | 6
---|---|---
 X | X | X

Congratulations! Player X wins!
```

---

## 🎓 Learning Objectives

This project helps in understanding:

* Python functions
* Lists and indexing
* Loops
* Conditional statements
* Input validation
* Exception handling
* Boolean expressions
* Game logic
* Modular programming

---

## 🚀 Future Improvements

The game can be enhanced by adding:

* 🤖 Player vs Computer mode
* 🏆 Score tracking
* 🔄 Replay option
* 🖥️ Graphical interface using Tkinter
* 📊 Game statistics
* 🎨 Improved user interface

---

## 👩‍💻 Author

**Raksha**

### 📌 Project

**Tic-Tac-Toe Game**

### 💻 Language

**Python**
