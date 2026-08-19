# 🐍 Python Code Explainer using Ollama API

## 📌 Project Overview

**Python Code Explainer** is a basic Python project that uses the **Ollama API** and the **Llama 3.2 model** to analyze Python code.

The user enters Python code and can choose from three options:

1. Explain the Code
2. Find Errors
3. Improve the Code

The project sends the entered code to the locally running Ollama API and displays the AI-generated result.

---

## 🚀 Features

* 📝 Enter Python code directly in the terminal
* 🤖 Explain Python code using AI
* ❌ Find possible errors in the code
* 💡 Get suggestions to improve code
* 🔄 Perform multiple operations on the same code
* 🦙 Uses the Llama 3.2 model through Ollama
* 🌐 Uses Ollama's local REST API

---

## 🛠️ Technologies Used

* **Python**
* **Ollama**
* **Llama 3.2**
* **Ollama REST API**
* **urllib.request**
* **json**

---

## 📂 Project Structure

```text
Python-Code-Explainer-Ollama-API/
│
├── app.py
└── README.md
```

---

## ⚙️ Requirements

Before running the project, make sure you have:

* Python installed
* Ollama installed
* Llama 3.2 model downloaded

Pull the model using:

```bash
ollama pull llama3.2
```

Start Ollama if it is not already running.

---

## ▶️ How to Run

### Step 1: Open the project folder

Open the project folder in VS Code or terminal.

### Step 2: Run the Python file

```bash
python app.py
```

### Step 3: Enter Python code

The program will ask you to enter Python code.

Type:

```text
END
```

when you have finished entering the code.

### Step 4: Select an option

```text
1. Explain Code
2. Find Errors
3. Improve Code
4. Exit
```

Enter your choice and the AI will generate the result.

---

## 🔌 API Used

This project uses the Ollama local API:

```text
http://localhost:11434/api/generate
```

The program sends the selected task and Python code to the API in JSON format.

Example request data:

```python
data = {
    "model": "llama3.2",
    "prompt": task[choice] + "\n" + code,
    "stream": False
}
```

---

## 🧠 How It Works

```text
User enters Python code
        ↓
Program stores the code
        ↓
User selects an operation
        ↓
Python creates API request
        ↓
Ollama receives the request
        ↓
Llama 3.2 analyzes the code
        ↓
AI response is returned
        ↓
Result is displayed in terminal
```

---

## 💻 Example

### Input

```python
x = 10
y = 20
print(x + y)
```

### Select

```text
1. Explain Code
```

### Output

The AI explains what the variables do and how the program calculates and prints their sum.

---

## 📚 Python Modules Used

### `urllib.request`

Used to send the HTTP request to the Ollama API.

### `json`

Used to convert Python data into JSON and convert the API response back into Python data.

---

## 🎯 Purpose of the Project

The main purpose of this project is to understand how a Python program can communicate with a locally running AI model through an API.

It also demonstrates basic concepts of:

* API requests
* JSON data
* User input
* AI prompts
* Local AI models
* Python programming

---

## 🔮 Future Improvements

Some possible improvements are:

* Add a graphical user interface
* Support more programming languages
* Save previous code explanations
* Add code generation
* Add syntax highlighting
* Add more code analysis options

---

## 👩‍💻 Author

**Raksha**

### Project: Python Code Explainer using Ollama API
