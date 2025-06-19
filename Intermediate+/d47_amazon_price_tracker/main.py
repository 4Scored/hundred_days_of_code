import os
import smtplib
import requests
from bs4 import BeautifulSoup

PRACTICE_URL= "https://appbrewery.github.io/instant_pot/"
LIVE_URL = "https://www.amazon.com/dp/B075CYMYK6?ref_=cm_sw_r_cp_ud_ct_FM9M699VKHTT47YD50Q6"

THRESHOLD = 100.00 # threshold for price notification

header = {
    "User-Agent": "YOUR-USER-AGENT-HEADER",
    "Accept-Language": "en-GB,en-US;q=0.9,en;q=0.8"
}

prac_response = requests.get(LIVE_URL, headers=header)
prac_response.raise_for_status()
prac_content = prac_response.content

soup = BeautifulSoup(prac_content, "html.parser")

price_dollar = soup.find(name="span", class_="a-price-whole").getText()
price_cents = soup.find(name="span", class_="a-price-fraction").getText()
price = float(f"{price_dollar}{price_cents}")

title = soup.find(name="span", class_="product-title-word-break").getText()

# print(price)
# print(title)

if price < THRESHOLD:
    message = f"Subject:Amazon Price Alert!\n\n{title} is on sale for ${price}!\n{LIVE_URL}".encode("utf-8")
    with smtplib.SMTP(os.environ.get("SMTP_ADDRESS"), port=587) as conn:
        conn.starttls()
        res = conn.login(os.environ.get("EMAIL_ADDRESS"), os.environ.get("EMAIL_PASSWORD"))
        conn.sendmail(
            from_addr=os.environ.get("EMAIL_ADDRESS"),
            to_addrs=os.environ.get("EMAIL_ADDRESS"),
            msg=message
        )