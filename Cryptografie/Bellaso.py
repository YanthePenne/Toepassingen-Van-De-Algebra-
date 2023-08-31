import Modulus as hf
# Bellaso
"""
Beschrijving: 
    Ceasar Encryptie met een passkey. 

Input:
    phrase      = [int]
    pass_key    = [int]
    m = modulo  = int

Output: 
    Encrypt mod(phrase[i] + pass_key[mod(i, len)] , m)
    Decrypt mod(phrase[i] - pass_key[mod(i, len)] , m)
"""


def encrypt_Bellaso_algorithm(phrase, pass_key, m):
    result = []
    for i in range(0, len(phrase) - 1):
        result.append(hf.modulo_plus(
            phrase[i], pass_key[i % len(pass_key)], m))
    return result


def encrypt_Bellaso_algoritm(phrase, pass_key, m):
    result = []
    for i in range(0, len(phrase) - 1):
        result.append(hf.modulo_min(phrase[i], pass_key[i % len(pass_key)], m))
    return result
