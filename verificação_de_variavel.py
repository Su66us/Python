a = input('Digite algo: ')
print('O tipo primitivo desse valor é ', type(a))
print('só tem espaços? ', a.isspace())
print('É um número? ', a.isnumeric())
print('É alfabetico?', a.isalpha())
print('É alfanumérico?', a.isalnum())
print('Está em maiúsculas? ', a.isupper())
print('Está em minúsculas? ', a.islower())
print('Está capitalizada? ', a.istitle())
# Esse "A" se refere ao objeto
# Esse parenteses é o "metodo"