# 🤖 AI Study Assistant using Ollama

## 📌 Project Overview

**AI Study Assistant** is a simple Python project that uses the **Ollama Chat API** and the **Llama 3.2 model** to help students understand different topics.

The user enters a topic, and the AI generates:

* Definition
* Important Points
* Simple Example
* Practice Questions

The project is designed using basic Python concepts and demonstrates how an AI language model can be integrated into a Python application.

---

## 🎯 Objective

The main objective of this project is to learn:

* How to integrate Ollama with Python
* How to use the Ollama Chat API
* How to create effective prompts
* How to take input from a user
* How to send input to an AI model
* How to receive and display an AI-generated response

---

## 🛠️ Technologies Used

* **Python**
* **Ollama**
* **Llama 3.2**
* **Ollama Chat API**

---

## 📂 Project Structure

```text
AI-Study-Assistant/
│
├── app.py
├── requirements.txt
└── README.md
```

---

## ⚙️ Requirements

Before running the project, install:

### 1. Python

Make sure Python is installed on your computer.

### 2. Ollama

Install Ollama on your system.

### 3. Install Python Ollama package

```bash
pip install ollama
```

### 4. Download Llama 3.2

```bash
ollama pull llama3.2
```

Make sure the Ollama service is running before executing the Python program.

---

## ▶️ How to Run

Run the Python file using:

```bash
python app.py
```

The program will display:

```text
===== AI STUDY ASSISTANT =====

Enter a topic to study:
```

Enter any topic you want to learn.

---

## 💡 Example

### Input

```text
Enter a topic to study: Python Functions
```

### Output

```text
===== STUDY NOTES =====

1. Definition
A function is a reusable block of code designed to perform a specific task.

2. Important Points
- Functions help reduce code repetition.
- Functions can accept parameters.
- Functions can return values.

3. Simple Example
def add(a, b):
    return a + b

4. Practice Questions
1. What is a function?
2. Why are functions used?
3. What is a parameter?
```

---

## 🔄 How the Project Works

```text
User enters a topic
        ↓
Python receives the input
        ↓
Prompt is created
        ↓
Ollama Chat API
        ↓
Llama 3.2 Model
        ↓
AI generates study material
        ↓
Python receives the response
        ↓
Study notes are displayed
```

---

## 🧩 Main Function

The project contains one main function:

```python
def study_assistant(topic):
```

This function:

1. Takes the topic from the user.
2. Creates a prompt with specific instructions.
3. Sends the prompt to the Llama 3.2 model using Ollama.
4. Receives the AI-generated response.
5. Returns the study material.

---

## 📡 API Used

This project uses the **Ollama Chat API** through the Python `ollama` library.

The API is called using:

```python
ollama.chat()
```

The AI model used in this project is:

```text
Llama 3.2
```

---

## 🌟 Features

* Simple and beginner-friendly
* Uses AI to generate study material
* Provides structured learning content
* Generates practice questions
* Uses a locally running AI model through Ollama
* Built using basic Python

---

## 🚀 Future Improvements

The project can be enhanced by adding:

* Multiple-choice quiz generation
* Difficulty levels such as Easy, Medium and Hard
* Different languages
* PDF or document-based learning
* Save notes to a file
* Interactive quiz mode
* Graphical User Interface

---

## 🎓 Learning Outcome

Through this project, I learned how to connect a Python program with an AI language model using the Ollama Chat API.

The main learning objective is **AI and API integration**, while the study assistant is the practical use case.

---

## 👩‍💻 Author

**Raksha**

---

## 📄 License

This project is created for educational and learning purposes.
