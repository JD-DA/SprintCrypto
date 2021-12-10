from Crypto.Cipher import AES
from Crypto.Hash import HMAC, SHA256

"""
msg = bytes.fromhex("3902ba33e1942edf4f16eebb6fab4be7e949916098b735a84a4d9b636b4a42139e38a1ae98d587e3a578b5433dead800806513cd63040add07b83ffcc196afb64cac15ee2fa759bf6783d09e8bdb4af615dbf6ea89d14a57cef37448e41305cff24a3ed112bc2574e3316ce5ace8dfc8b486062076006b2fed9bf0a7f370fbe3")
hash = HMAC.new(pow(918_760, 885_582, 999_959).to_bytes(128, 'big'), digestmod=SHA256)
hash.update(b"bob->alice")
hash = hash.digest()

nonce = msg[:16]
c = msg [16:-16]
h = msg[-16:]

cipher = AES.new(hash, AES.MODE_GCM, mac_len=16, nonce=nonce)
bytes = cipher.decrypt(c)

print(bytes.decode('utf-8'))
"""

hexa = "3902ba33e1942edf4f16eebb6fab4be7e949916098b735a84a4d9b636b4a42139e38a1ae98d587e3a578b5433dead800806513cd63040add07b83ffcc196afb64cac15ee2fa759bf6783d09e8bdb4af615dbf6ea89d14a57cef37448e41305cff24a3ed112bc2574e3316ce5ace8dfc8b486062076006b2fed9bf0a7f370fbe3"
decimal_value = int.from_bytes(bytes.fromhex(hexa), 'big')
print(decimal_value)