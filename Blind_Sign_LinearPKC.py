import random as rn
import sympy as sp


def asymmetric_key():
    global e, n, d, q
    print()
    print('Starting the Process of Public and Private Key Generation')
    p = sp.randprime(1, 1000)
    a = rn.randint(1, 1000)
    b = rn.randint(1, 1000)
    m = a * b - p
    print('The Value of M is: ', m)
    e = (p * m) + a
    print('The Value of E is: ', e)
    d = (p * m) + b
    print('The Value of D is: ', d)
    n = int((e * d - p)/m)
    print('The Value of N (Common Modulus) is: ', n)
    print('Applying the Inverse Modulus Operation')
    t = pow(p, -1)
    q = pow(p, -1, n)
    print('The Value of Q is: ', q)
    q1 = (q * e * d) % n
    print('Checking the Proof (Q*E*D)%N: ', q1)
    print()


def blind_sign(m, r):
    print('\033[1m' + 'Blind Signature Algorithm' + '\033[0m')
    print("Starting the Encryption and Decryption Process")
    print()
    print("The Message Value is: ", m)
    print("The Random Number Generated is: ", r)
    print()
    print('\033[1m' + 'Using Linear RSA-PKC Algorithm for Key Generation' + '\033[0m')
    asymmetric_key()
    print('\033[1m' + 'Sharing of the Public Key from Signer to User' + '\033[0m')
    bf = (r * m) % n
    print('The Blind Factor is: ', bf)
    bm = (bf * e) % n
    print('The Blinded Message is: ', bm)
    print("Sign Generation done by the Signer")
    sg = (bm * q * d) % n
    print("The Generated Sign is: ", sg)
    print("Sign Verification done by the User")
    sv1 = pow(r, -1)
    sv2 = (sg * sv1) % n
    print("The Verified Sign Value is: ", int(sv2))
    if sv2 == m:
        print('\033[1m' + 'The Sign is True' + '\033[0m')
        print()
    else:
        print('\033[1m' + 'The Sign is False' + '\033[0m')
        print()
    print('The Value of Decrypted/Original Message is: ', int(sv2))
    print('NOTE: Here all the values are automatically generated')


message = rn.getrandbits(10)
random = rn.getrandbits(10)
blind_sign(message, random)
