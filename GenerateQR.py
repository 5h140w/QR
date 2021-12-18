import qrcode

#standard qrcode
img= qrcode.make("https://facebook.com/")
img.save("xx.png")