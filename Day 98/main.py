import requests
import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart

# Configuration
API_KEY = ''
CITY = 'Nagoya'
COUNTRY_CODE = 'JP'
EMAIL = ''
PASSWORD = ''
TO_EMAIL = ''
SMTP_SERVER = 'smtp.gmail.com'
SMTP_PORT = 587


def get_weather():
    url = f'http://api.openweathermap.org/data/2.5/weather?q={CITY},{COUNTRY_CODE}&appid={API_KEY}&units=metric'
    response = requests.get(url)
    data = response.json()
    if response.status_code == 200:
        weather = data['weather'][0]['description']
        temp = data['main']['temp']
        return f"Weather in {CITY}: {weather}, Temperature: {temp}°C"
    else:
        return "Failed to retrieve weather data"


def send_email(weather_report):
    msg = MIMEMultipart()
    msg['From'] = EMAIL
    msg['To'] = TO_EMAIL
    msg['Subject'] = f'Daily Weather Report for {CITY}'

    msg.attach(MIMEText(weather_report, 'plain'))

    try:
        with smtplib.SMTP("smtp.gmail.com", port=587) as connection:
            connection.starttls()
            result = connection.login(EMAIL, PASSWORD)
            connection.sendmail(
                from_addr=EMAIL,
                to_addrs=EMAIL,
                msg=f'{msg.as_string()}'.encode(
                    "utf-8")
            )
        print("Email sent successfully!")
    except Exception as e:
        print(f"Failed to send email: {e}")


if __name__ == "__main__":
    weather_report = get_weather()
    send_email(weather_report)
