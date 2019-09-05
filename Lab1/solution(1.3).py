import codecs
from Crypto.Cipher import AES

file=open('aes_weak_ciphertext.hex','r')

file=file.read()

file=codecs.decode(file,'hex')

vector=''
for k in range(0,16):
    vector=vector+chr(0)


key=''
for k in range(0,31):
    key=key+chr(0)


for i in range(0,32):
    cipher=AES.new(key+chr(i),AES.MODE_CBC,vector)
    decrypted_text=cipher.decrypt(file)
    print('index: ',i+1,'',decrypted_text)

index=input('Index: ')
found_key="{0:#{1}x}".format(int(index),66)
f=open('Solution03.hex','w')
f.write(found_key)
f.close()


cipher=AES.new(key+chr(int(index)-1),AES.MODE_CBC,vector)
print(cipher.decrypt(file).decode("utf-8"))
