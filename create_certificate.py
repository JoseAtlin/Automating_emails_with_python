from PIL import Image, ImageDraw, ImageFont
import pandas as pd


def create_certificate(name, college, year):
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


data = pd.read_csv('MOCK_DATA.csv')
names = data['first_name']
college_name = data['company_name']
sem_year = data['year']

for row in range(1):
    name, college, year = names[row], college_name[row], sem_year[row]
    print(name, college, year)
    create_certificate(name, college, year)
