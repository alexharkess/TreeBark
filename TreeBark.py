
# coding: utf-8

# In[7]:

import sys
import pytesseract
from PIL import Image
from PIL import ImageFilter


# In[64]:

def iswhite(value):
    if value == (255,255,255):
        return True

# Open the tree file, convert to b&w, extract tip ids with OCR

img = Image.open("/Users/alex/GitHub/TreeBark/Geraniales-tree.jpg")
img = img.convert('1')
print(pytesseract.image_to_string(img))





# In[56]:




# In[ ]:



