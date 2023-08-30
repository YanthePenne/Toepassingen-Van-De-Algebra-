import Modulus as m
import Euclidian_Algorithm as ea
# Extended Euclidian Algorithm

"""
Beschrijving: 
    Toegevoegde Extended Euclidian Algorithm.
    d = gcd(a, b) = alf a *a + beta * b. 

Input:
    extended_gcd(number1, number2)

Output: 
    20 = 4 * 5
    15 = 3 * 5
    d = gcd(20,15) = 5
    d = a * number1 + b * number2 
    
"""
def extended_gcd(a, b): 
    d = ea.gcd(a, b)
    alfa = 
    beta = 

    print(f"{d} = {alfa} * {a} + {beta} * {b}")