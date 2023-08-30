import math
# Modulus a mod m = y
""" 
Rest bij deling 
m = a * x + y 
mod(a, m) = y 
relatief priem als mod(a, m) = 0
"""


def mod(a, m):
    return a % m

# Modulo Calculations


def modulo_times(x, times, m):
    return mod(x*times, m)


def modulo_plus(left_term, right_term, m):
    return mod(left_term + right_term, m)


def modulo_min(left_term, right_term, m):
    return mod(left_term - right_term, m)


# Modulo Inverse
"""
input = int, modulo
return: False if no Inverse 
        int = inverse
"""


def modulo_inverse(number, m):
    for b in range(1, m):
        if mod(number * b, m) == 1:
            return b
    return False


# Modulo of an exponential number
"""
Rest bij deling van een exponentieel getal 
modulo_exp(a, x, m) = 
a^x modulus m = y
m = a^x + y 
Inverse: 
Relatief Priem: 
Cyclisch: 
"""


def modulo_exp(a, x, m):
    return mod(pow(a, x), m)


# Modulo of an logaritmic number
"""
Rest bij deling van een exponentieel getal 
modulo_exp(a, x, m) = 
log(a) modulus m = y
m = log(a)*x + y 
"""


def modulo_log(a, m):
    return int(mod(math.log(a, 2), m))
