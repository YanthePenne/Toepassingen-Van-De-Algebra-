import math
# Congruence Solver
"""
Beschrijving:

    Solves a congruence equation a*x = e mod m
    Given a, e, m 
    Solves x 

Input:

    congruentie (a, e, m)

Output: 

    x  
"""


def congruentie(a, e, m):
    # ax = e mod m
    checker = math.gcd(a, m) == 1
    if checker:
        for i in range(0, m):
            solution = (a * i) % m == e % m
            if solution:
                return i