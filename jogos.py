#Importa os outros dois jogos para o menu
import forca
import adivinhacao

#Define uma função para o menu de jogos
def escolha_jogo():
    print("*******************")
    print("Escolha o seu jogo!")
    print("*******************\n")

    print("1 - Jogo da forca\n2 - Jogo da adivinhação\n3 - Sair")

    #Recebe qual jogo o usuário deseja jogar
    jogo = int(input("Qual jogo deseja jogar: "))
    print("")

    #if para decidir qual jogo o usuário escolheu e executa-lo
    if(jogo == 1):
        forca.jogar()
    elif(jogo == 2):
        adivinhacao.jogar()
        
    
if(__name__ == "__main__"):
    escolha_jogo()