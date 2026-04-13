valor = float(input("Digite a Faixa Salarial:"))

if valor <= 500.00:
 novo_valor = valor

elif 500.01 <= valor <= 1500.00:
 novo_valor = valor * 0.9

elif 1500.01 <= valor <= 2500.00:
 novo_valor = valor * 0.85

else: 
  novo_valor = valor * 0.8

print("Novo salário:", novo_valor)

