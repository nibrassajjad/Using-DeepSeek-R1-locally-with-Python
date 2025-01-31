import openai

# Use LM Studio's local API
openai.api_base = "http://localhost:1234/v1"  # Check your LM Studio API port
openai.api_key = "lm-studio"  # No real API key needed for local use

def prompt_sentence(sentence):
    prompt = f"{sentence}"
    response = openai.ChatCompletion.create(
        model="deepseek-r1-distill-qwen-7b.gguf",  # Change to your LM Studio model
        messages=[
            {"role": "system", "content": "You are an AI trained to respond to user."},
            {"role": "user", "content": prompt}
        ],
        temperature=0
    )

    return response["choices"][0]["message"]["content"].strip()

# User Input
# Keep running until user decides to quit
while True:
    sentence = input("\nAsk or say anything (or type 'exit' to quit): ")
    if sentence.lower() == 'exit':
        print("Exiting program. Goodbye!")
        break
    output = prompt_sentence(sentence)
    print(f"{output}")
