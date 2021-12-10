from Crypto.Cipher import AES
from Crypto.Hash import HMAC, SHA256
from Crypto.Random.random import randint
import socket

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

# 0001c830

def start_alice(s):
   "invoqué avant toute opération chez alice"
   global kab,kba
   # DH
   a=randint(n//2,n) # ---> Inconnu : range(999959)
   x=pow(g,a,n) # ---> Inconnu mais devinable par 2^a % 999959
   envoie(s,'alice',x.to_bytes(4,'big'))
   y=int.from_bytes(recoit(s),'big') # ----> Inconnu
   # secret partagé
   k=pow(y,a,n).to_bytes(4,'big') # ---> Inconnu <=> y^a % 999959
   # dérivation de clés
   h=HMAC.new(k, digestmod=SHA256)
   h.update(b'alice->bob')
   kab=h.digest() # ---> clef alice -> bob
   h=HMAC.new(k, digestmod=SHA256)
   h.update(b'bob->alice')
   kba=h.digest() # ---> clef bob -> alice

y = int.from_bytes("0001c830", 'big')
k = pow(y, a, n).to_bytes(4,'big')

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


