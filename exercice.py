#!/usr/bin/env python
# -*- coding: utf-8 -*-


from typing import List


def convert_to_absolute(number: float) -> float:
    if number < 0:
     number = -number
    return number

def use_prefixes() -> List[str]:
    prefixes, suffixe = 'JKLMNOPQ', 'ack'
    liste_nom = []
    for pre in prefixes:
        liste_nom.append(pre + suffixe)
    return liste_nom


def prime_integer_summation() -> int:
    sum = 0
    number = 2
    count = 0
    while count < 100:
        i = 2
        if i == number:
            sum += number
        while i < number:
            if number % i !=0:
                i += 1
            sum += number
        count += 1
    return sum
    #faux rep: 24133


def factorial(number: int) -> int:
    i = 1
    fact = 1
    while i <= number:
        fact = fact * i
        i += 1
    return fact


def use_continue() -> None:
    x = (1, 2, 3, 4, 5, 6, 7, 8, 9, 10)
    for i in range(0, len(x)):
        if x[i] == 5:
            continue
        print(x[i])


def verify_ages(groups: List[List[int]]) -> List[bool]:
    etat_groupes = [True] * len(groups)
#critère de taille
    i = 0
    while i < len(groups):
        if 4 > len(groups[i]):
            etat_groupes[i] = False
        elif 10 < len(groups[i]):
            etat_groupes[i] = False
#critères d'âge
        elif 25 in groups[i]:
            pass
        else:
            x = 0
            while x < len(groups[i]) and etat_groupes[i] is True:
                if 18 > groups[i][x]:
                    etat_groupes[i] = False
                if 50 in groups[i]:
                    if groups[i][x] > 70:
                        etat_groupes[i] = False
                x += 1
        i += 1
    return etat_groupes

def main() -> None:
    number = -4.325
    print(f"La valeur absolue du nombre {number} est {convert_to_absolute(number)}")

    print(f"La liste des noms générés avec les préfixes est: {use_prefixes()}")

    print(f"La somme des 100 premiers nombre premier est : {prime_integer_summation()}")

    number = 10
    print(f"La factiorelle du nombre {number} est: {factorial(number)}")
    
    print(f"L'affichage de la boucle est:")
    use_continue()

    groups = [
        [15, 28, 65, 70, 72], [18, 24, 22, 50, 70], [25, 2],
              [20, 22, 23, 24, 18, 75, 51, 49, 100, 18, 20, 20], [70, 50, 26, 28], [75, 50, 18, 25],
              [13, 25, 80, 15], [20, 30, 40, 50, 60], [75, 50, 100, 28]
    ]
    print(f"Les différents groupes sont: {groups}")
    print(f"L'acceptance des groupes est: {verify_ages(groups)}")


if __name__ == '__main__':
    main()
