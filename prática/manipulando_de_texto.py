frase = 'Meu pau'
# Fatiamento de string
# Somente um micro espaço
print(frase[0])
# Apresenta mais de um micro espaço do 0 ao 2 sendo o 3 a condição de parada
print(frase[1:3])
# Apresente a condição de inicio (2) a de parada (7) sendo parado no micro espaço 6 e pulando de dois em dois(um sim um não)
print(frase[2:7:2])
# Não apresenta uma condição de inicio ou seja começa no espaço 0 até a condição de parada (5) ou seja mostra até o 4
print(frase[:5])
# Mesma lógica do anterior só que ao contrário
print(frase[0:])
# Apresenta um condição de inico não tendo condição de parada vai até o final pulando de dois em dois(um sim um não)
print(frase[0::2])