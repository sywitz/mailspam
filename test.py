import pandas as pd

# Load email data from CSV file
email_data = pd.read_csv('emails.csv')

# Print the column names
print(email_data.columns)

import os

smtp_user = os.getenv('SMTP_USER')
smtp_password = os.getenv('SMTP_PASSWORD')

print(f'SMTP_USER: {smtp_user}')
print(f'SMTP_PASSWORD: {smtp_password}')