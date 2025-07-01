def calcularTempoViagem(distancia, velocidade):
    tempo = distancia / velocidade
    return round(tempo, 2)

#main
distancia = float(input("Digite a distância a percorrer (em km): "))
velocidade = float(input("Digite a velocidade média (em km/h): "))
tempoEstimado = calcularTempoViagem(distancia, velocidade)

print("O tempo estimado de viagem em horas é: ", (tempoEstimado))