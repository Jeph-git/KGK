from flask_wtf import FlaskForm
from wtforms import SelectMultipleField
from wtforms import StringField
from wtforms import SelectField
from wtforms.validators import DataRequired
import json
from utils import load_bus_data, load_messages



class OptionForm(FlaskForm):
    groups = SelectMultipleField(
        'Choose groups', 
        choices=[('Oslobuss', 'Oslobuss'), ('Unibuss', 'Unibuss'), ('Ruter', 'Ruter')],
    )

class MessageForm(FlaskForm):
    message = StringField('Message', validators=[DataRequired()])


class ChooseMessage(FlaskForm):
    messages = load_messages()
    message = SelectField(
        'Choose message',
        choices=[(key, value) for key, value in messages.items()], 
    )
    phone_number = StringField('Phone Number', validators=[DataRequired()])

    
class ChooseMessageForChange(FlaskForm):
    messages = load_messages()
    message = SelectField(
        'Choose message',
        choices=[(value, value) for value in messages.values()],
    )

class ChooseCompany(FlaskForm):
    bus_data = load_bus_data()
    companies = list(bus_data['company'])
    company = SelectField(
        'Velg selskap',
        choices=[(company, company) for company in companies],
    )