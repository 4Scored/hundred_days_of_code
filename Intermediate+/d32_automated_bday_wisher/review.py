import smtplib
import datetime as dt
import random

email = "example_email@gmail.com"
password = "imecalmxknejppql"

now = dt.datetime.now()
if now.weekday() == 0: # 0 for Monday
    with open("quotes.txt") as qf:
        quotes = qf.readlines()
        quote = random.choice(quotes)        
    
    with smtplib.SMTP("stmp.gmail.com") as conn:
        conn.starttls()
        conn.login(user=email, password=password)
        conn.sendmail(
            from_addr=email,
            to_addrs="other_example_email@yahoo.com",
            msg=f"Subject:Monday Motivational Quote!\n\n{quote}"
        )   

# ------------------------------------------ 

# email = "example_email@gmail.com"
# password = "imecalmxknejppql"

# with smtplib.SMTP("stmp.gmail.com") as conn:
#     conn.starttls()
#     conn.login(user=email, password=password)
#     conn.sendmail(
#         from_addr=email,
#         to_addrs="other_example_email@yahoo.com",
#         msg="Subject:Testing...\n\nTesting this email sending connection."
#     )

# ------------------------------------------ 

# now = dt.datetime.now()
# yr = now.year
# mo = now.month
# day_of_week = now.weekday()

# dob = dt.datetime(year=2000, month=1, day=1)
# print(dob)