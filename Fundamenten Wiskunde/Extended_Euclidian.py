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
    # d = ea.gcd(a, b)
    r0 = a
    a0 = 1
    b0 = 0

    r1 = b
    a1 = 0 
    b1 = 1
  
    
    while r1 != 0: 
        q = r0/r1
        r0 = r1
        r1 = r0 - q*r1
        a1 = a0 - q*a1 
        b1 = b0 - q*b1

    return print(f"{r1} = {a1} * {a} + {b1} * {b}")


print(extended_gcd(int(input("Number1: ")), int(input("Number2: "))))
