from __future__ import annotations
from datetime import date
atual = date.today().year
nasc = int(input('Ano de nascimento: '))
idade = atual - nasc
print('Quem nasceu em {} tem {} anos em {}.'.format(nasc, idade, atual))
if idade == 18:
    print('VocÊ tem qeu se alistar IMEDIATAMENTE!')
elif idade < 18 :
    saldo = 18 - idade
    print('Ainda faltam {} anos para o alistmanto'. format(saldo))
    ano = atual + saldo
    print('Seu alistamento será em {}'.format(ano))
elif idade > 18:
    saldo = idade - 18
    print('Você já deveria ter se alistado há {} anos.'.format(saldo))
    ano = atual - saldo
    print('Seu alistamento foi em {}'.format(ano))





# Minha reolução
#idade = int(input('Digite a sua idade: '))
#if idade < 18:
#    print('VocÊ ainda terá que se alistar')
#elif idade == 18:
#    print('Está na hora de se alistar')
#else:
#    print('Você já se alistou!')