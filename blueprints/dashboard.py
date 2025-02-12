from flask import Blueprint, render_template, request, redirect, url_for, flash, jsonify, session
from utils import load_messages, load_bus_data, load_messages_sent, save_messages_sent
from forms import ChooseCompany, ChooseMessage, ChooseMessageForChange


dashboard = Blueprint('dashboard', __name__)

@dashboard.route('/dashboard', methods=['GET', 'POST'])
def dashboard_home():
    choose_company_form = ChooseCompany()
    select_message_form = ChooseMessage()
    select_message_for_change = ChooseMessageForChange()

    if request.method == 'POST':
        # Determine which form was submitted
        if 'submit_select_message' in request.form and select_message_form.validate_on_submit():
            selected_message = select_message_form.message.data
            messages_sent = load_messages_sent()
            messages_sent['messages_sent'] += 1
            save_messages_sent(messages_sent)
            # print(f'Messages sent: {messages_sent[0]}')
            

            print(f"Selected message: {selected_message}")
            # flash(f"{selected_message} ble sendt", 'success')
            flash({'header': 'Melding sendt!', 'body': f'{selected_message} ble sendt'}, 'success')

        elif 'submit_change_message' in request.form and select_message_for_change.validate_on_submit():
            selected_message = select_message_for_change.message.data
            print(f"Selected message for change: {selected_message}")
            flash(f"{selected_message} ble endret", 'success')

        elif choose_company_form.validate_on_submit():
            selected_company = choose_company_form.company.data
            session['selected_company'] = selected_company
            print('Selected company from form:', selected_company)

    selected_company = session.get('selected_company', 'Unibuss')
    choose_company_form.company.data = selected_company
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
                           choose_company_form=choose_company_form, 
                           select_message_form=select_message_form,
                           messages_dict=messages_dict,
                           select_message_for_change=select_message_for_change
                           )
