from fractions import Fraction
import math
from decimal import *

getcontext().prec = 1024

dec=open("4.3_ciphertext.hex","r")
dec=dec.read()

dec=int(dec,16)


def continued_fraction_sum(frac):
	rev_frac=list(reversed(frac))
	sum=Fraction(0,1)
	one = Fraction(1, 1)
	for each_val in rev_frac:
		sum=sum._add(each_val)
		sum = one._div(sum)
	#print(sum._denominator)
	return  sum



def bigmod(a, p,m ):
    if (p == 0):
        return 1

    if (p & 1):

        return ((a % m) * (bigmod(a, p - 1, m))) % m

    else:
        tmp = bigmod(a, p / 2, m)
        return (tmp * tmp) % m



def cf_expansion(n, e):
    contF = []
    reale=e
    realn=n

    q = e // n
    r = e % n

    while r != 0:
        e, n = n, r
        q = e // n
        
        r = e % n
        contF.append(q)

        sum = continued_fraction_sum(contF)
        d = sum._denominator
        k = sum._numerator

        if d % 2 == 0:
           continue

        phik = ((reale * d) - 1)
        if k == 0 or phik % k != 0:
           continue

        phi = ((reale * d) - 1) / k
        b = -realn + phi - 1


        up = Decimal((b * b) - 4 * realn)
        sq=-1
        if up>=0:
            sq= (math.sqrt(Decimal(b * b) - 4 * realn))



        if sq >= 0:
            x1 = (-b + sq ) / 2
            x2 = (-b - sq) / 2

            if (x1%1)== 0 and (x2%1)==0:

                #print('Root1: ',x1,"Root2: ",x2,"d: ",d)
                print('Decrypted text: ',bigmod(dec,d,realn))
                print("d", d)

                return True


    return contF



mod=open("4.5_modulo.hex","r")
mod=mod.read()

mod=int(mod, 16)

e=open("4.4_public_key.hex","r")
e=e.read()

e=int(e, 16)




cf_expansion(mod,e)