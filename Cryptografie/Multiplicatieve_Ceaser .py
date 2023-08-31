import Modulus as hf
# Multiplicatief Ceaser
"""
Beschrijving: 
    Ceasar Encrypte maar met vermenigvuldiging. 

Input: 
    phrase      = [int]
    key         = int 
    m = modulo  = int 

Output: 
    Encrypt hf.mod(phrase * key, m)
    Decrypt hf.mod(phrase * hf.modulo_inverse(key), m)
"""


def encrypt_mCeasar_algorithm(phrase, key, m):
    return [hf.modulo_times(i, key, m) for i in phrase]


def decrypt_mCeasar_algorithm(phrase, reverse_key, m):
    return [hf.modulo_times(i, reverse_key, m) for i in phrase]
