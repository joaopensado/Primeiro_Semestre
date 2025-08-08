numero = int(input("digite um numero: "))
intervalo1 = 0 
intervalo2 = 0
intervalo3 = 0
intervalo4 = 0 
while numero >= 0: 
    if numero <= 25: 
        intervalo1 = intervalo1 + 1
    elif numero <= 50:
        intervalo2 = intervalo2 + 1
    elif numero <= 75:
        intervalo3 = intervalo3 + 1
    elif numero <= 100:
        intervalo4 = intervalo4 + 1
    numero = int(input("digite um numero: "))
print(f"o resultado é: {intervalo1} ")
print(f"o resultado é: {intervalo2} ")
print(f"o resultado é: {intervalo3} ")
print(f"o resultado é: {intervalo4} ")