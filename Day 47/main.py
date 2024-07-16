import os
import smtplib

from dotenv import load_dotenv
from bs4 import BeautifulSoup
import requests

# URL = "https://appbrewery.github.io/instant_pot/"
URL = "https://www.amazon.com/dp/B075CYMYK6?psc=1&ref_=cm_sw_r_cp_ud_ct_FM9M699VKHTT47YD50Q6"
header = {
    "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_5) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/84.0.4147.125 Safari/537.36",
    "Accept-Language": "en-US;"
}
response = requests.get(URL,headers=header)
website_html = response.text
soup = BeautifulSoup(website_html, "html.parser")

# Get product price
priceWhole = soup.find(name='span',class_ = 'a-price-whole').getText().strip()
priceFraction=soup.find(name='span',class_ = 'a-price-fraction').getText().strip()
priceTotal = float(priceWhole) + (float(priceFraction)/100)


# Get the product title
title = soup.find(id="productTitle").get_text().strip()

# Set the price below which you would like to get a notification
BUY_PRICE = 70
if priceTotal < BUY_PRICE:
    message = f"{title} is on sale for {priceTotal}!"

SMTP_ADDRESS="smtp.gmail.com"
EMAIL_ADDRESS="in stick"
EMAIL_PASSWORD="in stick"

with smtplib.SMTP("smtp.gmail.com", port=587) as connection:
    connection.starttls()
    result = connection.login(EMAIL_ADDRESS, EMAIL_PASSWORD)
    connection.sendmail(
        from_addr=EMAIL_ADDRESS,
        to_addrs=EMAIL_ADDRESS,
        msg=f"Subject:Amazon Price Alert!\n\n{message}\n{URL}".encode("utf-8")
    )


