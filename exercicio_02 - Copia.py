cateto_1 = int(input("Informe o valor do primeiro Cateto: "))
cateto_2 = int(input("Informe o valor do segundo Cateto: "))

import math
hipotenusa = math.sqrt(cateto_1*cateto_1 + cateto_2*cateto_2)

print(f"Valor da Hipotenusa: {hipotenusa:.2f}")
