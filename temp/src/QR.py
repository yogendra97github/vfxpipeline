import pyqrcode
import os
import shutil

title = input("Give your QR code a title! >>")
text = input("What would you like the QR code to say? ??")

file_name_svg = title + ".svg"
file_name_png = title + ".png"

url = pyqrcode.create(text)

url.svg(file_name_svg, scale=8)
url.png(file_name_png, scale=10)

os.mkdir(fr"C:\\Users\\acer\\Desktop\\QR\\{title}")

shutil.move(file_name_png, fr"C:\\Users\\acer\\Desktop\\QR\\{title}")
shutil.move(file_name_svg, fr"C:\\Users\\acer\\Desktop\\QR\\{title}")
