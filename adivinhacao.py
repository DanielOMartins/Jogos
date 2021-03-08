#importa a biblioteca para gerar um número random e o arquivo jogos 
import random
import jogos

#Define a Função jogar para chamar ela em outros arquivos
def jogar():
    inicio()

    #Declaração das variáveis
    numero_secreto = random.randrange(1, 101) #Gera um número random de 1 a 100
    total_tentativas = 0
    pontos = 1000

    #Print teste para saber o número discreto
    #print(numero_secreto)

    #Variável para salvar o valor de entrada que seleciona o nível de dificuldade
    nivel = int(input(" 1 - Fácil\n 2 - Médio\n 3 - Difícil\nEscolha um nível de jogo entre: "))
    print("")
    
    total_tentativas = nivel_jogo(nivel)

    #for para executar as tentativas
    for rodada in range(1, total_tentativas + 1):
        print("Rodada {} de {}".format(rodada, total_tentativas)) #Formatação ideal para um print
        num = int(input("Digite o seu número entre 1 e 100: "))

        #Define o limite para o número digitado pelo usuário
        if(num < 1 or num > 100):
            print("O número precisa ser entre 1 e 100!\n")
            continue
        
        #Variáveis que recebem o resultado da tentativa do usuário
        acertou = num == numero_secreto
        maior = num > numero_secreto
        menor = num < numero_secreto

        #if para definir e imprimir o resultado
        if(acertou):
            print("Você acertou e fez {} pontos" .format(pontos))
            break
        else:
            if(maior):
                print("O número secreto é menor do que {}\n".format(num))
            elif(menor):
                print("O número secreto é maior do que {}\n".format(num))
        
        #Variáveis que recebem os pontos da rodado e 
        pontos_perdidos = abs(numero_secreto - num)
        pontos = pontos - pontos_perdidos
        
    print("Fim de jogo!!")
    continuar_jogando()
    
def inicio():
    print("************************")
    print("Bem vindo a adivinhação!")
    print("************************\n")
def nivel_jogo(nivel):
    if(nivel == 1):
        total_tentativas = 10
    elif(nivel == 2):
        total_tentativas = 5
    else:
        total_tentativas = 3
    return total_tentativas
def continuar_jogando():
    continuar = input("Deseja voltar ao menu de jogos? (sim/nao)\n")
    continuar = continuar.lower()
    if(continuar == "sim"):
        return jogos.escolha_jogo()
    else:
        return print("\nObrigado por jogar com a gente!!")
#Garante que arquivo pode ser executado diretamente
if(__name__ == "__main__"):
    jogar()