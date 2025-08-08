# #Construa um algoritmo que efetue o cálculo do salário líquido de um professor do ensino funamental.
# As informações fornecidas serão: valor da hora aula, número de aulas lecionadas no mês e percentual
# de desconto do INSS. Imprima na tela o salário líquido final.

valor_aula = float(input("informe o valor da aula: "))
quantidade_aulas = int(input("informe o quantidade de aulas: "))
percentual_desconto = int(input("informe o desconto do INSS: "))
salario_bruto = valor_aula * quantidade_aulas
salario_liquido = salario_bruto - percentual_desconto
print(f"o salario liquido é {salario_liquido}")
