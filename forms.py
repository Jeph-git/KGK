from flask_wtf import FlaskForm
from wtforms import SelectMultipleField
from wtforms import StringField
from wtforms.validators import DataRequired
class OptionForm(FlaskForm):
    groups = SelectMultipleField(
        'Choose groups', 
        choices=[('Oslobuss', 'Oslobuss'), ('Unibuss', 'Unibuss'), ('Ruter', 'Ruter')],
    )

class MessageForm(FlaskForm):
    message = StringField('Message', validators=[DataRequired()])