# A jornada de trabalho semanal de um funcionário é de 40 horas. O funcionário que trabalhar mais de 40
# horas receberá hora extra, cujo cálculo é o valor da hora regular com um acréscimo de 50%. Escreva um
# algoritmo que leia o número de horas trabalhadas em um mês, o salário por hora e escreva o salário
# total do funcionário, que deverá ser acrescido das horas extras, caso tenham sido trabalhadas 
# (considere que o mês possua 4 semanas exatas).


# Leitura dos dados
horas_mes = int(input("Informe a quantidade de horas trabalhadas pelo funcionário no mês: "))
salario_hora = float(input("Informe o salário por hora: "))

# Definições
horas_semanais = 40
semanas = 4
horas_trabalhadas_mes = horas_semanais * semanas  # 160 horas mensais

# Cálculo do salário
if horas_mes > horas_trabalhadas_mes:
    # Calculando horas extras
    horas_extras = horas_mes - horas_trabalhadas_mes
    salario_extra = salario_hora * 1.5  # Hora extra com acréscimo de 50%
    salario_total = (horas_trabalhadas_mes * salario_hora) + (horas_extras * salario_extra)
else:
    # Sem horas extras
    salario_total = horas_mes * salario_hora

# Exibição do salário total
print(f"O salário total do funcionário é: R$ {salario_total:.2f}")
