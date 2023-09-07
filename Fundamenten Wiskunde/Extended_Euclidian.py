
# Extended Euclidian Algorithm
"""
Beschrijving: 
    Toegevoegde Extended Euclidian Algorithm.
    d = gcd(a, b) = alf * a + beta * b. 

Input:
    extended_gcd(number1, number2)
    a > b
Output: 
    20 = 4 * 5
    15 = 3 * 5
    d = gcd(20,15) = 5
    d = a * number1 + b * number2 
    
"""


def ee_algorithm(a, b):
    # 1 Stel r[0] = alfa[0] * a + beta[0] * b
    # 2 Stel r[1] = alfa[1] * a + beta[1] * b
    # 3 alfa[0] = 1, beta[0] = 0, alfa[1] = 0, beta[1] = 1
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

    # 4 Stel i = 1
    i = 1
    # 5 Zolang r[i] != 0, doe het volgende:
    while r[i] != 0:
        # 6 Verhoog de waarde i met 1
        i = i + 1
        # 7 Bereken q
        q = r[i-2]/r[i - 1]
        # 8 Bereken r[i], alfa[i], beta[i]
        r.append(r[i-2] - q * r[i - 1])
        alfa.append(alfa[i-2] - q * alfa[i - 1])
        beta.append(beta[i-2] - q * beta[i - 1])

    # 9 Bezout's Identity
    result = alfa[i-1] * number1 - beta[i-1] * number2
    return (f"{result % number1} = {alfa[i-1]} * {number1} - {beta[i-1]} * {number2}")


a = int(input("a: "))
b = int(input("b: "))
print(ee_algorithm(a, b))
