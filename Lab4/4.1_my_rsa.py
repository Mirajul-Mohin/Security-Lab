p=int(input('p: '))
q=int(input('q: '))
n=p*q
print("\nn = " + str(n) )
phi=(p-1)*(q-1)
print("phi(n): " + str(phi) + "\n")


def gcd(a, b):
    while b != 0:
        c = a % b
        a = b
        b = c
    return a

def modinv(a, m):
    for x in range(1, m):
        if (a * x) % m == 1:
            return x
    return None

def coprimes(a):
    l = []
    for x in range(2, a):
        if gcd(a, x) == 1 and modinv(x,phi) != None:
            l.append(x)
    for x in l:
        if x == modinv(x,phi):
            l.remove(x)
    return l

e=coprimes(phi)[3]
d=modinv(e,phi)
print("\npublic key pair (e=" + str(e) + ", n=" + str(n) + ").\n")
print("private key pair (d=" + str(d) + ", n=" + str(n) + ").\n")

m = int(input("Enter a message to encrypt: "))
m = m ** e
m = m % n
print("\nEncrypted message: " , m , "\n")
print("Decrypted message: " , m**d % n , "\n")
