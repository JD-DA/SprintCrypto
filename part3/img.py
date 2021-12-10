import base64
from PIL import Image
from numpy import asarray


def traduction(text,num):
    textTraduit = ''
    for i in text:
        if (i.islower() and i.isalpha()):
            textTraduit += chr(97 + (ord(i) - num - 97) % 26)
        elif (not (i.islower()) and i.isalpha()):
            textTraduit += chr(65 + (ord(i) - num - 65) % 26)
        else:
            textTraduit += i
    return textTraduit



if __name__ == '__main__':

    #print(traduction(message, 7))

    reader = open("img.txt", "r")
    writer = open("../allgame.png", "w+b", )
    txt = reader.readlines()
    texteComplet=""
    for line in txt:
        texteComplet+=line
    decodedTxt = base64.b64decode(texteComplet)
    print(len(decodedTxt))
    writer.write(decodedTxt)
    reader.close()
    writer.close()


