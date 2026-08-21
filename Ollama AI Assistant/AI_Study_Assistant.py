import ollama


def study_assistant(topic):
    prompt = f"""
You are a helpful study assistant.

Explain the following topic in simple language.

Topic: {topic}

Give the answer in this format:
1. Definition
2. Important Points
3. Simple Example
4. Practice Questions

Keep the explanation easy for a student to understand.
"""

    response = ollama.chat(
        model="llama3.2",
        messages=[
            {
                "role": "user",
                "content": prompt
            }
        ]
    )

    return response["message"]["content"]


print("===== AI STUDY ASSISTANT =====")

topic = input("\nEnter a topic to study: ")

result = study_assistant(topic)

print("\n===== STUDY NOTES =====")
print(result)
