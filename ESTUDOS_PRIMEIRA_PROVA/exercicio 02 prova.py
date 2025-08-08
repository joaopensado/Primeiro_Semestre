# Faça um algoritmo que calcule e escreva a média aritmética dos números inteiros entre 15 (inclusive) e
# 100 (inclusive).

soma = 0
quantidade = 0
for numero in range(15, 101):
    soma = soma + numero
    quantidade = quantidade + 1
media = soma / quantidade
print(f'A média aritmética dos números inteiros entre 15 e 100 é: {media}')


