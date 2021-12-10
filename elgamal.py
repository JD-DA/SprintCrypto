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
decrypt = ec2 / ec1**(es)
print(decrypt)
print(len(decrypt))

