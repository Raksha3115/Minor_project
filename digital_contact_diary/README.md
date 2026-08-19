# 📱 Digital Contact Diary

## 📌 Project Overview

**Digital Contact Diary** is a simple Python-based contact management system. It allows users to store and manage contact details such as **name, phone number, and email address** through a menu-driven interface.

The project demonstrates the use of **Python dictionaries, functions, loops, conditional statements, and user input**.

---

## ✨ Features

* ➕ Add a new contact
* 👀 View all saved contacts
* 🔍 Search for a contact by name
* ✏️ Update contact details
* 🗑️ Delete a contact
* ❌ Exit the application
* ⚠️ Handles invalid menu choices
* ✅ Prevents empty contact names

---

## 🛠️ Technologies Used

* **Python 3**
* Python Dictionaries
* Python Functions
* `while` loop
* `if-elif-else` statements
* User Input

---

## 📂 Project Structure

```text
DIGITAL_CONTACT_DIARY/
│
├── contact_diary.py
└── README.md
```

---

## ▶️ How to Run

### 1. Make sure Python is installed

Check Python using:

```bash
python --version
```

### 2. Run the program

```bash
python contact_diary.py
```

The Digital Contact Diary menu will appear in the terminal.

---

## 🖥️ Menu Options

```text
1. Add Contact
2. View Contacts
3. Search Contact
4. Update Contact
5. Delete Contact
6. Exit
```

### 1. Add Contact

The user enters:

* Contact name
* Phone number
* Email address

The information is stored in a Python dictionary.

### 2. View Contacts

Displays all contacts currently stored in the program.

### 3. Search Contact

Searches for a contact using the contact name.

### 4. Update Contact

Allows the user to change the phone number and email of an existing contact.

### 5. Delete Contact

Removes an existing contact from the contact diary.

### 6. Exit

Closes the program.

---

## 🧠 How It Works

The project uses a dictionary named `contacts` to store contact information.

Each contact is stored in this structure:

```python
contacts[name] = {
    "phone": phone,
    "email": email
}
```

The program uses separate functions for each operation:

```text
add_contact()
      ↓
view_contacts()
      ↓
search_contact()
      ↓
update_contact()
      ↓
delete_contact()
      ↓
main()
```

The `main()` function displays the menu and calls the appropriate function according to the user's choice.

---

## 🧪 Sample Output

```text
======================================
         DIGITAL CONTACT DIARY
======================================
1. Add Contact
2. View Contacts
3. Search Contact
4. Update Contact
5. Delete Contact
6. Exit
======================================

Enter your choice (1-6): 1
Enter contact name: Anand Kumar Sahu
Enter phone number: 8810609109
Enter email: example@gmail.com

Contact added successfully!
```

For an invalid choice:

```text
Enter your choice (1-6): 7

Invalid choice! Please enter a number from 1 to 6.
```

To exit:

```text
Enter your choice (1-6): 6

Thank you for using Digital Contact Diary!
```

---

## 🎯 Learning Objectives

This project helps in understanding:

* Python dictionaries
* Functions and modular programming
* Loops and conditional statements
* CRUD operations
* User input handling
* Basic data management
* Menu-driven Python applications

---

## 🚀 Future Improvements

The project can be enhanced by adding:

* 💾 File-based data storage
* 🔐 Password protection
* 📞 Contact validation
* 📧 Email validation
* 🔤 Sorting contacts alphabetically
* 🖥️ Graphical User Interface (GUI)
* 🗄️ Database support

---

## 👩‍💻 Author

**Raksha**

### 📌 Project

**Digital Contact Diary**

### 💻 Language

**Python**
