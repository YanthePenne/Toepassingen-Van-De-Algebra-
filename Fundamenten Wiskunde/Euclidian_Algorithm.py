import Modulus as hf

# Euclidian Algorithm

"""
Beschrijving: 
    Grootste gemeenschappelijke deler. 

Input:
    gcd(number1, number2)

Step:
    gcd(number2, mod(number1, number2))
    
Output: 
    20 = 4 * 5
    15 = 3 * 5
    gcd(20,15) = 5
    
"""


def gcd_algorithm(a, b):
    if (b == 0):
        return abs(a)
    else:
        return gcd_algorithm(b, hf.mod(a, b))


a = int(input("Number 1: "))
b = int(input("Number 2: "))
print(gcd_algorithm(a, b))
