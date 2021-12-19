import qrcode
import PIL
from qrcode import constants

#qrcodev1 (only link)
##Function: 
def v1(link):
    img= qrcode.make(link)
    img.save("xx.png")

v1("facebook.com")

#qrcodev2(link + colors)
def v2(link,colors):
    qr=qrcode.QRCode(
        version=1,
        error_correction=qrcode.constants.ERROR_CORRECT_H,
        box_size=12,
        border=2
    )
    qr.add_data(link)
    qr.make(fit=True)
    img = qr.make_image(fill=colors[0],back_color=colors[1])
    print(type(img))
    img.save("xx1.png")

v2("wwww",["black","white"])


##qrcode3(link+color+logo)
def v3(link,color,logo):
    qr= qrcode.QRCode(version=2,error_correction=constants.ERROR_CORRECT_M,box_size=12,border=5)
    qr.add_data(link)
    qr.make(fit=True)
    img = qr.make_image()