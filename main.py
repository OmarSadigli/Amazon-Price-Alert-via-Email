import requests
import lxml
from bs4 import BeautifulSoup
import smtplib

my_email = "EMAIL"
password = "PASSWORD"
URL = "PRODUCT_LINK"

headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:86.0) Gecko/20100101 Firefox/86.0",
    "Accept-Language": "en-US,en;q=0.5"
}

response = requests.get(URL, headers=headers)

soup = BeautifulSoup(response.text, "lxml")

price = soup.find("span", class_="a-size-base a-color-price").get_text()
price_without_currency = price.split("$")[1]
price_as_float = float(price_without_currency)
print(price)

product_name = soup.find(id="productTitle").get_text().strip()
print(product_name)

if price_as_float < 105:
    with smtplib.SMTP("smtp.gmail.com", port=587) as connection:
        connection.starttls()
        connection.login(user=my_email, password=password)
        connection.sendmail(
            from_addr=my_email,
            to_addrs="RECIEVER_EMAIL",
            msg=(f"Subject: Amazon Price Alert!\n\n{product_name} is now {price}").encode("utf-8")
        )