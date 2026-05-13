from flask import Flask, request
from twilio.twiml.messaging_response import MessagingResponse
import os

app = Flask(__name__)

@app.route('/sms', methods=['POST'])
def sms():
    to_number = request.form.get('To')
    from_number = request.form.get('From')
    body = request.form.get('Body')
    
    log_message = f"Received SMS from {from_number} to {to_number}: {body}"
    print(log_message)
    
    # Save to file
    with open('sms_codes.txt', 'a') as f:
        f.write(log_message + '\n')
    
    if to_number == '+12487522561':
        resp = MessagingResponse()
        resp.message("OK")
        return str(resp)
    else:
        return 'OK'  # Ignore SMS to other numbers

if __name__ == '__main__':
    app.run(debug=True)