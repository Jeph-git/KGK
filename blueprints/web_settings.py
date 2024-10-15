from flask import Blueprint, render_template, request, redirect, url_for, flash, jsonify
import json
from forms import MessageForm
web_setting = Blueprint('settings', __name__)

# Function to load messages from a JSON file
def load_messages():
    with open('messages.json', 'r') as file:
        messages = json.load(file)
    return messages

# Function to save messages to a JSON file
def save_messages(messages):
    with open('messages.json', 'w') as file:
        json.dump(messages, file)

@web_setting.route('/settings', methods=['GET', 'POST'])
def settings():
    form = MessageForm()
    
    if request.method == 'POST':
        if form.validate_on_submit():
            message_type = request.form.get('modal_message_type')
            message_content = form.message.data
            
            if message_type:
                messages = load_messages()
                messages[message_type] = message_content
                save_messages(messages)
                flash('Message saved successfully.', 'success')
            else:
                flash('Failed to save message. Invalid message type.', 'danger')
        else:
            flash('Failed to save message. Form validation failed.', 'danger')
        
        return redirect(url_for('settings.settings'))
    
    # For GET request, just render the page with the form
    return render_template('web_setting.html', form=form)