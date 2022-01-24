"""
Date:       2021-11-23
Authors:    Orlando Laguna Zuñiga
File:       T1E2_even_odd.py
Brief:      Ingresar un número y validar si es par o impar.
Score:      60+
Versión:    0.2.1
Fixes:      - Falta la condición de __main__

            - PEP8 recomienda añadir espacios en blanco alrededor de
                los operadores
            
            - PEP8 recomienda que la sangría sea un múltiplo de 4 
                espacio
"""

num1 = int(input("Digite un numero:"))


if num1%2==0:
  print("El numero es par")
elif num1%2==0:
  print(f"{num1} el numero es par")

else:
  print("El numero es impar")
  
