import os
os.system("cls m|| clear")

QUANTIDADE_NUMEROS = 5
maior_numero = 0
menor_numero = 0
quantidade_pares = 0
quantidade_impares = 0
quantidade_positivos = 0
quantidade_negativos = 0

# Variáveis para armazenar os números.
for i in range(QUANTIDADE_NUMEROS):
    numero = int(input(f"Digite o {i+1}º número: "))

    if numero % 2 == 0:
        quantidade_pares += 1
    else: 
        quantidade_impares +=1
    if numero < 0:
        quantidade_negativos +=1
    else:
        quantidade_positivos +=1

        maior_numero = max(maior_numero, numero)
        menor_numero = min(menor_numero, numero)