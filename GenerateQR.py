import qrcode

#standard qrcode
##Function: 
def easyWay(link):
    img= qrcode.make(link)
    img.save("xx.png")

easyWay("facebook.com")