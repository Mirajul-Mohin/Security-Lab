map={}
file1 = open("sub_key.txt", "r")
file2=open("sub_ciphertext.txt","r")

file1=file1.read()
file2=file2.read()

for i in range(0,26):
    map[file1[i]]=chr(i+65)

temp=''
for i in range(0,len(file2)):
    if(file2[i] not in map.keys()):
        temp = temp + file2[i]
    else:
        temp = temp + map[file2[i]]

print(temp)
file = open('solution01.txt','w')
file.write(temp)
