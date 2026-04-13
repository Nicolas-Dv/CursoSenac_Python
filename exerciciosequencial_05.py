soma = 0
for numero in range(85, 907):

    modulo_numero = numero % 2
    if modulo_numero == 0:
     print(f"O número [{numero}] é par.")
     soma = soma + numero

print(f"A soma dos números pares é {soma}")
