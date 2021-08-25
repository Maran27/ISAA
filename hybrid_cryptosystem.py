import random as rn
import sympy as sp

message = rn.getrandbits(10)


def hybrid_key():
    print('\033[1m' + 'A HYBRID CRYPTO-SYSTEM' + '\033[0m')
    print("Starting the Encryption and Decryption Process")
    print()
    print('\033[1m' + '...Starting the process of Key generation for Symmetric Encryption and Decryption...' + '\033[0m')
    global key, mes, a, b, e, d, n, q, y, sk
    key = rn.getrandbits(10)
    print("Key for Symmetric Encryption and Decryption: ", key)
    print()
    print('\033[1m' + '...Starting the Process of Public and Private Key Generation for Asymmetric Encryption and '
                      'Decryption...' + '\033[0m')
    mes = sp.randprime(1, 10000)
    a = rn.randint(1, 10000)
    b = rn.randint(1, 10000)
    m = a * b - mes
    print('The Value of M is: ', m)
    e = m + a
    print('The Value of E is: ', e)
    d = m + b
    print('The Value of D is: ', d)
    n = int((e * d - mes) / m)
    print('The Value of N (Common Modulus) is: ', n)
    print('Applying the Inverse Modulus Operation')
    q = pow(mes, -1, n)
    print('The Value of Q is: ', q)
    print()
    print('\033[1m' + '...Starting the process of secret key and number for Intelligent Cryptography...' + '\033[0m')
    y = rn.getrandbits(5)
    print('The Random number is: ', y)
    sk = rn.getrandbits(5)
    print('The Secret Key is: ', sk)
    print()


def hybrid_encryption(mes):
    print('\033[1m' + '...The Message...' + '\033[0m')
    m2 = bin(mes)
    print('The Original Message is: ', mes)
    print('The Binary Value of Original Message is: ', m2)
    print()
    global mes1, en, en2, r, d1, e1
    print('\033[1m' + '...Starting the Symmetric Encryption Process...' + '\033[0m')
    mes1 = mes << 1
    print('Applying the Left Shift Operation on Message')
    mes2 = bin(mes1)
    print('After Applying Shift Operation: ', mes2)
    print('After Applying Shift Operation Value is: ', mes1)
    en = mes1 ^ key
    print('Applying the XOR Operation')
    en1 = bin(en)
    print('After applying XOR operation: ', en1)
    print('Value after applying XOR operation is: ', en)
    print()
    print('\033[1m' + '...Starting the Asymmetric Encryption Process...' + '\033[0m')
    en2 = (en * e) % n
    en3 = bin(en2)
    print('The Binary Value of Encrypted Value is: ', en3)
    print('The Encrypted Value is: ', en2)
    print()
    print('\033[1m' + '...Intelligent Encryption...' + '\033[0m')
    r = en2 - y
    r1 = bin(r)
    print('After Subtracting D-C: ', r1)
    print('Value After Subtracting D-C: ', r)
    print('Applying XOR Operation')
    d1 = r ^ sk
    d2 = bin(d1)
    print('After Applying XOR Operation R XOR K: ', d2)
    print('Value After Applying R XOR K: ', d1)
    e1 = y ^ sk
    e2 = bin(e)
    print('After Applying XOR Operation C XOR K: ', e2)
    print('Value after applying C XOR K: ', e1)
    print()


def hybrid_decryption():
    print('\033[1m' + '...Starting Intelligent Decryption...' + '\033[0m')
    de = e1 ^ sk
    de1 = bin(de)
    print('After Applying XOR Operation EN XOR K: ', de1)
    print('Value after applying EN XOR K: ', de)
    dd = d1 ^ sk
    dd1 = bin(dd)
    print('After applying XOR Operation EN1 XOR K: ', dd1)
    print('Value After applying EN1 XOR K: ', dd)
    dc = de + dd
    dc1 = bin(dc)
    print('After Adding DE + DE1: ', dc1)
    print('Value after adding DE + DE1 is: ', dc)
    print()
    print('\033[1m' + '...Starting Asymmetric Decryption...' + '\033[0m')
    da1 = (dc * q * d) % n
    da2 = bin(da1)
    print('The Binary Value of Decrypted Value is: ', da2)
    print('The Decrypted Value is: ', da1)
    print()
    print('\033[1m' + '...Starting Symmetric Decryption...' + '\033[0m')
    ide = da1 ^ key
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


hybrid_key()
hybrid_encryption(message)
hybrid_decryption()
