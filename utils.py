import json



# Dummy DB Json files
def load_messages():
    with open('json/messages.json', 'r') as file:
        return json.load(file)

def save_messages(messages):
    with open('json/messages.json', 'w') as file:
        json.dump(messages, file)
    
def load_bus_data():
    with open('json/bus_data.json', 'r') as file:
        return json.load(file)

def load_messages_sent():
    with open('json/messages_sent.json', 'r') as file:
        data = json.load(file)
        return list(data.values())