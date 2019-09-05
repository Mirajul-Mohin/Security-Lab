from pymd5 import md5, padding
import urllib


file=open("3.3_query.txt","r")
file=file.read()

charBeforeHash = file[:file.find("=")+1]
print("Char Before Hash: "+charBeforeHash)

currentHashValue = file[file.find("=")+1:file.find("&")]
print("Current Hash Value: "+currentHashValue)

userMessage = file[file.find("&")+1:]
print("User Message: "+userMessage)


secretAndMsgLen = len(userMessage)+8 
print("Length (secret+msg) in Byte:"+ str(secretAndMsgLen))


paddingLen = len(padding(secretAndMsgLen*8))
print("Padding Length (in Byte): "+ str(paddingLen))


bitLength = (secretAndMsgLen + len(padding(secretAndMsgLen*8)))*8
print("Total Length (key+Msg+Padding): "+ str(bitLength))


file=open("3.3_command3.txt","r")
file=file.read()

setStates = md5(state=currentHashValue.decode("hex"), count=bitLength)
setStates.update(file)


padding = urllib.quote(padding(secretAndMsgLen*8))
print("Padding to be inserted: "+padding)


newMessage = userMessage + padding + file
newhash = setStates.hexdigest()
print("New hash Value: "+newhash)


newUrl = charBeforeHash+newhash+"&"+newMessage
print("New url is: "+ str(newUrl))

file= open("solution33.txt","w")
file.write(newUrl)
# test=md5(string=newMessage)
# print(test.hexdigest())
