lado1 = int(input("informe o valor do primeiro lado do quadrilatero: "))
lado2 = int(input("informe o valor do segundo lado do quadrilatero: "))
lado3 = int(input("informe o valor do terceiro lado do quadrilatero: "))
lado4 = int(input("informe o valor do quarto lado do quadrilatero: "))
if lado1 == lado2 == lado3 == lado4:
    print("o quadrilatero é um quadrado") 
elif lado1 == lado3 and lado2 == lado4:
    print("o quadrilatero é um retangulo")
else:
    print("o quadrilatero não é retangulo e nem quadrado")