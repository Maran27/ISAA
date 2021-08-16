import random as rn


def symmetric_key(m, k):
    print('\033[1m' + 'Symmetric Algorithm' + '\033[0m')
    print("Starting the Encryption and Decryption Process")
    print()
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
    en = mes1 ^ k
    print('Applying the XOR Operation')
    en1 = bin(en)
    print('After applying XOR operation: ', en1)
    print('Value after applying XOR operation is: ', en)
    print()
    op = input("Do you wan to decrypt the Message [y/n]?")
    if op.lower() == 'y':
        print()
        print('Starting the Decrypting Process.....')
        ide = en ^ k
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
        print('NOTE: Here all the values are automatically generated')


message = rn.getrandbits(10)
key = rn.getrandbits(10)

symmetric_key(message, key)
