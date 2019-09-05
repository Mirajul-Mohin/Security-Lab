
file1= 'de4960933bf2bac6dd5ab2b55543d20a2043e51b35adab3528cb7fd0454d55f2'
file2= '78ef06a64e25bc760134d5360a48bf038dafc5a7eab2390ada4d8bd6db19c49d'


file1= bin(int(file1, 16))[2:].zfill(256)
file2= bin(int(file2, 16))[2:].zfill(256)

count=0

for i in range(0,min(len(file1),len(file2))):
    if file1[i] != file2[i]:
        count+=1

count= count + max(len(file1),len(file2))-min(len(file1),len(file2))
print(count)
print(hex(count))

file= open("solution31.hex","w")
file.write(hex(count))