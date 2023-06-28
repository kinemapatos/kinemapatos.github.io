from flask import Flask, render_template, request

app = Flask(__name__)
valid_ticket_codes = ['Z4xtOGXj2Bbt', 'Bzg7CO4d4BcT', 'UK5NuHS5fAAC', 'LbL6zToJknwy', 'a5RGuzNcg0PA', 'FICGyCOklIAi', 'VI6wOJrbBWyz', 'kOLoVcrMjgP4', '8JQofAo1AWbM', '2tLKSp6QvkOo', 'nAs4tf0xD8Hu', 'QruGwmT6THGw', 'qw8ysCpQfhGw', 'q7DGlqZlEmsX', 'BelSAh6kBuyW', 'kuXIHvE6XnQz', 'qMfWALTkwfRW', 'RsKRJR6vSBk2', 'dtmKU1j6Qx8V', 'OjaWGNPNoYYx', 'vPeRPpXeWFm8', 'qIHYbu0SMAEQ', 'QNG6svU2qlgw', 'C2hKjS1iZBm0', 'GCp7fYWBElsf', 'lNgNPhgDe5RK', 'uB76QqDUqiVg', 'wP3RUfDTqHaA', '9AlcQym8Mtz2', '7iY3sCMgaus5', '7pOgVip7yPMr', 'jjNgafvdGvL6', 'G9lcmzybNSgP', '7mY46fRiI9D8', 'qRQG1NNG8yea', 'xL3msfd3c33m', 'E7ljQllsFFja', '01XjvPLCQ9TZ', 'oBcF98Z9PY3T', 'RA7k6rsLbv3z']

def verify_ticket(ticket_code):

    if ticket_code.startswith('A'):
        return True
    else:
        return False

@app.route('/')
def home():
    return render_template('index.html')

def verify_ticket(ticket_code):
    if ticket_code in valid_ticket_codes:
        return "Numri i biletes eshte i sakte!"
    else:
        return "Numri i biletes eshte i pasakte!"

@app.route('/verifikim', methods=['POST'])
def verify():
    ticket_code = request.form['ticket_code']
    message = verify_ticket(ticket_code)
    return render_template('verify.html', message=message)

if __name__ == '__main__':
    app.run()