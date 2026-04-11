from PIL import Image, ImageFilter

before = Image.open("yard.bmp")

after = before.filter(ImageFilter.FIND_EDGES)

after.save("yardEdges.bmp")