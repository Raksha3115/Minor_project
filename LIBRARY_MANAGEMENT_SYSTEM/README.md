# 📚 Library Management System

A simple **Python-based Library Management System** that allows users to manage books through a menu-driven console application.

The system provides basic library operations such as **adding, viewing, searching, issuing, returning, and deleting books**.

## 🚀 Features

* ➕ Add new books
* 📖 View all available books
* 🔍 Search books by title
* 📕 Issue a book
* 🔄 Return an issued book
* 🗑️ Delete books
* ⚠️ Handles invalid input
* 🔢 Automatically generates a new Book ID
* 🐍 Uses basic Python concepts

## 🛠️ Technologies Used

* **Python 3**
* Dictionaries
* Functions
* Loops
* Conditional statements
* User input
* Exception handling

## 📂 Project Structure

```text
LIBRARY_MANAGEMENT_SYSTEM/
│
├── library_management.py
└── README.md
```

## 📋 Main Menu

The application provides the following options:

```text
========================================
       LIBRARY MANAGEMENT SYSTEM
========================================
1. Add Book
2. View All Books
3. Search Book
4. Issue Book
5. Return Book
6. Delete Book
7. Exit
========================================
```

## 🧠 How the Project Works

The project stores book information in a Python dictionary.

Each book contains:

* **Book ID**
* **Title**
* **Author**
* **Status**

Example:

```python
books = {
    1: {
        "title": "Python Programming",
        "author": "John Smith",
        "status": "Available"
    }
}
```

The status of a book can be:

```text
Available
Issued
```

## 🔧 Functions Used

### 1. `add_book()`

Adds a new book to the library.

The user enters:

* Book title
* Author name

A new Book ID is automatically generated.

### 2. `view_books()`

Displays all books along with their:

* Book ID
* Title
* Author
* Status

### 3. `search_book()`

Allows the user to search for a book using its title.

The search is **case-insensitive** and can also match part of a title.

### 4. `issue_book()`

Issues a book using its Book ID.

The program checks:

* Whether the Book ID exists
* Whether the book is already issued

If everything is valid, the status changes to:

```text
Available → Issued
```

### 5. `return_book()`

Returns an issued book.

The status changes from:

```text
Issued → Available
```

### 6. `delete_book()`

Deletes a book using its Book ID.

An issued book cannot be deleted.

### 7. `main()`

Controls the complete menu-driven application and continuously displays the menu until the user selects **Exit**.

## ▶️ How to Run

### Step 1: Open the project

Open the project folder in **VS Code** or any Python-supported environment.

### Step 2: Run the Python file

```bash
python library_management.py
```

### Step 3: Select an option

Enter a number from **1 to 7** according to the operation you want to perform.

## 💻 Example

### Issue Book

If the user enters:

```text
Enter Book ID: machine learning
```

the program detects that the input is not a valid number and displays:

```text
Please enter a valid number!
```

The program then returns to the main menu.

### Add Book

The user can add a new book:

```text
========== ADD BOOK ==========
Enter book title: Python Programming
Enter author name: John Smith
Book added successfully!
Book ID: 4
```

## 🛡️ Error Handling

The project handles several invalid situations:

* Empty book title or author
* Invalid Book ID input
* Book ID not found
* Already issued book
* Returning a book that is already available
* Attempting to delete an issued book
* Invalid menu choice

## 🎯 Project Objective

The main objective of this project is to demonstrate how **Python dictionaries and functions can be used to create a practical management system**.

It provides hands-on practice with:

* Data storage using dictionaries
* CRUD operations
* Functions
* Loops
* Conditional logic
* Input validation
* Exception handling

## 🔮 Future Improvements

The project can be extended by adding:

* 👤 Student/member management
* 📅 Issue and return dates
* ⏰ Due-date tracking
* 💰 Fine calculation
* 💾 File or database storage
* 🔐 User login system
* 📊 Library statistics
* 🖥️ Graphical User Interface (GUI)

## 👩‍💻 Author

**Raksha**

### 📚 Library Management System

*A simple Python project for managing books and basic library operations.*
