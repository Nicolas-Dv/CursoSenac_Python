salario_bruto = float(input("Informe o salário: "))
desconto = salario_bruto * 0.2
salario_liquido = salario_bruto - desconto
print(f"Salário líquido: {salario_liquido:.2f}")
print("O Salário líquido: " + str(salario_liquido))
print("O Salário líquido: (0.2f)".format(salario_liquido))

