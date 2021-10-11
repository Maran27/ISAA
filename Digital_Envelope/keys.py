import random as rn
import sympy as sp
import math
import json


def rsa():
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
    return {"Public Key Pair": {"N": n, "E": e}, "Private Key": {"D": d}}


def symmetric_key():
    print('\033[1m' + 'Symmetric Key Generation' + '\033[0m')
    key = rn.getrandbits(10)
    print("the symmetric key is: ", key)
    print()
    return {"Symmetric Key": key}


rsa = rsa()
skey = symmetric_key()

print('\033[1m' + 'KEYS FOR THE DIGITAL ENVELOPE' + '\033[0m')
print("Storing the Keys Generated")
keys = {"Public and Private Key": rsa, "Random Symmetric Key": skey}
print(keys)
saveFile = open("keys.txt", "wt")
saveFile.write(json.dumps(keys))
saveFile.close()
print("Stored the Keys")
print('NOTE: Here all the values are automatically generated')
