import qrcode
from functions.getDetails import Get_Details
from PIL import Image
from time import time

def GenQRCode(link):
    qr= qrcode.QRCode(version=10, error_correction=qrcode.constants.ERROR_CORRECT_M,box_size=10,border=4)
    qr.make(fit=True)
    colors, logo,location = Get_Details(link)
    img = qr.make_image(fill_color=colors[0], back_color=colors[1]).convert('RGBA')
    if logo:
        logo_display = Image.open(logo)
        logo_display.thumbnail((120,120))
        logo_pos = ((img.size[0] - logo_display.size[0]) // 2, (img.size[1] - logo_display.size[1]) // 2)
        img.paste(logo_display,logo_pos)   
    
    filename= str(time()).split(".")[0]
    savedFolder= location+"/"+filename+".png"
    img.save(savedFolder)