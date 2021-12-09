image_byte = b""

with open('img_1.png', "rb") as file:
    for line in file.readlines():
        image_byte += line

seven_zip_part = image_byte.split(b'\x00\x00\x00\x00\x49\x45\x4e\x44\xae\x42\x60\x82')[1]

with open('img_1_ouput.7z', "wb") as file:
    file.write(seven_zip_part)