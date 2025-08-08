numero = int(input("digite um numero inteiro de 3 digitos:"))
resultado = numero // 100
numero = numero - (100 * resultado)
resultado2 = numero //10
numero = numero - (10 * resultado2)
resultado3 = numero // 1
print("o numero invertido é: ", resultado3, resultado2, resultado)

