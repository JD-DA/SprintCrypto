from PIL import Image
import base64

class Chunck:

    def __init__(self, length, type, payload, crc):
        self.length = length
        self.type = type
        self.payload = payload
        self.crc = crc

def remove_png_header(bytes):
    return bytes[8:]

def get_chunck_length(bytes):
    #print(f"bytes : {bytes[:4]}")
    #print(int.from_bytes(bytes[:4], "big"))
    return int.from_bytes(bytes[:4], "big") ,bytes[4:]

def get_chunck_type(bytes):
    return bytes[:4], bytes[4:]

def get_chunck_payload(bytes, length):
    return bytes[:length], bytes[length:]

def get_chunck_crc(bytes):
    return bytes[:4], bytes[4:]

def get_chunck(byte: bytes):
    chuncks = []

    # while byte:
    byte = remove_png_header(byte)
    
    while(len(bytes) > 0 ):
        length, byte = get_chunck_length(byte)
        print(length)
        types, byte = get_chunck_type(byte)
        payload, byte = get_chunck_payload(byte, length)
        crc, byte = get_chunck_crc(byte)
        chuncks.append(Chunck(length, types, payload, crc))
        print(types)
        if(types==b"IEND"):
            break
        if(types==b"caKe"):
            print(payload)
            for i in payload:
                print(bytes.fromhex(i))


    
    return chuncks

    

if __name__ == "__main__":
    bytes = b""

    with open("./part3/allgame.png", "rb") as file:
        for line in file.readlines():
            bytes += line

    for chunck in get_chunck(bytes):
        pass
