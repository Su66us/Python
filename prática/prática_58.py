try:# operação 
    a = int(input('Numerador: '))
    b = int(input('Denominador: '))
    r = a / b
except(ValueError, TypeError):# se acontecer algum desse erro aparece igual o if
    print('Tivemos um problema com os tipos de dados que você digitou. ')
except ZeroDivisionError:
    print('Não é possivle dividir um número por zero!')
except KeyboardInterrupt:
    print('O usuário preferiu não informar os dados!')
except Exception as erro:
    print(f'O erro encontrado foi {erro.__cause__}')
else:#se deu certo
    print(f'O resultado é {r:.1f}')
finally:# vai acontecer de qualquer forma
    print('Volte sempre!')
    