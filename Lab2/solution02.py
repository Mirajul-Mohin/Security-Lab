
def masking(input):
    Mask= 0x3FFFFFFF
    outHash= 0
    for i in range(0,len(input)):
        intermediate_value = ((ord(input[i]) ^ 0xCC) << 24) | ((ord(input[i]) ^ 0x33) << 16) | ((ord(input[i]) ^ 0xAA)<< 8) |  (ord(input[i]) ^ 0x55)
        outHash =(outHash & Mask) + (intermediate_value & Mask)
    return outHash

file = open('3.2_input_string.txt','r')
file = file.read()

print("Original String: "+file)

print("Hash Value: "+hex(masking(file)))

words = file.split()
sentence_rev = " ".join(reversed(words))
print("New String: "+sentence_rev)

print("Hash Value of New String: "+hex(masking(sentence_rev)))

file= open("solution32.txt",'w')
file.write(sentence_rev)



