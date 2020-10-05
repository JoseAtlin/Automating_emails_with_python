import os
import smtplib
import imghdr
from email.message import EmailMessage
from PIL import Image, ImageDraw, ImageFont
import pandas as pd


def send_certificate(certificate_name, email_add):
    msg = EmailMessage()
    msg['Subject'] = "Digital Certificate"
    msg['From'] = EMAIL_ADDRESS
    msg.set_content('Certificate of Participation')
    msg['To'] = email_add

    with open(certificate_name, 'rb') as f:
        file_data = f.read()
        file_type = imghdr.what(f.name)
        file_name = f.name

    msg.add_attachment(file_data, maintype='image', subtype=file_type, filename=file_name)

    with smtplib.SMTP_SSL('smtp.gmail.com', 465) as smtp:
        smtp.login(EMAIL_ADDRESS, EMAIL_PASSWORD)
        smtp.send_message(msg)


def create_certificate(name, college, year, email_add):
    image = Image.open(ORIGINAL_CERTIFICATE)
    draw = ImageDraw.Draw(image)
    draw.text((X1, Y1), name, fill=FONT_COLOR, font=FONT)
    draw.text((X2, Y2), college, fill=FONT_COLOR, font=FONT)
    draw.text((X3, Y3), str(year), fill=FONT_COLOR, font=FONT)
    certificate_name = name + " " + college + ".jpg"
    image.save(certificate_name)
    send_certificate(certificate_name, email_add)
    del draw
    del image


EMAIL_ADDRESS = os.environ.get('EMAIL_ADD')
EMAIL_PASSWORD = os.environ.get('EMAIL_PASS')


ORIGINAL_CERTIFICATE = "original.jpg"
(X1, Y1) = (850, 1925)
(X2, Y2) = (250, 2050)
(X3, Y3) = (400, 2000)
FONT = ImageFont.truetype("arial.ttf", 60)
FONT_COLOR = 'rgb(0, 0, 0)'


data = pd.read_csv('input.csv')
names = data['full_name']
college_names = data['college_name']
sem_year = data['year']
email_id = data['email']

for row in range(len(names)):
    name, college, year, email_add = names[row], college_names[row], sem_year[row], email_id[row]
    print(name, college, year, email_add)
    create_certificate(name, college, year, email_add)
