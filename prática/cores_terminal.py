print('\033[;36;45mOlá mundo!\033[m') 
a = 1
b = 2
nome = 'Aiden'
print('Os valores são \033[31m {} \033[m e \033[36m {} \033[m !!!'.format(a,b))
print('Muito prazer em te conhecer \033[31m {}\033[m !!'.format(nome))
print('Muito prazer em te conhecer  {}{}{} !!'.format('\033[31m', nome,'\033[m'))
# Tecnica dicionário 
cores =  {
    'limpa': '\033[m',
    'azul' : '\033[34m',
    'amarelo' : '\033[33m',
    'pretoebranco' : '\033[7;30m'
    }
print('Muito prazer em te conhecer  {}{}{} !!'.format(cores['pretoebranco'], nome, cores['limpa']))