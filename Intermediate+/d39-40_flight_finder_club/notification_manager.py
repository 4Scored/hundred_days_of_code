import os
from twilio.rest import Client
import smtplib

TWILIO_NUM = f"whatsapp:{os.environ.get("TWILIO_NUM")}"
MY_NUM = f"whatsapp:{os.environ.get("MY_NUM")}"
SMTP_ADDR = os.environ.get("SMTP_ADDRESS")
EMAIL = "xyz@gmail.com"
EMAIL_PASS = os.environ.get("EMAIL_ADDR_PASS")

class NotificationManager:
    #This class is responsible for sending notifications with the deal flight details.
    
    def __init__(self):
        self.client = Client(os.environ.get('TWILIO_SID'), os.environ.get("TWILIO_AUTH_TOKEN"))        
        self.connection = smtplib.SMTP(SMTP_ADDR)

    def send_msg(self, msg_body):
        message = self.client.messages.create(            
            from_=TWILIO_NUM, 
            to=MY_NUM,
            body=msg_body,
        )
        print(message.sid)

    def send_emails(self, email_list, email_body):
        with self.connection as conn:
            conn.starttls()
            conn.login(EMAIL, EMAIL_PASS)
            for to_email in email_list:
                self.connection.sendmail(
                    from_addr=EMAIL,
                    to_addrs=to_email,
                    email_body=f"Subject:Lower Prices on Flight!\n\n{email_body}"
                )




