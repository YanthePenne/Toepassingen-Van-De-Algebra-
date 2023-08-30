import Modulus as hf

# Additief Ceaser
"""
Beschrijving: 
    (x+a) mod n) - a mod n = x

Input:
    phrase      = [int]
    key         = int 
    m = modulo  = int 

Output: 
    Encrypt 
    Decrypt
"""


def encrypt_aCeasar(phrase, key, m):
    return [hf.modulo_plus(i, key, m) for i in phrase]


def decrypt_aCeasar(phrase, key, m):
    return [hf.modulo_min(i, key, m) for i in phrase]
