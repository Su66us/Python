def jogar():
    print("*********************************")
    print("Bem vindo ao jogo da Forca!      ")
    print("*********************************")

    palavra_secreta = "banana" 
    letras_acertadas = ['_','_','_','_','_','_']
    enforcou = False
    acertou = False

    print(letras_acertadas)
    #  lista [] tuplas() não pode mudar imutavel estrura de dados 
    # enquanto (true e true)
    while(not enforcou and not acertou):
        
        chute = input('Qual letra: ')
        chute = chute.strip()

        index = 0
        for letra in palavra_secreta:
            if(chute.upper() == letra.upper()):
                letras_acertadas[index] = letra
            index = index + 1

        print(letras_acertadas)

    print('Fim de Jogo')
if(__name__ =="__main__"):
    jogar()