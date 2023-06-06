import openai

# openai.api_key = 'MY_API_KEY'
openai.api_key = 'MY_API_KEY'

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