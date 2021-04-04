import smtplib
import os


email_notifier = "physical.taco@yahoo.com"
password = os.environ.get("EMAIL_KEY")
host = "smtp.mail.yahoo.com"


def send_email(text):

    with smtplib.SMTP(host, port=587) as connection:
        connection.starttls()                                           # Make the connection secure
        connection.login(user=email_notifier, password=password)
        connection.sendmail(
            from_addr=email_notifier,
            to_addrs='physical.taco@gmail.com',
            msg=text
        )
