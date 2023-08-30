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
    
        r = []
        r.append(a)
        r.append(b)

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
            r.append(int(r[i-2] - q*r[i-1]))
            alfa.append(int(alfa[i-2] - q * alfa[i - 1])) 
            beta.append(int(beta[i-2] - q * beta[i - 1]))
    
        return f"{ea.gcd(a,b)} = {alfa[i]} * {a} + {beta[i]} * {b}"
    

   
    
a = int(input("Number 1: "))
b = int(input("Number 2: "))
print(extended_gcd(a,b))