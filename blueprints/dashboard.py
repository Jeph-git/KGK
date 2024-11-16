from flask import Blueprint, render_template, request, redirect, url_for, flash, jsonify, session
from utils import load_messages, load_bus_data, load_messages_sent
from forms import ChooseBus, ChooseMessage


dashboard = Blueprint('dashboard', __name__)

@dashboard.route('/dashboard', methods=['GET', 'POST'])
def dashboard_home():
    choose_bus_form = ChooseBus()
    select_message_form = ChooseMessage()
    # On POST request, process the form submission
    if request.method == 'POST':
        if choose_bus_form.validate_on_submit():
            selected_company = choose_bus_form.company.data
            session['selected_company'] = selected_company
            print('Selected company from form:', selected_company)
        else:
            print(f'Selected session company: {session.get("selected_company")}')
            selected_company = session.get('selected_company')

        # Process the message selection
        if select_message_form.validate_on_submit():
            selected_message = select_message_form.message.data
            # Process the selected message, for example, save it to the session or send it to an API
            print(f"Selected message: {selected_message}")
            # You can store the selected message in the session or redirect to a new page as needed
            flash(f"Message '{selected_message}' selected!", 'success')
            
    else:
        # On GET request, default to 'Unibuss' or use the selected company from session
        selected_company = session.get('selected_company', 'Unibuss')
        print(selected_company)

    choose_bus_form.company.data = selected_company
    #Load messages
    messages_dict = load_messages()

    # Load the bus data based on selected company
    bus_data = load_bus_data()
    selected_buses = bus_data['buses'][0].get(selected_company, [])
    
    # Count the number of buses for each company
    num_of_buses = {}
    for company, buses in bus_data['buses'][0].items():
        num_of_buses[company] = len(buses)
    total_buses = sum(num_of_buses.values())
    
    # Count the number of messages sent
    messages_sent = load_messages_sent()
    messages = load_messages()
    num_of_messages = len(messages)

    return render_template('dashboard.html', 
                           active='dashboard', 
                           num_of_messages=num_of_messages, 
                           total_buses=total_buses,
                           messages_sent=messages_sent,
                           company=selected_company,
                           buses=selected_buses,
                           choose_bus_form=choose_bus_form, 
                           select_message_form=select_message_form,
                           messages_dict=messages_dict)
