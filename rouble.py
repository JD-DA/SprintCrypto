#!/usr/bin/env python3
from itertools import islice
from sys import argv

class lfsr:
    """
    LFSR en mode Fibonacci
    cf https://fr.wikipedia.org/wiki/Registre_à_décalage_à_rétroaction_linéaire
    """
    def __init__(self, n, *taps):
        "initialise un registre de longueur [n] avec bits de retour [taps]"
        self.n = n - 1
        self.taps = taps
        self.state = 0

    def seed(self, s):
        "initalise le contenu du registre"
        self.state = s & ((1 << self.n) - 1) 

    def onebit(self):
        "génère le bit suivant"
        b = self.state & 1
        nb = b
        for x in self.taps:
            nb ^= (self.state >> x) & 1
        self.state = (self.state >> 1) | (nb << self.n)
        return b

def digits(l):
    "générateur équitable d'entiers"
    m=0
    while True:
        n=0
        for i in range(5):
            n = (n << 1) | l.onebit()
        if n<30:
            yield (n%10)
            m=0
        else:
            m+=1
            if m==100:
                raise ValueError("stucked")

howmany = 200
seed = 0
regsize = 16
tap1 = 4
tap2 = 13
tap3 = 3

def usage(howmany, seed, regsize, tap1, tap2):
    x=lfsr(regsize, *[tap1, tap2])
    x.seed(seed)
    l=[]
    c=''
    for d in islice(digits(x), howmany):
        c+=str(d)
        if len(c)==5:
            l.append(c)
            c=''
    return(''.join(l))

while seed < 70000000:
    values = usage(howmany, seed, regsize, tap1, tap2)
    if (str(values)[:19] == '0566738888742956805'):
        with open("lfsr3.txt", "a") as f:
            f.write(values)
            f.write('\n')
            print('bingo')
    if (seed%1000 == 0):
        print(seed)
    seed += 1
