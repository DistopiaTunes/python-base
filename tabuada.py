#!/usr/bin/env python3
"""Imprime a tabuada do 1 ao 10.

---Tabuada do 1---

        1 x 1 = 1
        2 x 1 = 2
        3 x 1 = 3
...
##############
---Tabuada do 2---

        1 x 2 = 2
        2 x 2 = 4
...
#############

"""
__version__ = "0.1.1"
__author__ = "raphael"


# numeros = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

numeros  = list(range(1, 11))

# Iterable (percorríveis) (corre a lista)

#para cada "numero" dentro da sequência "numeros":
for n1 in numeros:
    print("{:🔷^25}".format(f" Tabuada do {n1} "))
    print()
    for n2 in numeros:
        resultado = n1 * n2
        print ("{:^35}".format(f"{n1:02d} x {n2:02d} = {resultado:03d}"))
    print() 

    print("\U00002600" * 35 )
    print()
