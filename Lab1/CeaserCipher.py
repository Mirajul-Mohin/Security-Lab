from collections import Counter

m = {}
                            #probability of charcters in english language
m['a'] = 0.08167

m['b'] = 0.01492

m['c'] = 0.02782

m['d'] = 0.04253

m['e'] = 0.12702

m['f'] = 0.02228

m['g'] = 0.02015

m['h'] = 0.06094

m['i'] = 0.06966

m['j'] = 0.00153

m['k'] = 0.00772

m['l'] = 0.04025

m['m'] = 0.02406

m['n'] = 0.06749

m['o'] = 0.07507

m['p'] = 0.01929

m['q'] = 0.00095

m['r'] = 0.05987

m['s'] = 0.06327

m['t'] = 0.09056

m['u'] = 0.02758

m['v'] = 0.00978

m['w'] = 0.02360

m['x'] = 0.00150

m['y'] = 0.01974

m['z'] = 0.00074


def distance(key,encrypted_str,m):
    dist=0
    encrypted_string=''

    for i in range(len(encrypted_str)):
        encrypted_string=encrypted_string+chr(((ord(encrypted_str[i])-ord('a'))-key)%26+97)

    count = Counter(encrypted_string)                       #counting frequencies of characters
    encrypted_string=list(encrypted_string)

    length=len(encrypted_string)
    encrypted_string=set(encrypted_string)

    len1=len(encrypted_string)

    for i in range(len1):
        chars = encrypted_string.pop()
        dist=dist+(length*m[chars]-count[chars])**2             #calculate the squared distance
    return dist

encrypted_file=open('ceaser_cipher.txt','r')
encrypted_org=encrypted_file.read().lower()                 #change all the characters to lowercase
encrypted_main=encrypted_org
encrypted_list=list(encrypted_org)
unwanted={' ','.',','}
encrypted_list = [ele for ele in encrypted_list if ele not in unwanted]         #this will remove the characters not in the alphabet




min=1000000
key_index=0


for i in range(1,26):
    dis=distance(i,encrypted_list,m)
    if(dis<min):
        min=dis
        key_index=i                 #calculate the minimum squared distance


print('Key : ',key_index)
print(encrypted_main)


encrypted_string = ''
for i in range(len(encrypted_main)):
    if encrypted_main[i] >= 'a' and encrypted_main[i] <= 'z':
        encrypted_string = encrypted_string + chr(((ord(encrypted_main[i]) - ord('a')) - key_index) % 26 + 97)      #main decryption string
    else:
        encrypted_string+=encrypted_main[i]          #if char is not in alphabet, it remains as it is

print(encrypted_string)
output_file=open('ceaser_decrypted.txt','w')
output_file.write(encrypted_string)
