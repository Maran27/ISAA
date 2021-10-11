import random as rn
import json

keysopen = open("keys.txt", "r")
keys = json.loads(keysopen.readline())
keysopen.close()

e = keys["Public and Private Key"]["Public Key Pair"]["E"]
d = keys["Public and Private Key"]["Private Key"]["D"]
n = keys["Public and Private Key"]["Public Key Pair"]["N"]
key = keys["Random Symmetric Key"]["Symmetric Key"]


def ekeys():
    print('\033[1m' + 'Details of the Keys' + '\033[0m')
    print("Public Key: ", e)
    print("Common Modulus: ", n)
    print("Random Symmetric Key: ", key)
    print()


def keyencryption(key1, e1):
    print('\033[1m' + 'Encryption of the Keys Using Asymmetric Algorithm' + '\033[0m')
    print("Starting the Encryption Process....")
    CM = pow(key1, e1, n)
    print("The Encrypted Key is: ", CM)
    print()
    return {"Encrypted Key": CM}


def messageencryption(m, key1):
    print('\033[1m' + 'Encryption of the Message using Symmetric Algorithm' + '\033[0m')
    print('The Original Message is: ', m)
    mes = bin(m)
    print('The Binary Value of Original Message: ', mes)
    print()
    print("Starting the Encrypting Process.....")
    mes1 = int(mes, 2) << 1
    print('Applying the Left Shift Operation on Message')
    mes2 = bin(mes1)
    print('After Applying Shift Operation: ', mes2)
    print('After Applying Shift Operation Value is: ', mes1)
    en = mes1 ^ key1
    print('Applying the XOR Operation')
    en1 = bin(en)
    print('After applying XOR operation: ', en1)
    print('Value after applying XOR operation is: ', en)
    print()
    return {"Encrypted Message": en}

ekeys()
message = rn.getrandbits(10)
ke = keyencryption(e, key)
me = messageencryption(message, key)

print('\033[1m' + 'DIGITAL ENVELOPE' + '\033[0m')
print("Creating the Digital Envelope")
DEMK = {"Encrypted Key": ke, "Encrypted Message": me, "Message": message}
print(DEMK)
saveFile = open("Digital_Envelope.txt", "wt")
saveFile.write(json.dumps(DEMK))
saveFile.close()
print("Digital Envelope Created")
print('NOTE: Here all the values are automatically generated')
