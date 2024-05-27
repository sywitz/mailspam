#!/usr/bin/env python

import os
import smtplib
import pandas as pd
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText

# Load email data from CSV file
email_data = pd.read_csv('emails.csv')

# Print column names for debugging
print("Column names in CSV file:", email_data.columns)

# Ensure column names are stripped of leading/trailing spaces
email_data.columns = email_data.columns.str.strip()

# Email configuration
smtp_server = 'smtp.gmail.com'
smtp_port = 587
smtp_user = os.getenv('SMTP_USER')
smtp_password = os.getenv('SMTP_PASSWORD')

# Print environment variables for debugging
print(f'SMTP_USER: {smtp_user}')
print(f'SMTP_PASSWORD: {smtp_password}')

# Email content
subject = 'Your Subject Here'
body = 'Hello {name},\n\nYou are being watched.\n\nBest regards,\nSylas'

# Function to send email
def send_email(to_address, name):
    msg = MIMEMultipart()
    msg['From'] = smtp_user
    msg['To'] = to_address
    msg['Subject'] = subject
    
    # Personalize the email body
    body_formatted = body.format(name=name)
    msg.attach(MIMEText(body_formatted, 'plain'))
    
    try:
        # Set up the server
        server = smtplib.SMTP(smtp_server, smtp_port)
        server.starttls()
        server.login(smtp_user, smtp_password)
        
        # Send the email
        server.sendmail(smtp_user, to_address, msg.as_string())
        print(f'Email sent to {to_address}')
        
        # Close the server
        server.quit()
    except Exception as e:
        print(f'Failed to send email to {to_address}: {e}')

# Send emails individually
for index, row in email_data.iterrows():
    try:
        send_email(row['email'], row['name'])
    except KeyError as e:
        print(f"KeyError: {e} - Check the column names in your CSV file")
    except Exception as e:
        print(f"An error occurred: {e}")
