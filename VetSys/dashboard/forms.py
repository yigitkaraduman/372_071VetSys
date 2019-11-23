from flask_wtf import FlaskForm
#from VetSys.users.models import Staff
from wtforms import StringField, PasswordField, SubmitField, IntegerField, RadioField, DecimalField
from wtforms.fields.html5 import DateField, TimeField
from wtforms.validators import DataRequired, Email, Optional


class OwnerCreationForm(FlaskForm):
    name = StringField('Name:', validators=[DataRequired()])
    last_name = StringField('Last Name:', validators=[DataRequired()])
    sex = RadioField('Sex:', choices=['Man', 'Woman'])
    phone = IntegerField('Phone:', validators=[DataRequired()])
    ssn = IntegerField('ID Number:', validators=[DataRequired()])
    email = StringField('Email', validators=[Email()])
    address = StringField('Address:')
    phone = IntegerField('Phone:')
    submit_button = SubmitField('Register an Owner')


class AppointmentCreationForm(FlaskForm):
    on = DateField('Date:')
    hour = TimeField('Time:')
    appointment_type = RadioField(
        'Type:', choices=[('r1', 'For once'), ('r2', 'Periodic')])
    period = StringField('Period:')
    owner_ssn = StringField('Owner SSN:')
    submit_button = SubmitField('Create')


class PetCreationForm(FlaskForm):
    pet_name = StringField('Name:')
    age = IntegerField('Age:')
    weight = IntegerField('Weight:')
    race = StringField('Race: ')
    species = StringField('Species:')
    disabilities = StringField('Disabilities:')
    owner_ssn = StringField('Owner SSN:', validators=[DataRequired()])
    submit_button = SubmitField('Create')


class TreatmentCreationForm(FlaskForm):
    treatment_type = StringField('Treatment Type:')
    start_date = DateField('Start Date:')
    end_date = DateField('End Date:')
    pet_name = StringField('Pet Name:')
    submit_button = SubmitField('Create')

class InvoiceCreationForm(FlaskForm):
    quantity = IntegerField('Quantity:')
    transaction_date = DateField('Invoice Date:')
    service_name = StringField('Service name:') #burasi dropdown box gibi bisi olacak aslinda ama duzelticem onu -cagatay
    # bi de nasil yapacaksam multiple selection olacak
    service_quantity = IntegerField('Service quantity:')
    owner_ssn = IntegerField('Owner SSN:')
    submit_button = SubmitField('Create')

class ServiceCreationForm(FlaskForm):
    name = StringField('Service name:')
    cost = DecimalField('Cost: ')
    submit_button = SubmitField('Create')


