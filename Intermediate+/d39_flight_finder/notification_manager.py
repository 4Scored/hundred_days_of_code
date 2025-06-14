import os
from twilio.rest import Client

TWILIO_NUM = f"whatsapp:{os.environ.get("TWILIO_NUM")}"
MY_NUM = f"whatsapp:{os.environ.get("MY_NUM")}"

class NotificationManager:
    #This class is responsible for sending notifications with the deal flight details.
    
    def __init__(self):
        self.client = Client(os.environ.get('TWILIO_SID'), os.environ.get("TWILIO_AUTH_TOKEN"))

    def send_msg(self):
        message = self.client.messages.create(
            body="",
            from_=TWILIO_NUM, 
            to=MY_NUM,
        )
        print(message.sid)





