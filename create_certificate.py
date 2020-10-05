from PIL import Image, ImageDraw, ImageFont
import pandas as pd


def create_certificate(name, college, year, email_add):
    image = Image.open(ORIGINAL_CERTIFICATE)
    draw = ImageDraw.Draw(image)
    draw.text((X1, Y1), name, fill=FONT_COLOR, font=FONT)
    draw.text((X2, Y2), college, fill=FONT_COLOR, font=FONT)
    draw.text((X3, Y3), str(year), fill=FONT_COLOR, font=FONT)
    certificate_name = name + " " + college + ".jpg"
    image.save(certificate_name)
    del draw
    del image


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
