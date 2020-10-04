import os
import imghdr
import smtplib
from email.message import EmailMessage

EMAIL_ADDRESS = os.environ.get('EMAIL_ADD')
EMAIL_PASSWORD = os.environ.get('EMAIL_PASS')

contacts = ['abc@gmail.com', '123@gmail.com']
files = ['dog1.jpg', 'dog2.jpg']

msg = EmailMessage()
msg['Subject'] = 'Sending email using Python'
msg['From'] = EMAIL_ADDRESS
msg['To'] = ', '.join(contacts)
msg.set_content('Attachments are added and this is confidential')

for file in files:
    with open(file, 'rb') as f:
        file_data = f.read()
        file_type = imghdr.what(f.name)
        file_name = f.name

    msg.add_attachment(file_data, maintype='image', subtype=file_type, filename=file_name)

with smtplib.SMTP_SSL('smtp.gmail.com', 465) as smtp:
    smtp.login(EMAIL_ADDRESS, EMAIL_PASSWORD)
    smtp.send_message(msg)
