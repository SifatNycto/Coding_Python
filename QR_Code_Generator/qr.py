import qrcode

image = qrcode.make("https://github.com/SifatNycto")

image.save("qr.png", "PNG")