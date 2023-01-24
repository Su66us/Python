import forca
import adivinhacao



print("*********************************")
print("*******Escolha um jogo!**********")
print("*********************************")

print('(1) Forca (2) Adivinhção')

jogo = int(input('Qual jogo: '))

if(jogo == 1):
    print('Jogando Forca')
    forca.jogar()
elif(jogo == 2):
    print('Jogando adivinhação')
    adivinhacao.jogar()