# ==========================================
# Program : Simple Gmail Mail Sender
# Author : Atharva Dhamale
# Purpose : Send mail using Python SMTP
# ==========================================

import smtplib
from email.message import EmailMessage

# -------------------------------------------------
# Function : Marvellous_send_mail
# Description : Sends email using Gmail SMTP server
# -------------------------------------------------

def send_mail(sender, app_password, receiver, subject, body):
 
    # Step 1 : Create Email object

    msg = EmailMessage()

    # Step 2 : Set mail headers

    msg["From"] = sender
    msg["To"] = receiver
    msg["Subject"] = subject

    # Step 3 : Add mail body

    msg.set_content(body)

    # Step 4 : Create SMTP SSL connection manually

    smtp = smtplib.SMTP_SSL("smtp.gmail.com", 465)

    # Step 5 : Login using Gmail + App password

    smtp.login(sender, app_password)

    # Step 6 : Send the email

    smtp.send_message(msg)

    # Step 7 : Close connection manually

    smtp.quit()


# -------------------------------------------------
# Function : main
# Description : Driver code
# -------------------------------------------------

def main():
 
    # Always use separate temporary/testing account

    sender_email = "atharvaserverpython@gmail.com"

    # App password generated from Google account
 
    app_password = "jqcu vsll axjl rawb"

    # Your second email for testing

    receiver_email = "atharvaclientpython@gmail.com"

    subject = "Testing Automation Mail from Python Script"

    body = """Jay Ganesh,
    
    This is a test email sent for Python Automation Script.
    
    Thanks and Regards, 
    Atharva Enterprises
    """

    send_mail(sender_email, app_password, receiver_email, subject, body)

    print(" Mail Sent Successfully")

# -------------------------------------------------
# Program Entry Point
# -------------------------------------------------

if __name__ == "__main__":
    main()
