# Algorithm van Luhn
"""
Beschrijving:

1. Neem je eigen bankkaart en bekijk het kaartnummer. Negeer voorlopig het laatste cijfer. (Het reeksnummer N8 geeft aan dat dit de negende kaart, dit negeer je ook.)
2. Neem je smartphone, open het rekentoestel en tel alle cijfers op de oneven posities op.
(Op de kaart rechts dus 6+0+6+2+4+1+9+2)
3. Vervolgens verdubbel je elk cijfer op de even posities; indien het resultaat strikt groter is dan 9 dan trek je er 9 van af. Tel al deze getallen bij het vorige resultaat op.
4. Vermenigvuldig het bekomen getal met 9. Neem het laatste cijfer van dit getal en trek hier tenslotte het laatste cijfer van je bankkaartnummer (dat je tot dusver moest negeren) van af.

Input: 
    Card Number = Int 
Ouput: 
    Valid or Not
"""


def luhn_formule(int_card_no):
    lst_card_no = [int(i) for i in str(int_card_no)]
    last = len(lst_card_no) - 1

    lst_odd = []
    lst_even = []

    """
    Step 1:  
        Neem je eigen bankkaart en bekijk het kaartnummer.
        Negeer voorlopig het laatste cijfer.
        (Het reeksnummer N8 geeft aan dat dit de negende kaart, dit negeer je ook.)
    """
    for x in range(0, last - 1):
        lst_odd.append(lst_card_no[x*2 + 1])
        lst_even.append(lst_card_no[x*2])

    """  
    Step 2 : 
        Neem je smartphone, open het rekentoestel en tel alle cijfers op de oneven posities op.
        (Op de kaart rechts dus 6+0+6+2+4+1+9+2)
    """
    int_sum_odd = sum(lst_odd)

    """
    Step 3:
        Vervolgens verdubbel je elk cijfer op de even posities, 
        indien het resultaat strikt groter is dan 9 dan trek je er 9 van af. 
        Tel al deze getallen bij het vorige resultaat op. (int_sum_odd)
    """
    int_sum_even = sum([double_mod9(i) for i in lst_even])

    """
    step 4
        Vermenigvuldig het bekomen getal met 9. 
        Neem het laatste cijfer van dit getal en trek hier tenslotte 
        het laatste cijfer van je bankkaartnummer 
        (dat je tot dusver moest negeren) van af.
    """
    lst_result = [int(i) for i in str(9*(int_sum_odd + int_sum_even))]
    int_result_last = lst_result[len(lst_result) - 1]

    valid = (int_result_last - lst_card_no[last]) == 0
    return valid


# Help Functions
"""
Beschrijving: 


Input: 




Output: 




"""


def double_mod9(int):
    return (2 * int) % 9


int_card_no = int(input("What is your card number?: "))
print(luhn_formule(int_card_no))
