import datetime as dt
import pandas as pd
import random
import smtplib

##################### Hard Starting Project ######################

# 1. Update the birthdays.csv with your friends & family's details. 
# HINT: Make sure one of the entries matches today's date for testing purposes. 
today = (dt.datetime.now().month, dt.datetime.now().day)

# 2. Check if today matches a birthday in the birthdays.csv
# HINT 1: Only the month and day matter. 
# HINT 2: You could create a dictionary from birthdays.csv that looks like this:
# birthdays_dict = {
#     (month, day): data_row
# }
bdays_df = pd.read_csv("birthdays.csv")
bdays_dict = {(row["month"], row["day"]) : row for (_, row) in bdays_df.iterrows()}

#HINT 3: Then you could compare and see if today's month/day matches one of the keys in birthday_dict like this:
# if (today_month, today_day) in birthdays_dict:
# 3. If step 2 is true, pick a random letter from letter templates and replace the [NAME] with the person's actual name from birthdays.csv
# HINT: https://www.w3schools.com/python/ref_string_replace.asp
# 4. Send the letter generated in step 3 to that person's email address.
# HINT: Gmail(smtp.gmail.com), Yahoo(smtp.mail.yahoo.com), Hotmail(smtp.live.com), Outlook(smtp-mail.outlook.com)
email = "my_email@gmail.com"
password = "testtesttesttest"
if today in bdays_dict:
    letter = f"letter_templates/letter_{random.randint(1,3)}.txt"
    with open(letter) as lf:
        lf_content = lf.read()
        lf_content = lf_content.replace("[NAME]", bdays_dict[today]["name"])    
    with smtplib.SMTP("stmp.gmail.com") as conn:
        conn.starttls()
        conn.login(user=email, password=password)
        conn.sendmail(
            from_addr=email,
            to_addrs=bdays_dict[today]["email"],
            msg=f"Subject:Happy Birthday!\n\n{lf_content}"
        )

