import json
from flask import Flask, render_template, request, flash, redirect, url_for
from forms import OptionForm

from blueprints.all_choices import all_choices
from blueprints.web_settings import web_setting
from blueprints.dashboard import dashboard

from utils import load_messages

app = Flask(__name__)
app.config['SECRET_KEY'] = 'your_secret_key'

app.register_blueprint(all_choices)
app.register_blueprint(web_setting)
app.register_blueprint(dashboard)

@app.route('/', methods=['GET', 'POST'])
def home():
    form = OptionForm()
    messages_dict = load_messages()  # Load the messages from JSON
    
    if request.method == 'POST':
        selected_groups = form.groups.data
        message_type = request.form.get('message')  # message1, message2, etc.
        
        if message_type and selected_groups:
            messages = []
            for group in selected_groups:
                messages.append(group)
                print(f"{group} got {messages_dict.get(message_type, 'unknown message')}")  # For server logs
            # flash_message = ', '.join(messages)
            if len(messages) == 1:
                flash_message = messages[0]
            else:
                flash_message = ", ".join(messages[:-1]) +" & "+messages[-1]

            # Flash the message that corresponds to the message type
            flash(f'{flash_message} fikk {messages_dict.get(message_type, "unknown message")}', 'success')
        else:
            flash('Velg en gruppe.', 'warning')

        return redirect(url_for('home'))  # Redirect to avoid resubmission

    # Pass the messages to the template
    return render_template('index.html', form=form, messages_dict=messages_dict, active='home')

if __name__ == '__main__':
    # app.run(debug=True, host= '192.168.10.222') # This one for running on local network
    app.run(debug=True, use_reloader=True) 
