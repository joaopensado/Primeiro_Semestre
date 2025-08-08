# Elabore um algoritmo que leia o ano em que uma pessoa nasceu, imprima na tela quantos anos, meses
# e dias essa pessoa já viveu. Considere o ano com 365 dias e o mês com 30 dias.

ano_nascimento = int(input("informe a data de nascimento: "))
ano_atual = 2025
meses = 12
dias = 365
anos_vividos = ano_atual - ano_nascimento
meses_vividos = anos_vividos * meses 
dias_vividos = anos_vividos * dias
print(f"{anos_vividos} , {meses_vividos} , {dias_vividos}")