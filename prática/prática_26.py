dis = int(input("Distancia da sua viagem me Km: "))
if dis <= 200:
    preco = 0.5 * dis
    print('O preço da sua viajem deu {} reais'. format(preco))
else:
    preco_long = 0.45 * dis
    print('O preço da sua viajem é de {} reias'.format(preco_long))