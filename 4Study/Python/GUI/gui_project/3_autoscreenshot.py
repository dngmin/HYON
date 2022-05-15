from time import *
from PIL import ImageGrab

#python image library   #pip install Pillow

sleep(1)

for i in range(1,3):
    img=ImageGrab.grab()   #현재 스크린 이미지를 가져옴
    img.save("image{}.png".format(i))
    sleep(1)