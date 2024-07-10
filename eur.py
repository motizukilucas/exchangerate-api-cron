import requests
import os
import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from dotenv import load_dotenv
from datetime import datetime

# Load environment variables from .env file
load_dotenv()

# Get the API key and Gmail credentials from environment variables
api_key = os.getenv('API_KEY')
gmail_user = os.getenv('GMAIL_USER')
gmail_pass = os.getenv('GMAIL_PASS')

# URL for the GET request
url = f"https://v6.exchangerate-api.com/v6/{api_key}/pair/EUR/BRL"

# Making the GET request
response = requests.get(url)

# Checking the status code of the response
if response.status_code == 200:
    # If the response is successful, parse the JSON data
    data = response.json()
    conversion_rate = data.get('conversion_rate', 0)

    # Print the conversion rate
    current_time = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
    print(f"[{current_time}] Conversion Rate: {conversion_rate}")

    # If the conversion rate is below 5.7, send an email
    if conversion_rate < 5.7:
        # Create the email content
        subject = "Conversion Rate Alert"
        body = f"The conversion rate from EUR to BRL is below 5.7. Current rate: {conversion_rate}"
        msg = MIMEMultipart()
        msg['From'] = gmail_user
        msg['To'] = gmail_user
        msg['Subject'] = subject
        msg.attach(MIMEText(body, 'plain'))

        # Send the email
        try:
            server = smtplib.SMTP('smtp.gmail.com', 587)
            server.starttls()
            server.login(gmail_user, gmail_pass)
            text = msg.as_string()
            server.sendmail(gmail_user, gmail_user, text)
            server.quit()
            print("Email sent successfully.")
        except Exception as e:
            print(f"Failed to send email. Error: {e}")
else:
    # If the response is not successful, print the status code
    print(f"Failed to retrieve data. HTTP Status code: {response.status_code}")

