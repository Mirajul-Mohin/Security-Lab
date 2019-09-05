from fractions import Fraction
import math
from decimal import *

getcontext().prec = 1024

# dec=open("4.3_ciphertext.hex","r")
# dec=dec.read()

# dec=int(dec,16)
dec=2205316413931134031046440767620541984801091216351222789180967130585669043554866325905770867150377611820746759815247778516899403229047066700396787852388511389893043279713280998235746440322483431305358901578692935378439077796777060321410661

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
                print('d is: '+ d)
                print('Decrypted text: ',bigmod(dec,d,realn))
                # print("d", d)

                return True


    return contF



mod=open("n.hex","r")
mod=mod.read()

mod=int(mod, 16)
mod=374159235470172130988938196520880526947952521620932362050308663243595788308583992120881359365258949723819911758198013202644666489247987314025169670926273213367237020188587742716017314320191350666762541039238241984934473188656610615918474673963331992408750047451253205158436452814354564283003696666945950908549197175404580533132142111356931324330631843602412540295482841975783884766801266552337129105407869020730226041538750535628619717708838029286366761470986056335230171148734027536820544543251801093230809186222940806718221638845816521738601843083746103374974120575519418797642878012234163709518203946599836959811

e=open("e.hex","r")
e=e.read()

e=int(e, 16)
e=3




cf_expansion(mod,e)