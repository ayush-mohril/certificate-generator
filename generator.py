from PIL import Image as im
from PIL import ImageDraw as imdr
from PIL import ImageFont as imf
import os
import pandas as pa
from numba import jit

def generator():
  os.chdir('C:/Users/mohri/Documents/python files/certificate generator')
  df =pa.read_excel('example.xlsx')
  for index,row in df.iterrows():
    image1=im.open('c1.png');
    name=row['name']
    branch=row['branch']
    year=row['year']
    draw =imdr.Draw(image1)
    ifont=imf.truetype('pacifico.ttf',50)
    draw.text((400,350),text=str(name),fill=(25,38,36),font=ifont)
    image1.save( "C:/Users/mohri/Documents/python files/certificate generator/certificates/" + name +'.png')
    print(index,name)

if __name__=='__main__':
    generator()
