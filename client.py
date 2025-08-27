import requests
import json

# Replace with your actual API Gateway endpoint
API_URL = "https://hr6vzc0lxb.execute-api.us-east-1.amazonaws.com/prod/chat"

def chat_with_bot(message: str):
    """
    Sends a message to the chatbot API and returns the reply.
    """
    headers = {"Content-Type": "application/json"}
    payload = {"message": message}

    response = requests.post(API_URL, headers=headers, data=json.dumps(payload))

    if response.status_code == 200:
        data = response.json()
        return data.get("reply", "No reply from bot.")
    else:
        return f"Error: {response.status_code}, {response.text}"

if __name__ == "__main__":
    print("ChatBot is ready! Type 'exit' or 'quit' to stop.\n")
    while True:
        user_input = input("You: ")
        if user_input.lower() in ["exit", "quit"]:
            print("Bye! 👋")
            break
        bot_reply = chat_with_bot(user_input)
        print("Bot:", bot_reply)
