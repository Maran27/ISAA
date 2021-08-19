import random as rn
import sympy as sp
import math


def rsa(m):
    print('\033[1m' + 'RSA Algorithm' + '\033[0m')
    print("Starting the Encryption and Decryption Process")
    print()
    print("The Message Value is: ", m)
    print()
    print('\033[1m' + 'Generation of Public and Private Keys' + '\033[0m')
    p = sp.randprime(1, 100000)
    print('The Prime Number P is: ', p)
    q = sp.randprime(1, 100000)
    print('The Prime Number Q is: ', q)
    n = p * q
    print('The Value of N(common modulus) is: ', n)
    dn = (p - 1) * (q - 1)
    print('The Value of pi(n) is: ', dn)

    def ev():
        global e
        e = rn.getrandbits(10)
        if 1 < e < dn and math.gcd(e, dn) == 1:
            print("The Public Key is: ", e)
        else:
            ev()
    ev()
    d = pow(e, -1, dn)
    print("The Private Key is: ", d)
    v = (d*e) % dn
    print("The Proof Verification of (D*E)%pi(n) is: ", v)
    print()
    print("Starting the Encryption Process")
    CM = pow(m, e, n)
    print("The Encrypted Message is: ", CM)
    print()
    print("Starting the Decryption Process")
    DM = pow(CM, d, n)
    print("The Decrypted Message is: ", DM)
    print('NOTE: Here all the values are automatically generated')


message = rn.randint(1, 100)
rsa(message)
