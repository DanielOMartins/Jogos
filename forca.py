import jogos
import random

def jogar():
    
    inicio()
    palavra_secreta = leitura_palavras()
   
    letras_acertadas = padrao_forca(palavra_secreta)
    print(letras_acertadas)
    
    enforcou = False
    acertou = False
    tentativas = 0

    #Enquanto true
    while(not enforcou and not acertou):
        chute = pede_chute()
        
        if(chute in palavra_secreta):
           verifica_chute(chute, letras_acertadas, palavra_secreta)
        else:
            tentativas += 1
            desenha_forca(tentativas)

        enforcou = tentativas == 7
        acertou = "_" not in letras_acertadas
        print(letras_acertadas)
    
    if(acertou):
        imprime_vencedor()
    else:
        imprime_perdedor(palavra_secreta, tentativas)
    
    continuar_jogando()
    

def inicio():
    print("*******************")
    print("Bem vindo a forca!")
    print("*******************\n")
def leitura_palavras():
    arquivo = open("palavras.txt", "r")
    palavras = []

    for linha in arquivo:
        linha = linha.strip()
        palavras.append(linha)

    arquivo.close()

    numero = random.randrange(0,len(palavras))
    palavra_secreta = palavras[numero].upper()

    return palavra_secreta
def padrao_forca(palavra):
    return ["_" for letra in palavra]
def pede_chute():
    chute = input("Digite uma letra: ")
    chute = chute.strip().upper()
    return chute
def verifica_chute(chute, letras_acertadas, palavra_secreta):
    i = 0
    for letra in palavra_secreta:
        if(chute == letra):
            letras_acertadas[i] = letra
        i += 1
def desenha_forca(erros):
    print("  _______     ")
    print(" |/      |    ")

    if(erros == 1):
        print(" |      (_)   ")
        print(" |            ")
        print(" |            ")
        print(" |            ")

    if(erros == 2):
        print(" |      (_)   ")
        print(" |      \     ")
        print(" |            ")
        print(" |            ")

    if(erros == 3):
        print(" |      (_)   ")
        print(" |      \|    ")
        print(" |            ")
        print(" |            ")

    if(erros == 4):
        print(" |      (_)   ")
        print(" |      \|/   ")
        print(" |            ")
        print(" |            ")

    if(erros == 5):
        print(" |      (_)   ")
        print(" |      \|/   ")
        print(" |       |    ")
        print(" |            ")

    if(erros == 6):
        print(" |      (_)   ")
        print(" |      \|/   ")
        print(" |       |    ")
        print(" |      /     ")

    if (erros == 7):
        print(" |      (_)   ")
        print(" |      \|/   ")
        print(" |       |    ")
        print(" |      / \   ")

    print(" |            ")
    print("_|___         ")
    print()
def imprime_vencedor():
    print("Parabéns, você ganhou!")
    print("       ___________      ")
    print("      '._==_==_=_.'     ")
    print("      .-\\:      /-.    ")
    print("     | (|:.     |) |    ")
    print("      '-|:.     |-'     ")
    print("        \\::.    /      ")
    print("         '::. .'        ")
    print("           ) (          ")
    print("         _.' '._        ")
    print("        '-------'       ")
def imprime_perdedor(palavra_secreta, erros):
    print("Puxa, você foi enforcado!")
    print("A palavra era {}".format(palavra_secreta))
    print("  _______     ")
    print(" |/      |    ")
    if (erros == 7):
        print(" |      (_)   ")
        print(" |      \|/   ")
        print(" |       |    ")
        print(" |      / \   ")

    print(" |            ")
    print("_|___         ")
    print("\n")
def continuar_jogando():
    continuar = input("Deseja voltar ao menu de jogos? (sim/nao)\n")
    continuar = continuar.lower()
    if(continuar == "sim"):
        return jogos.escolha_jogo()
    else:
        return print("\nObrigado por jogar com a gente!!")

if(__name__ == "__main__"):
    jogar()