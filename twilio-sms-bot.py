from main import generate_email
import dotenv
import os
from flask import Flask, request
from twilio.twiml.messaging_response import MessagingResponse

dotenv.load_dotenv(".env")

API_TOKEN = os.getenv("TOKEN")

app = Flask(__name__)

@app.route("/bot", methods=[ "POST"])
def bot():
    incoming_msg = request.values.get('Body', '').lower()

    resp = MessagingResponse()
    msg = resp.message()
    responded = False

    if "!formal" in incoming_msg:
        prompt = incoming_msg.replace("!formal", "")
        response: str = generate_email(prompt, API_TOKEN)
        msg.body(response)
        responded = True
    
    if not responded:
        msg.body("I only know how to respond to !formal")
    
    return str(resp)

if __name__ == '__main__':
    app.run()