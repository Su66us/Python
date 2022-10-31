#import uteis importa todo o modulo se não importar por parte tem que colocar uteis. função que definiu no arquivo
# from modulo import tal cois
# import modulo vai tudo
from uuteis import numeros
num = int(input('Digite um numero: '))
fat = numeros.fatorial(num)
print(f'O fatorial de {num} é {fat}')
print(f'O dobro de {num} é {numeros.dobro(num)}')