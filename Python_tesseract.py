from pytesseract import image_to_string
from PIL import Image#This is some library that deals with opening images and working on them 

#Example: im = Image.open(r'C:\Users\Giridhar\downloads\text.jpg')
im = Image.open(r'Paste the path of image file')

#r is just used to read the path string ignore it.
print(image_to_string(im))
