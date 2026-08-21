import ollama

def summarize_text(text):
    prompt = f"""
    Summarize the following text in 2-3 simple sentences:

    {text}
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


print("===== AI TEXT SUMMARIZER =====")

text = input("\nEnter your text: ")

summary = summarize_text(text)

print("\nSummary:")
print(summary)
