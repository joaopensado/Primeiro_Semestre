x = float(input("digite o valor de x:" ))
n = int(input("digite o valor de y: "))

resultado = 1

if n >= 0:
    for i in range(n):
        resultado *= x

    print(f"{x:.0f} elevado a {n:.0f} é {resultado:.0f}")
else:
    print("O valor de n deve ser um inteiro não negativo.")
