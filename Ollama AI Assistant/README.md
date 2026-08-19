# 🦙 Ollama AI CLI Assistant

A lightweight, interactive Command-Line Interface (CLI) chat assistant built with Python and powered by local open-source Large Language Models via the **Ollama API**.

---

## 📌 Features

- **100% Local & Private:** Runs entirely on your local machine without sending data to external third-party cloud APIs.
- **Real-Time Token Streaming:** Words are rendered incrementally on the terminal as they are generated.
- **Context-Aware Memory:** Maintains multi-turn conversation history within the session.
- **Zero API Costs:** Leverages free, open-weight models (e.g., LLaMA-3.2).

---

## 🛠️ Tech Stack

- **Language:** Python 3.10+
- **Inference Engine:** [Ollama](https://ollama.com/)
- **Model:** `llama3.2`
- **Library:** `ollama-python`

---

## 🚀 Getting Started

### 1. Prerequisites

Ensure you have Ollama installed and running on your system:
- Download and install Ollama from [ollama.com](https://ollama.com/download).
- Pull the target model in your terminal:
  ```bash
  ollama pull llama3.2
