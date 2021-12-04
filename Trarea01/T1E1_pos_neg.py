"""
Date:       2021-11-23
Authors:    Orlando Miguel Laguna Zuñiga
File:       T1E1_pos_neg.py
Brief:      Programa que pide al usuario un número e indica si este es: 
            positivo, negativo o igual a cero
Score:      35
Version:    0.1.1
Fixes:      - Falta la condición de __main__

            - PEP8 recomienda añadir espacios en blanco alrededor de
                los operadores
            
            - El programa no funciona cuando el número es cero, si te 
                atoras mucho puedes apoyarte con tu compañero de equipo 
                o mandarme whats para organizar un meet extra de la 
                clase
"""

num=int(input("ingresar numero:"))  # PEP8

if num>=1:                          # PEP8
    print("Numero es positivo")

else:
    print("Numero negativo")

    # AQUI ESTAS ASIGNANDO DEBERIAS COMPARAR CON EL OPERADOR ==
    # Y ADEMAS DEBERIA ESTAR ENTRE EL if Y EL else, USANDO elif
    num=0                           # PEP8
    print("El numero es 0")         # SIEMPRE IMPRIME CERO SI ES NEGATIVO, ESO ESTA MAL
