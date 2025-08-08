# Elabore um algoritmo que leia os valores reais de A, B, C e em seguida imprima na tela a soma entre A e
# B e mostre se a soma é menor que C

a = int(input("A: "))
b = int(input("B: "))
c = int(input("C: "))
soma = a + b 
if soma > c:
    print("a soma de A + B é maior que C.")
else: 
    print("a soma de A + B é menor que C.")