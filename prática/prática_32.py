valor_casa = float(input('Digite o valor da casa: '))
salario = float(input('Digite seu sálario aqui: '))
anos_pagar = int(input('Quntos anos pretende pagar a casa: '))
trinta = salario * 30 / 100
prestação = valor_casa / (anos_pagar * 12)
print('Pára pagar uma casa de R$ {} em {} anos '.format(valor_casa,anos_pagar))
print('A prestação será de {}'.format(prestação))
if prestação <= trinta:
    print('emprestimo aprovado')
else:
    print('Impossivel aprovar emprestimo')