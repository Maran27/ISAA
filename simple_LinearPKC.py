import random as rn
import sympy as sp


def asymmetric_key(m1):
    print('\033[1m' + 'Asymmetric Algorithm - Linear PKC' + '\033[0m')
    print("Starting the Encryption and Decryption Process")
    print()
    print('Starting the Process of Public and Private Key Generation')
    mes = sp.randprime(1, 10000)
    a = rn.randint(1, 10000)
    b = rn.randint(1, 10000)
    m = a * b - mes
    print('The Value of M is: ', m)
    e = m + a
    print('The Value of E is: ', e)
    d = m + b
    print('The Value of D is: ', d)
    n = int((e * d - mes)/m)
    print('The Value of N (Common Modulus) is: ', n)
    print('Applying the Inverse Modulus Operation')
    q = pow(mes, -1, n)
    print('The Value of Q is: ', q)
    q1 = (q * e * d) % n
    print('Checking the Proof (Q*E*D)%N: ', q1)
    print()
    m2 = bin(m1)
    print('The Original Message is: ', m1)
    print('The Binary Value of Original Message is: ', m2)
    print()
    print("Starting the Encryption Process...")
    en = (m1 * e) % n
    en1 = bin(en)
    print('The Binary Value of Encrypted Value is: ', en1)
    print('The Encrypted Value is: ', en)
    print()
    print("Starting the Decryption Process...")
    de = (en * q * d) % n
    de1 = bin(de)
    print('The Binary Value of Decrypted Value is: ', de1)
    print('The Decrypted Value is: ', de)
    print()
    print('The Value of Decrypted Message is: ', de)
    print('NOTE: Here all the values are automatically generated')


message = rn.getrandbits(5)
asymmetric_key(message)