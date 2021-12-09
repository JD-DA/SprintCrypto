import numpy
from PIL import Image
from numpy import asarray
import Crypto
from PIL import Image
from numpy import *
from Crypto.Cipher import AES
import struct
from Crypto.Util.Padding import unpad


def tableToBytes(table):
    return b"".join([struct.pack('>B', x) for x in table])

def writeInBinaryFile(data, fileDir="./reponse.7zip"):
    with open(fileDir, 'wb') as f:
        f.write(data)

def splitIV(table, position):
    IV = [table[x] for x in range(position)]
    newTable = table[position:]
    return (IV, newTable)

if __name__ == "__main__":
    img = Image.open('tram.png')
    numpydata = asarray(img)

    print(numpydata)

    blue_image = numpydata.copy()  # Make a copy


    for i in range(3):
        imageBlue2 = blue_image[:, :, i]
        imageBleu = Image.fromarray(imageBlue2)
        imageBleu.save("imagetest" + str(i) + ".png")
        imageBlue2 = imageBlue2.reshape(-1)
        dataFinal = [i % (pow(2, 4)) for i in imageBlue2]
        print(dataFinal[:20])
        print(len(dataFinal))
        """
        bin_data = struct.pack('<H', 824)
        print('bin_data length:', len(bin_data), bin_data)"""
        octalData = []
        for j in range(0, len(dataFinal), 2):
            octalData.append(dataFinal[j] * pow(2, 4) + dataFinal[j + 1])
        print(octalData[:20])
        bytesData = tableToBytes(octalData)
        print(bytesData[:200])
        writeInBinaryFile(bytesData, fileDir="./reponse" + str(i) + ".txt")

    """
        i,j,v=numpydata.shape
        print(i,j)
        for row in range(i):
            print(row)
            for col in range(j):
                #print(imageBlue[row][col])
                #print(pixel[0]^pixel[1])
                numpydata[row][col][0]=numpydata[row][col][0]^numpydata[row][col][1]^numpydata[row][col][2]
                numpydata[row][col][1]=0
                numpydata[row][col][2]=0
        imageBleu.save("imageXor.png")
        print(numpydata)
        print(numpydata[row][col][0])
        bytesData = tableToBytes(octalData)
        key = 'LACRYPTOGRAPHIECESTLAVIE!CESTTOP'.encode()

        iv, data = splitIV(bytesData, 16)
        packIV = tableToBytes(iv)
        packData = tableToBytes(data)
        cipher = AES.new(key, AES.MODE_CBC, packIV)
        dataDecrypt = cipher.decrypt(packData)
        writeInBinaryFile(dataDecrypt)
    """








