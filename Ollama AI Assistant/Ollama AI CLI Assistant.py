import ollama

def chat_with_ollama():
    print("=== Ollama AI Assistant ===")
    print("Type 'exit' or 'quit' to stop.\n")

    history = [
        {"role": "system", "content": "You are a helpful and concise assistant."}
    ]

    while True:
        user_input = input("You: ")

        # Exit condition
        if user_input.lower() in ["exit", "quit"]:
            print("Goodbye!")
            break

        # Empty input check
        if not user_input.strip():
            continue

        # Add user message to history
        history.append({"role": "user", "content": user_input})

        print("\nAI: ", end="", flush=True)

        # Call Ollama API with streaming
        response = ollama.chat(
            model="llama3.2",
            messages=history,
            stream=True
        )

        full_reply = ""
        for chunk in response:
            text = chunk["message"]["content"]
            print(text, end="", flush=True)
            full_reply += text

        print("\n")

        # Save AI reply to history
        history.append({"role": "assistant", "content": full_reply})

if __name__ == "__main__":
    chat_with_ollama() 
