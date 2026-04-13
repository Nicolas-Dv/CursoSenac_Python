valor = float(input("Digite o Valor da Compra"))

if valor >= 5000.00:
    novo_valor = valor * 0.8
else:
   novo_valor = valor * 0.85

print("Valor Final:", novo_valor)