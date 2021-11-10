import random as rn
from Crypto.Util import number
import math


def gcd(x, y):
    while y:
        x, y = y, x % y
    return x


def rsa(m):
    print('\033[1m' + 'RSA Algorithm' + '\033[0m')
    print("Starting the Encryption and Decryption Process")
    print()
    print("The Message Value is: ", m)
    print()
    print('\033[1m' + 'Generation of Public and Private Keys' + '\033[0m')
    p = number.getPrime(10)
    print('The Prime Number P (1024-bit) is: ', p)
    q = number.getPrime(10)
    print('The Prime Number Q (1024-bit) is: ', q)
    n = pow(p, 2) * q
    print('The Value of N(common modulus) (2048-bit) is: ', n)
    dn = math.lcm(p - 1, q - 1)
    print("The LCM Value is: ", dn)
    d = pow(n, -1, dn)
    print("The Private key D is: ", d)
    c = pow(m, n, n)
    print("Enc: ", c)
    m1 = pow(c, d, p*q)
    print("message: ", m1)


message = rn.getrandbits(10)
rsa(message)
