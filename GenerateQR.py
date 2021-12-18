import qrcode

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
    img.save("xx1.png")

v2("wwww",["black","white"])