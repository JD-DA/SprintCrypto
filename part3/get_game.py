bytes = b""

with open("image.png", "rb") as file:
    for line in file.readlines():
        bytes += line

game_part = bytes.split(b"\x49\x45\x4e\x44\xae\x42\x60\x82")[1]
print(game_part[0])

with open("game", "wb+") as file:
    file.write(game_part)