```markdown
# 🦙 Ollama AI CLI Assistant

A lightweight, interactive Command-Line Interface (CLI) chat assistant built with Python that connects to local large language models using the **Ollama API**.

---

## 📌 Features

- **100% Offline & Private:** Runs entirely on local hardware with zero data shared with third-party cloud services.
- **Real-Time Token Streaming:** Renders model responses incrementally in the terminal.
- **Context-Aware Memory:** Maintains multi-turn conversation history during the active session.
- **Zero API Costs:** Uses local, open-source models with no subscription or token fees.

---

## 🛠️ Tech Stack

- **Language:** Python 3.10+
- **Inference Engine:** [Ollama](https://ollama.com/)
- **Default Model:** `llama3.2`
- **Library:** `ollama`

---

## 🚀 Getting Started

### 1. Prerequisites

1. Download and install Ollama from [ollama.com](https://ollama.com/download).
2. Pull the default model:
   ```bash
   ollama pull llama3.2

```

### 2. Installation

1. Clone the repository:
```bash
git clone [https://github.com/YOUR_USERNAME/YOUR_REPOSITORY_NAME.git](https://github.com/YOUR_USERNAME/YOUR_REPOSITORY_NAME.git)
cd YOUR_REPOSITORY_NAME

```


2. Install the required Python package:
```bash
pip install ollama

```



---

## 💻 Usage

Run the assistant script:

```bash
python app.py

```

* Type your prompt and press **Enter** to chat.
* Type `exit` or `quit` to terminate the session.

---

## 📂 Project Structure

```text
├── app.py              # Main Python CLI script
├── requirements.txt    # Project dependencies
└── README.md           # Documentation

```

---

## ⚙️ How It Works

1. **System Prompt Initialization:** Defines the assistant's behavior and personality in the `history` list.
2. **Context Persistence:** Every user query and assistant response is appended to `history` to maintain context for multi-turn chats.
3. **Streaming Inference:** Communicates with the local Ollama daemon (`http://127.0.0.1:11434`) using `ollama.chat(..., stream=True)` to stream generated tokens with minimal latency.

---

## 📄 License

This project is licensed under the MIT License - see the `LICENSE` file for details.

```

```
