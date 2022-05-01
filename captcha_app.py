from asyncore import write
from re import A
from captcha.image import ImageCaptcha

image = ImageCaptcha()



def create_captcha(text) :
    image.write(text,"captcha.png")
   
a="kadir"
create_captcha(a)