import smtplib
import os

EMAIL = os.environ.get("MyTestGmailAddress")
PASSWORD = os.environ.get("MyTestGmailPassword")

def send_email(form):
    msg = f"Subject:New Message\n\nName: {form['name']}\nEmail: {form['email']}\nPhone: {form['phone']}\nMessage: {form['message']}"
    with smtplib.SMTP("smtp.gmail.com", port=587) as connection:
        connection.starttls()
        connection.login(EMAIL, PASSWORD)
        connection.sendmail(EMAIL, "maximus27rus@gmail.com", msg=msg)