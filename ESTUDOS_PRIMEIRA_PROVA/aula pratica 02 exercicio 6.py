tempo_gasto = float(input("informe o tempo gasto na viagem em horas:"))
velocidade_media = float(input("informe a velocidade media e Km/h:"))
distancia = velocidade_media / tempo_gasto
consumo = distancia / 12
print("a velocidade média percorrida foi:" , velocidade_media)
print("o tempo gasto foi:" , tempo_gasto)
print("a distancia percorrida foi:" , distancia)
print("o consumo é:" , consumo) 