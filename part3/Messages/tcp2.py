from Crypto.Cipher import AES
from Crypto.Hash import HMAC, SHA256
from Crypto.Random.random import randint
g=2
n=999959
kab=None
kba=None
def envoie(s,qui,quoi):
    s.send('{}: {}\n'.format(qui,quoi.hex()).encode())
def recoit(s):
    data=s.recv()
    st=data.index(b' ')
    return bytes.fromhex(data[st+1:-1].decode())
def start_alice(s):
   "invoqué avant toute opération chez alice"
   global kab,kba
   # DH
   a=randint(n//2,n)
   x=pow(g,a,n)
   envoie(s,'alice',x.to_bytes(4,'big'))
   y=int.from_bytes(recoit(s),'big')
   # secret partagé
   k=pow(y,a,n).to_bytes(4,'big')
   # dérivation de clés
   h=HMAC.new(k, digestmod=SHA256)
   h.update(b'alice->bob')
   kab=h.digest()
   h=HMAC.new(k, digestmod=SHA256)
   h.update(b'bob->alice')
   kba=h.digest()
def send_alice(s,data):
   "invoqué pour envoyer un message côté alice"
   cipher=AES.new(kab, AES.MODE_GCM, mac_len=16)
   assert len(cipher.nonce)==16
   c,h=cipher.encrypt_and_digest(data)
   msg=cipher.nonce+c+h
   envoie(s,'alice',msg)
def recv_alice(s):
   "invoqué pour recevoir un message côté alice"
   msg=recoit(s)
   nonce=msg[:16]
   c=msg[16:-16]
   h=msg[-16:]
   cipher=AES.new(kba, AES.MODE_GCM, mac_len=16, nonce=nonce)
   data=cipher.decrypt_and_verify(c,h)
   return data
def start_bob(s):
   "invoqué avant toute opération chez bob"
   global kab,kba
   # DH
   b=randint(n//2,n)
   y=pow(g,b,n)
   envoie(s,'bob',y.to_bytes(4,'big'))
   x=int.from_bytes(recoit(s),'big')
   # secret partagé
   k=pow(x,b,n).to_bytes(4,'big')
   # dérivation de clés
   h=HMAC.new(k, digestmod=SHA256)
   h.update(b'alice->bob')
   kab=h.digest()
   h=HMAC.new(k, digestmod=SHA256)
   h.update(b'bob->alice')
   kba=h.digest()
def send_bob(s,data):
   "invoqué pour envoyer un message côté bob"
   cipher=AES.new(kba, AES.MODE_GCM, mac_len=16)
   assert len(cipher.nonce)==16
   c,h=cipher.encrypt_and_digest(data)
   msg=cipher.nonce+c+h
   envoie(s,'bob',msg)
def recv_bob(s):
   "invoqué pour recevoir un message côté bob"
   msg=recoit(s)
   nonce=msg[:16]
   c=msg[16:-16]
   h=msg[-16:]
   cipher=AES.new(kab, AES.MODE_GCM, mac_len=16, nonce=nonce)
   data=cipher.decrypt_and_verify(c,h)
   return data
