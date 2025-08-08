n = int(input("digite a quantidade de numeros:"))
contimpar = 0
somapar = 0
for x in range(n):
    num = int(input("Digite um número: "))
    if num % 2 == 0:
        somapar += num
    else:
        contimpar += 1
    

print("a soma dos pares são: " , somapar)
print("a quantidade de impares são: " , contimpar)
