import qrcode


img = qrcode.make("www.google.com")
img.save("test.jpg")
img.save("test.png")


