from PIL import Image

loc = input("Please enter the path of image: ")

im = Image.open(loc)

width, height = im.size

static = int(input("Enter top value: "))

left = int(input("Enter left value: "))
top = height / static
right = int(input("Enter right value: "))
bottom = 3 * top

im1 = im.crop((left, top, right, bottom))

size = int(input("Size: "))

newsize = (size, size)

im1 = im1.resize(newsize)
# Shows the image in image viewer
im1.show()
