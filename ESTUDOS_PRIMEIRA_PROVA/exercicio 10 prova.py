# A prefeitura de uma cidade deseja fazer uma pesquisa entre seus habitantes. Faça um algoritmo para
# coletar dados sobre o salário e número de filhos de cada habitante e após as leituras, escrever:
# a) Média de salário da população
# b) Média do número de filhos
# c) Maior salário dos habitantes
# d) Percentual de pessoas com salário menor que R$ 1500,00
# Obs.: O final da leitura dos dados se dará com a entrada de um “salário negativo”.

salario = 0 
filhos = 0 
maior_salario = 0 
salario_menor_1500 = 0
quantidade_filhos = 0 
quantidade_salario = 0
soma_salario = 0

while salario >= 0:
    salario = float(input("informe o salario: "))
    filhos += int(input("informe a quantidade de filhos: "))
    quantidade_salario = quantidade_salario + 1
    quantidade_filhos = quantidade_filhos + 1
    soma_salario = soma_salario + salario
    media_salario = soma_salario / quantidade_salario
    print(f" a média de salario é: {media_salario} ")
    if salario < 1500:
        salario_menor_1500 = salario_menor_1500 + 1
    percentual_salario = 100 * salario_menor_1500 / quantidade_salario
    percentual_salario = salario / quantidade_salario
    print(f"o percentual é: {percentual_salario}")
    if salario > maior_salario:
        maior_salario = salario
    print(f"o maior salario é: {maior_salario} ")
    media_filhos = filhos/ quantidade_filhos
    print(f"a media de filhos é de: {media_filhos}")
