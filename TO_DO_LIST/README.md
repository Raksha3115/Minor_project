
# ✅ To-Do List

A simple **Python-based To-Do List application** that helps users manage their daily tasks through a menu-driven console interface.

Users can add tasks, view their tasks, mark tasks as completed, and delete tasks when they are no longer needed.

## 🚀 Features

* ➕ Add new tasks
* 📋 View all tasks
* ✅ Mark tasks as completed
* 🗑️ Delete tasks
* ⚠️ Handles invalid input
* 🔢 Uses task numbers for task management
* 🐍 Simple and beginner-friendly Python project

## 🛠️ Technologies Used

* **Python 3**
* Lists
* Dictionaries
* Functions
* Loops
* Conditional statements
* User input
* Exception handling

## 📂 Project Structure

```text
TO_DO_LIST/
│
├── todo_list.py
└── README.md
```

## 📋 Main Menu

The application provides five options:

```text
======================================
              TO-DO LIST
======================================
1. Add Task
2. View Tasks
3. Complete Task
4. Delete Task
5. Exit
======================================
```

## 🧠 How It Works

Tasks are stored inside a Python list.

Each task is represented using a dictionary containing:

* `task` — Stores the task description
* `completed` — Stores whether the task is completed or pending

Example:

```python
tasks = [
    {
        "task": "Complete Python assignment",
        "completed": False
    }
]
```

## 🔧 Functions Used

### 1. `add_task()`

Allows the user to add a new task.

The program checks whether the task is empty before adding it.

Example:

```text
Enter your task: Complete Python assignment
Task added successfully!
```

### 2. `view_tasks()`

Displays all tasks with their current status.

Tasks are shown as either:

```text
Pending
Completed
```

Example:

```text
1. Complete Python assignment - Pending
2. Prepare presentation - Completed
```

### 3. `complete_task()`

Allows the user to select a task number and mark it as completed.

The task status changes from:

```text
Pending → Completed
```

### 4. `delete_task()`

Allows the user to delete a task using its task number.

The selected task is removed from the list.

### 5. `main()`

Controls the complete application.

It continuously displays the menu using a `while` loop until the user selects **Exit**.

## 🛡️ Error Handling

The program handles several invalid situations:

* Empty task input
* Invalid menu choice
* Non-numeric task number
* Task number outside the available range
* Trying to complete a task when no tasks exist
* Trying to delete a task when no tasks exist

For example:

```text
Enter task number to complete: abc
Please enter a valid number!
```

## 💻 Example

The user can add a task:

```text
======================================
              TO-DO LIST
======================================
1. Add Task
2. View Tasks
3. Complete Task
4. Delete Task
5. Exit
======================================
Enter your choice (1-5): 1

========== ADD TASK ==========
Enter your task: Complete Python assignment
Task added successfully!
```

The user can then exit the application:

```text
Enter your choice (1-5): 5

Thank you for using To-Do List!
```

## ▶️ How to Run

### Step 1: Open the project

Open the project folder in **VS Code**, **Google Colab**, or any Python-supported environment.

### Step 2: Run the Python file

```bash
python todo_list.py
```

### Step 3: Select an option

Enter a number from **1 to 5** and follow the instructions.

## 🎯 Project Objective

The main objective of this project is to demonstrate how **Python can be used to build a simple task management application**.

This project provides practice with:

* Lists and dictionaries
* Functions
* Loops
* Conditional statements
* User input
* Exception handling
* Data manipulation

## 🔮 Future Improvements

The project can be extended by adding:

* 💾 Save tasks permanently using files
* 📅 Add due dates
* ⭐ Add task priorities
* 🔍 Add task search
* 📊 Show completed and pending task statistics
* 🔔 Add reminders
* 🖥️ Create a graphical user interface (GUI)
* 🌐 Create a web-based version
* 🗃️ Store tasks in a database

## 👩‍💻 Author

**Raksha**

### ✅ To-Do List

*A simple Python project for organizing and managing daily tasks.*
