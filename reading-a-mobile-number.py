# -*- coding: utf-8 -*-
"""m22ma012_Q10.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1ZcIPzohO2UrgTu6__T0w-LvEAx9v2PgK

**Q10: LAST 3 DIGITS OF A MOBILE NUMBER**
"""

!pip install pyocr
!apt-get install tesseract-ocr-eng

import cv2
import numpy as np
from PIL import Image
import pyocr
import pyocr.builders

'''Load image'''
image = cv2.imread("/content/Screenshot 2023-01-08 at 5.14.24 PM.png")

'''Convert to grayscale'''
gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

'''Apply threshold to binarize the image'''
_, thresh = cv2.threshold(gray, 150, 255, cv2.THRESH_BINARY)

'''Save binarized image to file'''
cv2.imwrite("binarized.jpg", thresh)

'''Load binarized image'''
binarized = Image.open("binarized.jpg")

'''Initialize OCR tool'''
tools = pyocr.get_available_tools()
tool = tools[0]

'''Set up OCR builder to extract 3 digits'''
builder = pyocr.builders.DigitBuilder(tesseract_layout=6)

'''Perform OCR on image'''
result = tool.image_to_string(binarized, builder=builder)

'''Extract 3 digits'''
digits = result[7:]

'''Print result'''
print("Extracted digits:", digits)
