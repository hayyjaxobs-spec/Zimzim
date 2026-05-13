from flask import Flask, request
from twilio.twiml.messaging_response import MessagingResponse

app = Flask(__name__)

@app.route('/sms', methods=['POST'])
def sms():
    resp = MessagingResponse()
    resp.message("Hello from Zimzim SMS API!")
    return str(resp)

if __name__ == '__main__':
    app.run(debug=True)