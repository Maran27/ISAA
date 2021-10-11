import json

keysopen = open("keys.txt", "r")
keys = json.loads(keysopen.readline())
keysopen.close()

e = keys["Public and Private Key"]["Public Key Pair"]["E"]
d = keys["Public and Private Key"]["Private Key"]["D"]
n = keys["Public and Private Key"]["Public Key Pair"]["N"]
key = keys["Random Symmetric Key"]["Symmetric Key"]

envelope = open("Digital_Envelope.txt", "r")
message = json.loads(envelope.readline())
envelope.close()

ek = message["Encrypted Key"]["Encrypted Key"]
em = message["Encrypted Message"]["Encrypted Message"]
om = message["Message"]


def ekeys():
    print('\033[1m' + 'Details of the Keys' + '\033[0m')
    print("Private Key: ", d)
    print("Common Modulus: ", n)
    print("Random Symmetric Key: ", key)
    print()


def emessages():
    print('\033[1m' + 'Details of the Messages' + '\033[0m')
    print("Encrypted Message: ", em)
    print("Encrypted Key: ", ek)
    print("Original Message: ", om)
    print()


def keydecryption(ekey, dp):
    print('\033[1m' + 'Decryption of the Key Using Asymmetric Algorithm' + '\033[0m')
    print("Starting the Decryption Process")
    Dk = pow(ekey, dp, n)
    print("The Decrypted Key is: ", Dk)
    print()
    return {"Decrypted Key": Dk}


def messagedecryption(em, Dk):
    print('\033[1m' + 'Decryption of the Message using Symmetric Algorithm' + '\033[0m')
    print('Starting the Decrypting Process.....')
    ide = em ^ Dk
    print('Applying the XOR Operation')
    ide1 = bin(ide)
    print('After applying XOR Operation: ', ide1)
    print('Value after applying Xor Operation is: ', ide)
    mes3 = int(ide1, 2) >> 1
    print('Applying the Right Shift Operation on Message')
    mes4 = bin(mes3)
    print('After applying Right Shift Operation: ', mes4)
    print('Value after applying Right Shift Operation is: ', mes3)
    print()
    print('Decrypted Message is: ', mes3)
    return {"Decrypted Message": mes3}


ekeys()
emessages()
dk = keydecryption(ek, d)
dm = messagedecryption(em, key)

print('\033[1m' + 'DIGITAL ENVELOPE' + '\033[0m')
print("Opening the Digital Envelope")
saveVal = {"Decrypted Key": dk, "Decrypted Message": dm}
print(saveVal)
saveFile = open("Opened_Digital_Envelope.txt", "wt")
saveFile.write(json.dumps(saveVal))
saveFile.close()
print("Digital Envelope Opened")
print('NOTE: Here all the values are automatically generated')
