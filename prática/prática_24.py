velocidade = int(input('Digite a velocidade do carro: '))
if velocidade > 80:
    print('você foi multado')
    km = velocidade - 80
    valor_multa  = (km * 7) / 10 
    print('O valor da multa foi de {} reais'.format(valor_multa))
else:
    print('Você não foi multado')
    print('fim programa')