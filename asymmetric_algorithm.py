import random as rn
from Crypto.Util import number


def asymmetric_key(m1):
    print('\033[1m' + 'Asymmetric Algorithm - Linear PKC' + '\033[0m')
    print("Starting the Encryption and Decryption Process")
    print()
    print('The Original Message is: ', m1)
    print()
    print('Starting the Process of Public and Private Key Generation')
    mes = number.getPrime(20)
    print("The Prime Number Generated is: ", mes)
    a = number.getPrime(1024)
    print("The Value of A (1024-bits) is: ", a)
    b = number.getPrime(1024)
    print("The Value of B (1024-bits) is: ", b)
    m = a * b - mes
    print('The Value of M (2048-bits) is: ', m)
    e = m + a
    print('The Value of E (2048-bits) is: ', e)
    d = m + b
    print('The Value of D (2048-bits) is: ', d)
    n = int((e * d - mes)//m)
    print('The Value of N (2048-bits) is: ', n)
    print('Applying the Inverse Modulus Operation')
    q = pow(mes, -1, n)
    print('The Value of Q is: ', q)
    q1 = (q * e * d) % n
    print('Checking the Proof (Q*E*D)%N: ', q1)
    print()
    print("Starting the Encryption Process...")
    en = (m1 * e) % n
    print('The Encrypted Value is: ', en)
    print()
    print("Starting the Decryption Process...")
    de = (en * q * d) % n
    print('The Decrypted Value is: ', de)
    print()
    print('The Value of Decrypted Message is: ', de)
    print('NOTE: Here all the values are automatically generated')


message = rn.getrandbits(10)
asymmetric_key(message)
