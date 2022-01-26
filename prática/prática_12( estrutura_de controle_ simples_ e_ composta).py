a = int(input('Digite um valor: '))
b = int(input('Digite outro valor: '))
c = int(input('Digite mais um valor: '))
if a > b and a > c:
    print('Ele é o maior {}'.format(a))
elif b > a and b > c:
    print('Ele é o maior {}'.format(b))
elif c > a and c > b: 
    print('Ele é o maior {}'.format(c))
