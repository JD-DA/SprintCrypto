def power(a, b, c):
    x = 1
    y = a

    while b > 0:
        if b % 2 != 0:
            x = (x * y) % c;
        y = (y * y) % c
        b = int(b / 2)

    return x % c

def decrypt(en_msg, p, key, q):
    dr_msg = []
    h = power(p, key, q)
    for i in range(0, len(en_msg)):
        dr_msg.append(chr(int(en_msg[i] / h)))

    return

def exponentionRapide(c1, s, mod):
    if (s == 1):
        return c1
    else:
        res = pow(c1, 2, mod)
        if (s % 2 == 0):
            return exponentionRapide(res, s // 2, mod)
        else:
            return (c1 * exponentionRapide(res, s // 2, mod)) % mod

if __name__ == "__main__":
    with open("part3/elgamal/y") as f:
        y = f.read()
    with open("part3/elgamal/n") as f:
        n = f.read()
    with open("part3/elgamal/ey") as f:
        ey = f.read()
    with open("part3/elgamal/es") as f:
        es = f.read()
    with open("part3/elgamal/c1") as f:
        c1 = f.read()
    with open("part3/elgamal/c2") as f:
        c2 = f.read()
    with open("part3/elgamal/ec1") as f:
        ec1 = f.read()
    with open("part3/elgamal/ec2") as f:
        ec2 = f.read()

    ec2 = int(ec2, 2)
    ec1 = int(ec1, 2)
    es = int(es, 2)
    n = int(n, 2)

    print(es)
    #decrypt = ec2 / ec1**(es)
    decryptN = exponentionRapide(ec1,es,n)
    print(ec2/decryptN)
    """decryptique = decrypt([ec2],ec1,es,n)
    print(decryptique)
    print(len(decryptique))
    """
