from sys import argv,stdin
from PIL import Image, ImageDraw, ImageFont

file_name = "part2/img_1"
img = Image.open(f"{file_name}.png")
width,height = img.size

red = Image.new('L', (width, height), color=255)
green = Image.new('L', (width, height), color=255)
blue = Image.new('L', (width, height), color=255)
rgb = Image.new('L', (width, height), color=255)

for row in range(height):
    for col in range(width):
        (r,g,b)= img.getpixel((col, row))
        red.putpixel((col, row), 255 * (r % 2))
        green.putpixel((col, row), 255 * (g % 2))
        blue.putpixel((col, row), 255 * (b % 2))
        rgb.putpixel((col, row), min(255 * (r % 2), 255 * (g % 2), 255 * (b % 2)))

red.save(f'{file_name}_red.png')
green.save(f'{file_name}_green.png')
blue.save(f'{file_name}_blue.png')
rgb.save(f'{file_name}_rgb.png')