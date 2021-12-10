byte = b""

with open('bugs.png', "rb") as file:
    for line in file.readlines():
        byte += line

seven_part = byte.split(b'\x00\x00\x00\x00\x49\x45\x4e\x44\xae\x42\x60\x82')[1]

with open("bugs_seven.7z", "wb") as file:
    file.write(seven_part)