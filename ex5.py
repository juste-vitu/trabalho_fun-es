def calcular_preco_aluguel(km, dias):
    preco = (dias * 60) + (km * 0.15)
    return round(preco, 2)

#main
km_percorridos = float(input("Quantos km foram percorridos com o carro? "))
dias_alugados = int(input("Por quantos dias o carro foi alugado? "))
preco_total = calcular_preco_aluguel(km_percorridos, dias_alugados)

print("O preço total a pagar é R$", (preco_total))