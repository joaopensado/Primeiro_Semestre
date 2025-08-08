#Ler 10 valores, calcular e escrever a média aritmética desses valores lidos.

quantidade = 0 
soma = 0 
for num in range (1,11): 
    soma = soma + num
    quantidade += 1
    media = soma / quantidade
print(media)
