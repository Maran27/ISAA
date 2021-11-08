import random as rn
from Crypto.Util import number


# Euclidean Algorithm
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
    p = number.getPrime(1024)
    print('The Prime Number P (1024-bit) is: ', p)
    q = number.getPrime(1024)
    print('The Prime Number Q (1024-bit) is: ', q)
    n = p * q
    print('The Value of N(common modulus) (2048-bit) is: ', n)
    dn = (p - 1) * (q - 1)
    print('The Value of pi(n) is: ', dn)
    e = rn.getrandbits(20)
    while e < dn:
        if gcd(e, dn) == 1:
            break
        else:
            e += 1

    t = 2
    while (1 + (t * dn)) % e != 0:
        t += 1
    d = int((1 + (t * dn)) // e)
    print("The Public Key is: ", e)
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


message = rn.getrandbits(100)
rsa(message)
