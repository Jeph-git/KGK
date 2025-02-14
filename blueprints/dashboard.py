from flask import Blueprint, render_template, request, redirect, url_for, flash, jsonify, session
from utils import load_messages, load_bus_data, load_messages_sent, save_messages_sent
from forms import ChooseCompany, ChooseMessage, ChooseMessageForChange
import requests


dashboard = Blueprint('dashboard', __name__)
@dashboard.route('/dashboard', methods=['GET', 'POST'])
def dashboard_home():
    choose_company_form = ChooseCompany()
    select_message_form = ChooseMessage()
    select_message_for_change = ChooseMessageForChange()

    if request.method == 'POST':
        # Handle message submission
        if 'submit_select_message' in request.form and select_message_form.validate_on_submit():
            selected_message_key = select_message_form.message.data  # Get the message key
            phone_number = select_message_form.phone_number.data

            # Load messages to get the value corresponding to the selected key
            messages_dict = load_messages()
            selected_message_value = messages_dict.get(selected_message_key, "Unknown Message")

            # Construct the link
            # link = f'https://nabohund.no/kgk/kgk.php?input={{"avsender": "{phone_number}","device": "+352602141532861","message": "{selected_message_key}"}}'
            
            flash({'header': 'Melding sendt!', 'body': f'{selected_message_value} ble sendt til nummer: {phone_number}'}, 'success')

            messages_sent = load_messages_sent()
            messages_sent['messages_sent'] += 1
            save_messages_sent(messages_sent)

            # Flash success message
            # flash({'header': 'Melding sendt!', 'body': f'{selected_message_value} ble sendt til {phone_number}'}, 'success')

        # Handle message change
        elif 'submit_change_message' in request.form and select_message_for_change.validate_on_submit():
            selected_message = select_message_for_change.message.data
            print(f"Selected message for change: {selected_message}")
            flash(f"{selected_message} ble endret", 'success')

        # Handle company selection
        elif choose_company_form.validate_on_submit():
            selected_company = choose_company_form.company.data
            session['selected_company'] = selected_company
            print('Selected company from form:', selected_company)

    # Load selected company from session or default to 'Unibuss'
    selected_company = session.get('selected_company', 'Unibuss')
    choose_company_form.company.data = selected_company

    # Load data for rendering
    bus_data = load_bus_data()
    selected_buses = bus_data['buses'][0].get(selected_company, [])
    num_of_buses = {company: len(buses) for company, buses in bus_data['buses'][0].items()}
    total_buses = sum(num_of_buses.values())
    messages_sent = load_messages_sent()
    messages_dict = load_messages()
    num_of_messages = len(messages_dict)

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