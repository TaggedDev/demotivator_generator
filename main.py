#!/usr/bin/python
# -*- coding: utf-8 -*-

import requests
import sys
import numpy
from PIL import Image, ImageFont, ImageDraw, ImageFont

#161 ^ 170

# OPEN 
blank = Image.open("D:\\Code\\PYTHON\\MemeGen\\portret.jpg")
picture = Image.open("D:\\Code\\PYTHON\\MemeGen\\pic.jpg")

# RESIZE 
picture = picture.resize((161, 170), Image.ANTIALIAS)
picture.save('resizedpic.jpg')
picture_size = picture.size

# PASTE TWO PICTURES
blank.paste(picture, (40, 40 ))# picture_size[1], picture_size[1]))
print(blank.size, picture_size[0], picture_size[1])

# TEXT | 203px | 270px OF TOP
userText = input(u'Текст мема: ')
userText = userText.encode('utf-8')
letters = 0
for i in userText:
    letters +=1

# WRITING TEXT
draw = ImageDraw.Draw(blank)
fontl = ImageFont.truetype("arial.ttf", 50)
coordinates = 30, 50
draw.text(coordinates, userText, fill=(255,255,0), font=fontl ) #270, int(203/letters)
blank.show()

# SAVE FILE
blank.save("D:\\Code\\PYTHON\\MemeGen\\result.jpg")
#blank.show()
#photo = input('Введите название фото (в той же папке что и файл): ')