import random as rn
import sympy as sp
import math


def rsa():
    global n, d
    p = sp.randprime(1, 100000)
    print('The Prime Number P is: ', p)
    q = sp.randprime(1, 100000)
    print('The Prime Number Q is: ', q)
    dn = (p - 1) * (q - 1)
    print('The Value of pi(n) is: ', dn)
    n = p * q
    print('The Value of N(common modulus) is: ', n)

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


def blind_sign(m, r):
    print('\033[1m' + 'Blind Signature Algorithm' + '\033[0m')
    print("Starting the Encryption and Decryption Process")
    print()
    print("The Message Value is: ", m)
    print("The Random Number Generated is: ", r)
    print()
    print('\033[1m' + 'Using RSA Algorithm for Key Generation' + '\033[0m')
    rsa()
    print('\033[1m' + 'Sharing of the Public Key from Signer to User' + '\033[0m')
    bf = pow(r, e, n)
    print('The Blind Factor is: ', bf)
    bm = (pow(r, e) * m) % n
    print('The Blinded Message is: ', bm)
    print("Sign Generation done by the Signer")
    sg = pow(bm, d, n)
    print("The Generated Sign is: ", sg)
    print("Sign Verification done by the User")
    sv1 = pow(r, -1, n)
    sv2 = sg * sv1
    sv = pow(sv2, e, n)
    print("The Verified Sign Value is: ", sv)
    if sv == m:
        print('\033[1m' + 'The Sign is True' + '\033[0m')
        print()
    else:
        print('\033[1m' + 'The Sign is False' + '\033[0m')
        print()
    print('The Value of Decrypted/Original Message is: ', sv)
    print('NOTE: Here all the values are automatically generated')


message = rn.getrandbits(10)
random = rn.getrandbits(10)
blind_sign(message, random)
