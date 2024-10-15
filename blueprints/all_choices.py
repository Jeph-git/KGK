from flask import Blueprint, render_template, request, flash, redirect, url_for
import json

all_choices = Blueprint('more', __name__)

# Function to load the messages from JSON
def load_messages():
    with open('messages.json', 'r') as file:
        return json.load(file)

def format_buses(buses):
    n = len(buses)
    if n > 1:
        return ('{}, '*(n-2) + '{} og {}').format(*buses)
    elif n > 0:
        return buses[0]
    else:
        return ''


# Route to display the groups and their subgroups (buses)
@all_choices.route('/more', methods=['GET', 'POST'])
def choices_func():
    bus_data = {
        'Unibuss': ['Bus 1', 'Bus 2', 'Bus 3', 'Bus 4', 'Bus 5'],
        'Oslobuss': ['Bus A', 'Bus B', 'Bus C', 'Bus D', 'Bus E']
    }
    
    messages = load_messages()  # Load messages from JSON

    if request.method == 'POST':
        selected_buses = request.form.getlist('buses')  # Get the selected buses
        selected_message = request.form.get('message')  # Get the selected message


        
        if selected_buses and selected_message:
            # flash(f'Sendte "{selected_message}" til {", ".join(selected_buses)}', 'success')
            flash(f'Sendte "{selected_message}" til {format_buses(selected_buses)}', 'success')
        else:
            flash('Vennligst velg minst en buss.', 'danger')

        return redirect(url_for('more.choices_func'))

    return render_template('more.html', bus_data=bus_data, messages=messages)
