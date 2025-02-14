import json



# Dummy DB Json files
def load_messages():
    # with open('json/messages.json', 'r') as file:
    #     return json.load(file)
    return {
        "BYPASS": "BYPASS",
        "BYPASS_OFF": "BYPASS OFF",
        
    }

def save_messages(messages):
    with open('json/messages.json', 'w') as file:
        json.dump(messages, file)
    
def load_bus_data():
    with open('json/bus_data.json', 'r') as file:
        return json.load(file)

def load_messages_sent():
    with open('json/messages_sent.json', 'r') as file:
        return json.load(file)
        # return list(data.values())
    
def save_messages_sent(messages_sent):
    with open('json/messages_sent.json', 'w') as file:
        json.dump(messages_sent, file)