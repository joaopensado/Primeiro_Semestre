salario = int(input("informe o salario do funcionario: ")) 
plano = int(input("informe o plano do funcionario: plano 1, plano 2, plano 3: "))
plano1 = (salario * 10/100) + salario
plano2 = (salario * 15/100) + salario
plano3 = (salario * 20/100) + salario
if plano == 1:
    print(f"o novo salario é {plano1}")
elif plano == 2:
    print(f"o novo salario é {plano2}")
elif plano == 3: 
    print(f"o novo salario é {plano3}")