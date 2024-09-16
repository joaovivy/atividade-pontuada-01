import os
os.system("cls || clear")

# Variáveis para armazenar os números.
lista_numeros = []
quantidade_pares = 0
quantidade_impares = 0
quantidade_positivos = 0
quantidade_negativos = 0
maior_numero = 0
menor_numero = 0
soma_pares = 0
soma_impares = 0
soma_geral = 0
total_numeros = 0

# Variável para armazenar os números.
print("\n=== Solicitando dados ===")
for i in range(5):
    numero = int(input(f"Digite o {i+1}º número: "))
    lista_numeros.append(numero)

    if numero % 2 == 0:
        quantidade_pares += 1
        soma_pares += numero
    else:
        quantidade_impares += 1
        soma_impares += numero

    if numero < 0:
        quantidade_negativos += 1
    else: 
        quantidade_positivos += 1

    soma_geral += numero

total_numeros += numero
maior_numero = max(lista_numeros)
menor_numero = min(lista_numeros)

# Calculando as médias
media_pares = soma_pares / quantidade_pares if quantidade_pares > 0 else 0
media_impares = soma_impares / quantidade_impares if quantidade_impares > 0 else 0
media_geral = soma_geral / 5

# Imprimindo as estatísticas
print("\n=== Estatísticas dos números ===")
print(f"Quantidade de pares: {quantidade_pares}")
print(f"Quantidade de ímpares: {quantidade_impares}")
print(f"Quantidade de positivos: {quantidade_positivos}")
print(f"Quantidade de negativos: {quantidade_negativos}")
print(f"Quantidade de números inseridos: {total_numeros}")
print(f"Maior número: {maior_numero}")
print(f"Menor número: {menor_numero}")
print(f"Soma geral: {soma_geral}")
print(f"Média dos números pares: {media_pares:.2f}")
print(f"Média dos números ímpares: {media_impares:.2f}")
print(f"Média de todos os números: {media_geral:.2f}")
lista_numeros.reverse()
print(f"Números na ordem inversa: {lista_numeros}")