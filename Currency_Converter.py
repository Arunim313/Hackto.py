from flask import Flask, render_template, url_for, flash, redirect, request, jsonify
from socket import gethostbyname as ghbn, gethostname as ghn
from flask_wtf import FlaskForm
from wtforms import DateField, FloatField, SelectField, SubmitField
from wtforms.validators import DataRequired
import redis
# Imported Flask
app = Flask(__name__)
app.config['SECRET_KEY'] = 'abdallah'
# Defining ip address and port number to connect to our redis database
ip_addr = ghbn(ghn())
port_num = 6379
client = redis.Redis(host=ip_addr, port=port_num)
aed_to_usd = float(client.get('aed_to_usd').decode('utf-8'))
usd_to_aed = float(client.get('usd_to_aed').decode('utf-8'))
choice = ["USD", "AED"]
choice_edit  = ["USD_TO_AED", "AED_TO_USD"]

# Creating Flask forms to pass them to our html pages
class InputDataForms(FlaskForm):
    date = DateField("Type the Date in This Format ( yyyy-mm-dd ) ", validators=[DataRequired()])
    base = SelectField('base', choices=choice, validators=[DataRequired()])
    currency = SelectField('currency', choices=[choice[-1], choice[0]], validators=[DataRequired()])
    quantity = FloatField(f'How much would you like to convert?', validators=[DataRequired()])
    submit = SubmitField('Calculate')
    edit = SubmitField('Edit conversion rates')

class UpdateDataForms(FlaskForm):
    curr = SelectField('curr', choices=choice_edit, validators=[DataRequired()])
    value = FloatField('Change the rate', validators=[DataRequired()])
    submit = SubmitField('Apply changes')
    back = SubmitField('Go back to the main application')

# Main converting route
@app.route('/convert', methods=['GET', 'POST'])
def convert():
    global aed_to_usd, usd_to_aed
    forms = InputDataForms()
    # Starting main conversion
    if forms.validate_on_submit():
        date = forms.date.data
        base = forms.base.data
        currency = forms.currency.data
        quantity = forms.quantity.data
        if base == 'USD' and currency == 'AED':
            total = quantity * float(client.get('usd_to_aed').decode('utf-8'))
        elif base == 'AED' and currency == 'USD':
            total = quantity * float(client.get('aed_to_usd').decode('utf-8'))
        elif base == currency:
            total = quantity 
        flash("{} {} = {:.2f} {} On The Day Of {}".format(quantity, base, total, currency, date))

    return render_template('converter.html', form=forms)

# Set rate route to change the conversion rates
@app.route('/setrate', methods=['GET','POST'])
def setrate():
    global aed_to_usd, usd_to_aed
    forms = UpdateDataForms()
    if forms.validate_on_submit():
        curr = forms.curr.data 
        value = forms.value.data 
        if curr == 'USD_TO_AED':
            client.set('usd_to_aed', value)
        else: 
            client.set('aed_to_usd', value)
        flash("You have successfully updated the conversion rates in our databases.")
    return render_template('setrate.html', form=forms)

# Route for the api to convert
@app.route('/convert/<string:currency>/<amount>', methods=['GET', 'POST'])
def conversion(currency, amount):
    if currency.lower() == 'usd_to_aed':
        total = float(amount) * float(client.get('usd_to_aed').decode('utf-8'))
        total_value = 'AED'
    elif currency.lower() == 'aed_to_usd':
        total = float(amount) * float(client.get('aed_to_usd').decode('utf-8'))
        total_value = 'USD'
    end_result = {'currency': currency,
                  'amount': amount,
                  'end_result': f'{total} {total_value}'}
    return jsonify(end_result)

# Route for the api to set a new rate
@app.route('/setrate/<string:currency>/<amount>', methods=['GET', 'POST'])
def newrate(currency, amount):
    if currency.lower() == 'usd_to_aed':
        client.set('usd_to_aed', amount)
        return jsonify({'is_valid': "You have successfully updated the converstion rates in our databases.",
                        'usd_to_aed': float(client.get('usd_to_aed').decode('utf-8')),
                        'aed_to_usd': float(client.get('aed_to_usd').decode('utf-8'))})
    elif currency.lower() == 'aed_to_usd':
        client.set('aed_to_usd', amount)
        return jsonify({'is_valid': "You have successfully updated the converstion rates in our databases.",
                        'usd_to_aed': float(client.get('usd_to_aed').decode('utf-8')),
                        'aed_to_usd': float(client.get('aed_to_usd').decode('utf-8'))})

# Running the application
if __name__ == "__main__":
    app.run(debug=True)
