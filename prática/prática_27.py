ano = int(input('DIGITE SEU ANO AQUI: '))
if ano % 4 == 0 and ano % 100 !=0 or ano % 4000 == 0:
    print('É um ano bissexto ')
else:
    print('Ano não bissexto')