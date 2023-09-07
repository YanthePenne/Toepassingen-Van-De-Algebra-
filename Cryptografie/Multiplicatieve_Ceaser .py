import math

# Multiplicatief Ceaser
"""
Beschrijving: 
    Ceasar Encrypte maar met vermenigvuldiging. 

Input: 
    phrase      = [int]
    key         = int 
    m = modulo  = int 

Output: [1,2,3]
    Encrypt hf.mod(phrase * key, m)
    Decrypt hf.mod(phrase * hf.modulo_inverse(key), m)
"""


def modulo_times(x, times, m):
    return mod(x*times, m)


def mod(a, m):
    return a % m


def encrypt_mCeasar_algorithm(phrase, key, m):
    result = []
    for i in phrase:
        integer = int(i)
        print(i)
        result.append(modulo_times(integer, key, m))

    return result


def decrypt_mCeasar_algorithm(phrase, reverse_key, m):
    return [modulo_times(i, reverse_key, m) for i in phrase]


phrase = input("pharse: ")
key = int(input("key: "))
m = int(input("m: "))
print(decrypt_mCeasar_algorithm(phrase, key, m))


def modulo_times(x, times, m):
    return mod(x*times, m)


def mod(a, m):
    return a % m
