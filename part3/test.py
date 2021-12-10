from Crypto.Cipher import AES
from Crypto.Hash import HMAC, SHA256

msg = bytes.fromhex("5b86c314a5c298d34797a2c79ab2b1752eafdbc26f5c0cb5fda30245fcae48bfa9475d3c7a919b9db7c0147ef3024a77beb64ee9d66f24f5f4bbf04f3e49f018cd9dc2ae0a837a1e6281a5e17dc6ca037c668d6603de76f0c6dc")
hash = HMAC.new(pow(918_760, 885_582, 999_959).to_bytes(4, 'big'), digestmod=SHA256)
hash.update(b"bob->alice")
hash = hash.digest()

nonce = msg[:16]
c = msg [16:-16]
h = msg[-16:]

cipher = AES.new(hash, AES.MODE_GCM, mac_len=16, nonce=nonce)
bytes = cipher.decrypt(c)

print(bytes.decode('utf-8'))