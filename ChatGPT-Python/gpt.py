import openai

# openai.api_key = 'MY_API_KEY'
openai.api_key = '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'

messages = [ {"role": "system", "content": "You are an intelligent assistant."} ]

while True:
    query = input("User : ")
    if query:
        messages.append(
            {"role": "user", "content": query},
        )
        chat = openai.ChatCompletion.create(
            model="gpt-3.5-turbo", messages = messages
        )
    reply = chat.choices[0].message.content
    print(f"ChatGPT: {reply}")
    messages.append({"role": "assistant", "content": reply})