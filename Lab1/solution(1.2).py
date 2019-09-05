from Crypto.Cipher import AES
import codecs

CipherText= open("aes_ciphertext.hex","r")
CipherText=CipherText.read()

CipherInitVector= open("aes_iv.hex","r")
CipherInitVector=CipherInitVector.read()

CipherKey= open("aes_key.hex","r")
CipherKey=CipherKey.read()

SolutionText=open("solution02.txt","w")

CipherText=codecs.decode(CipherText, "hex")
CipherInitVector=codecs.decode(CipherInitVector, "hex")
CipherKey=codecs.decode(CipherKey, "hex")


cipher = AES.new( CipherKey, AES.MODE_CBC, CipherInitVector)
decrypted = cipher.decrypt(CipherText)

print(decrypted.decode("utf-8"))
SolutionText.write(decrypted.decode("utf-8"))