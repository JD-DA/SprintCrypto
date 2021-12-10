import md4

def pad(msglen):
    """
    calcule le padding sha256 pour un message de longueur [msglen]
    le padding est de la forme 0x80 0x00 0x00 ... 0x00 l0 l1 ... l7
    avec l0 ... l7 la longueur du message codé sur 8 octets en grand-boutiste et de sorte que msglen + 9 + k (nb de 0x00) est
    un multiple de 64 !
    """
    count = (msglen + 9) % 64
    if count == 0:
        k = 0
    else:
        k = 64 - count
    l = (msglen*8).to_bytes(8, 'big')
    return bytes([0x80] + [0]*k) + l

def sha_cont(msglen, hexdgst):
    """
    fabrique une instance de sha256 qui se trouve dans le
    même état interne que celle qui a lu le message de longueur
    [msglen] dont le SHA256 est [hexdgst], just avant l'émission
    de ce digest, c'est-à-dire après avoir ajouté le padding.
    """
    x = md4.MD4()
    count = 8 * (msglen + len(pad(msglen)))
    x._sha['count_lo'] = count & 0xffffffff
    x._sha['count_hi'] = count >> 32
    x._sha['digest'] = [ int(hexdgst[i:i+8], 16) for i in range(0, 64, 8) ]
    return x

def extend(msglen, hexdgst, more):
    p = pad(msglen)
    x = sha_cont(msglen, hexdgst)
    x.update(more)
    return p + more, x.hexdigest()

if __name__=="__main__":
    pre = 'https://pdicost.univ-orleans.fr/cryptodm/micmac.php?'
    m = b'user=110&data=8'
    more = b'&data=1'
    h = '037f1e32a51ef99c259f0271c0d6366fa136ce7e1e8b615317969f70a6ca572c'
    mm, hh = extend(32 + len(m), h, more)
    url = pre + m.decode() + quote_from_bytes(mm, '/&=') + '&apikey=' + hh
    print(url)