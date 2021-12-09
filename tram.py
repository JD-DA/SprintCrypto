from typing import List, Union, Any
from Crypto.Util.strxor import strxor
from PIL import Image, ExifTags
import numpy as np

class Color:

    def __init__(self, red: int, green: int, blue: int, alpha: int = 0) -> None:
        self.red = red
        self.green = green
        self.blue = blue
        self.alpha = alpha

    def __eq__(self, target: Any) -> bool:
        if not isinstance(target, Color):
            return False
        return self.red == target.red and self.green == target.green and self.blue == target.blue

    def __str__(self) -> str:
        return f"(r:{self.red}, g:{self.green}, b:{self.blue}, a:{self.alpha})"

class Pixel:

    def __init__(self, color: Color, x: int, y: int) -> None:
        self.color = color
        self.x = x
        self.y = y

    def __str__(self) -> str:
        return f'color : {self.color}, pos: ({self.x}, {self.y})'


def get_pixel_of_image(image: List[List[List[int]]]) -> List[Pixel]:
    pixels = []

    for y, row in enumerate(image):
        for x, color_of_pixel in enumerate(row):
            pixels.append(Pixel(Color(*color_of_pixel), x, y))

    return pixels

def get_all_rgb_component(image: List[List[List[int]]]) -> List[int]:
    red_pixels, green_pixels, blue_pixels = [], [], []

    for row in image:
        for red, green, blue in row:
            red_pixels.append(red)
            green_pixels.append(green)
            blue_pixels.append(blue)

    return red_pixels, green_pixels, blue_pixels

def get_lower_bits(bytes: bytes) -> int:
    return [byte & 1 for byte in bytes]

image = Image.open("cake.png")
image = np.array(image)

print(image[0][0])
pixels = get_pixel_of_image(image)
red_pixels, green_pixels, blue_pixels = get_all_rgb_component(image)
hash_red = bytes(red_pixels)
hash_green = bytes(green_pixels)
hash_blue = bytes(blue_pixels)
rgb_pixels = []


"""
for pixel in pixels:
    rgb_pixels.append(pixel.color.red)
    rgb_pixels.append(pixel.color.green)
    rgb_pixels.append(pixel.color.blue)

rgb_pixels = bytes(rgb_pixels)
lower = get_lower_bits(rgb_pixels)
lower = "".join(str(l) for l in lower)

binaries = []

for i in range(0, len(lower), 8):
    binaries.append(lower[i:i+8].zfill(8))

for binary in binaries:
    if binary != "11111111":
        print(chr(int(binary, 2)), end="")
"""









