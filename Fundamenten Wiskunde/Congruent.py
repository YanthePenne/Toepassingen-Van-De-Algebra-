import math


# Congruence Solver (Brute Force)
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


def congruence_algorithm(a, e, m):
    # ax = e mod m
    # Coprime
    checker = math.gcd(a, m) == 1

    if checker:
        for i in range(0, m):
            solution = (a * i) % m == e % m
            if solution:
                return i

    return False
