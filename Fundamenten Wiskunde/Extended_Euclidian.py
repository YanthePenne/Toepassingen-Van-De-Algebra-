
# Extended Euclidian Algorithm
"""
Beschrijving: 
    Toegevoegde Extended Euclidian Algorithm.
    d = gcd(a, b) = alf a *a + beta * b. 

Input:
    extended_gcd(number1, number2)
    a > b
Output: 
    20 = 4 * 5
    15 = 3 * 5
    d = gcd(20,15) = 5
    d = a * number1 + b * number2 
    
"""
def extended_gcd(a, b):
     r = [] 
     if a > b: 
        r.append(a)
        r.append(b)
        number1 = a 
        number2 = b
     else: 
        r.append(b)
        r.append(a)
        number1 = b 
        number2 = a
     alfa = [] 
     alfa.append(1)
     alfa.append(0)

     beta = []
     beta.append(0)
     beta.append(1) 
    
     i = 1
     while r[i] != 0: 
         i = i + 1 
         q = r[i-2]/r[i - 1]
         r.append(r[i-2] - q * r [i - 1])
         alfa.append(alfa[i-2] - q * alfa[i - 1])
         beta.append(beta[i-2] - q * beta[i - 1])
        
     result = alfa[i-1] * number1  - beta[i-1] * number2
     return ( f"{result % number1} = {alfa[i-1]} * {number1} - {beta[i-1]} * {number2}")
    
      

   
    
