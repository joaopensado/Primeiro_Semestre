valor_metro = float(input("informe o valor do metro de tela: R$"))
comprimento = float(input("informe o comprimento do terreno em metros:"))
largura = float(input("informe a largura do terreno em metros:"))
perimetro = comprimento * 2 + largura * 2
valor_total = perimetro * valor_metro
print(f"o custo total sera de: R${valor_total:.2f}")