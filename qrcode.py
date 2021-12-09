from sys import argv,stdin
from PIL import Image, ImageDraw, ImageFont

if __name__ == "__main__":
    file_name = "ecran"
    img = Image.open(f"{file_name}.png")
    width,height = img.size

    red = Image.new('L', (width, height), color=255)
    green = Image.new('L', (width, height), color=255)
    blue = Image.new('L', (width, height), color=255)
    masqueRouge = Image.new('L', (width, height), color=255)
    masqueVert = Image.new('L', (width, height), color=255)
    masqueBleu = Image.new('L', (width, height), color=255)

    for row in range(height):
        for col in range(width):
            (r,g,b)= img.getpixel((col, row))
            if max((r),(g),(b)) >200:
                pixel = 1
            else :
                pixel = 0
            masqueRouge.putpixel((col, row), 255 * (pixel ^ (r % 2)))
            masqueVert.putpixel((col, row), 255 * (pixel ^ (g % 2)))
            masqueBleu.putpixel((col, row), 255 * (pixel ^ (b % 2)))
    """
    for row in range(10):
        for col in range(1):
            (r, g, b) = img.getpixel((col, row))
            print(r,g,b)
            noir = max((r % 2), (g % 2), (b % 2))
            print(noir)
            masqueRouge.putpixel((col, row), 255 * (noir ^ (r % 2)))
            masqueVert.putpixel((col, row), 255 * (noir ^ (g % 2)))
            masqueBleu.putpixel((col, row), 255 * (noir ^ (b % 2)))"""


    masqueRouge.save(f'{file_name}_red.png')
    masqueVert.save(f'{file_name}_green.png')
    masqueBleu.save(f'{file_name}_blue.png')
