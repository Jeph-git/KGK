import json

def load_messages():
    with open('messages.json', 'r') as file:
        return json.load(file)