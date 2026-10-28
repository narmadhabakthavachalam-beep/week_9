import ollama
import csv
import os
from datetime import datetime

os.makedirs("dataset", exist_ok=True)

history = []

print("Welcome to Education Chatbot!")
print("Type 'exit' to stop the chatbot.")

while True:
    user_input = input("You: ")

    if user_input.lower() == "exit":
        print("Chatbot: Goodbye!")
        break

    history.append({
        "role": "user",
        "content": user_input
    })

    response = ollama.chat(
        model="llama3.2",
        messages=[
            {
                "role": "system",
                "content": "You are a helpful education chatbot. Explain topics in simple English."
            }
        ] + history
    )

    bot_reply = response["message"]["content"]

    print("Chatbot:", bot_reply)

    history.append({
        "role": "assistant",
        "content": bot_reply
    })

    file_exists = os.path.exists("dataset/chat_history.csv")

    with open("dataset/chat_history.csv", "a", newline="", encoding="utf-8") as file:
        writer = csv.writer(file)

        if not file_exists:
            writer.writerow(["Timestamp", "User_Question", "Chatbot_Response"])

        writer.writerow([
            datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
            user_input,
            bot_reply
        ])


import ollama
import csv
import os
from datetime import datetime

os.makedirs("dataset", exist_ok=True)

history = []

print("Welcome to Education Chatbot!")
print("Type 'exit' to stop the chatbot.")

while True:
    user_input = input("You: ")

    if user_input.lower() == "exit":
        print("Chatbot: Goodbye!")
        break

    history.append({
        "role": "user",
        "content": user_input
    })

    response = ollama.chat(
        model="llama3.2",
        messages=[
            {
                "role": "system",
                "content": "You are an education chatbot. Explain topics in simple English."
            }
        ] + history
    )

    bot_reply = response["message"]["content"]
    timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

    print("Chatbot:", bot_reply)

    history.append({
        "role": "assistant",
        "content": bot_reply
    })

    for filename in ["chat_history.csv", "responses.csv"]:
        file_path = os.path.join("dataset", filename)
        file_exists = os.path.exists(file_path)

        with open(file_path, "a", newline="", encoding="utf-8") as file:
            writer = csv.writer(file)

            if not file_exists or os.path.getsize(file_path) == 0:
                writer.writerow([
                    "Timestamp",
                    "User_Question",
                    "Chatbot_Response"
                ])

            writer.writerow([timestamp, user_input, bot_reply])

print("Conversation saved successfully!")
