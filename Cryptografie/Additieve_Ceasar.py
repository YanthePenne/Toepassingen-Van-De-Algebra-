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

    Encrypt hf.mod(phrase + key, m)
    Decrypt hf.mod(phrase - key, m)

"""


def encrypt_aCeasar_algorithm(phrase, key, m):
    return [hf.modulo_plus(i, key, m) for i in phrase]


def decrypt_aCeasar_algorithm(phrase, key, m):
    return [hf.modulo_min(i, key, m) for i in phrase]
