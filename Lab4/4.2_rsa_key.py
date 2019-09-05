from Crypto.PublicKey import RSA

private_key = open("a", "r").read()
public_key = open("a.pub", "r").read()
rsapri = RSA.importKey(private_key)
rsapub = RSA.importKey(public_key)

msg = "hello world"
print(msg)
enc = rsapub.encrypt(msg, "")[0]
print(enc.encode("hex"))
dec = rsapri.decrypt(enc)
print(dec)