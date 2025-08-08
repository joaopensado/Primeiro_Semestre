dias_trabalhados = float(input("informe a quantidade de dias trabalhados pelo encanador:"))
salario = 30 * dias_trabalhados
imposto = 8/100 * salario
salario_pago = salario - imposto
print(f"o salario pago ao encanador é:{salario_pago:.2f} ")