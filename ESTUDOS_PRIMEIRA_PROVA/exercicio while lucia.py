n = int(input("digite um numero: "))
maior = n 
cont = 1 
while cont < 15:
    n = int(input("digite um numero:"))
    if n > maior: 
        maior = n 
    cont = cont + 1 
print(maior)
