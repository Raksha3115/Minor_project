# AI Text Summarizer using Ollama

## 📌 Project Overview

AI Text Summarizer is a simple Python project that uses the **Ollama Chat API** and the **Llama 3.2 model** to summarize user-provided text.

The user enters a paragraph or any text, and the program sends it to the AI model through Ollama. The model generates a summary in **6–7 simple sentences**, which is then displayed on the screen.

## 🎯 Objective

The main objective of this project is to learn how to:

* Use Python with an AI model
* Integrate the Ollama API into a Python program
* Create and send prompts to an AI model
* Take input from the user
* Receive and process an AI-generated response
* Display the generated summary

## 🛠️ Technologies Used

* **Python**
* **Ollama**
* **Llama 3.2**
* **Ollama Chat API**

## 📂 Project Structure

```text
AI-Text-Summarizer/
│
├── app.py
├── requirements.txt
└── README.md
```

## ⚙️ Requirements

Before running the project, make sure you have:

1. Python installed
2. Ollama installed
3. Llama 3.2 model installed
4. Python Ollama package installed

Install the Python package using:

```bash
pip install ollama
```

Download the Llama 3.2 model:

```bash
ollama pull llama3.2
```

## ▶️ How to Run

Start Ollama and make sure the Ollama service is running.

Then run the Python program:

```bash
python app.py
```

The program will ask:

```text
===== AI TEXT SUMMARIZER =====

Enter your text:
```

Enter your text and the AI will generate a summary.

## 💡 Example

### Input

```text
Python is a high-level programming language known for its simple
and readable syntax. It is widely used in web development, data
science, artificial intelligence, automation and many other fields.
Python has a large number of libraries and frameworks that make
development easier.
```

### Output

```text
Summary:

Python is a high-level programming language with simple syntax.
It is widely used in web development and data science.
Python is also popular in artificial intelligence and automation.
Its readability makes it easy to learn and use.
Python provides many useful libraries and frameworks.
These features make Python a popular programming language.
```

## 🔄 How the Project Works

```text
User enters text
       ↓
Python receives input
       ↓
Prompt is created
       ↓
Ollama Chat API
       ↓
Llama 3.2 Model
       ↓
AI generates summary
       ↓
Python receives response
       ↓
Summary displayed
```

## 🧩 Main Function

The project contains one main function:

```python
def summarize_text(text):
```

This function:

1. Creates a prompt.
2. Sends the prompt to the Llama 3.2 model using Ollama.
3. Receives the AI response.
4. Extracts the generated text.
5. Returns the summary.

## 📡 API Used

This project uses the **Ollama Chat API** through the Python `ollama` library.

The code uses:

```python
ollama.chat()
```

The model used is:

```text
llama3.2
```

## 🚀 Future Improvements

The project can be improved by adding:

* Different summary lengths
* Multiple languages
* File upload for summarization
* PDF and document summarization
* A simple graphical user interface
* Option to save summaries into a file

## 👩‍💻 Author

**Raksha**

## 📄 License

This project is created for educational and learning purposes.
