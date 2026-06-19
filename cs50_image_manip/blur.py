from PIL import Image, ImageFilter

before = Image.open("yard.bmp")

x = float(input("entr blur value: "))

after = before.filter(ImageFilter.GaussianBlur(x))

after.save("yardBlur.bmp")