import random

print("========== JOKENPÔ ==========\n")

print("PEDRA\t\tPAPEL\t\tTESOURA\n")

print("    _______ \t    _______ \t        _______")
print("---'   ____) \t---'   ____)____ \t---'   ____)____")
print("      (_____) \t          ______) \t          ______)")
print("      (_____) \t          _______) \t       __________)")
print("      (____) \t         _______) \t      (____)")
print("---.__(___) \t---.__________) \t---.__(___)\n")

print("======================")
print("1 - Humano x Humano")
print("2 - Humano x Computador")
print("3 - Computador x Computador")
print("======================\n")

opcao = int(input("Insira qual modalidade você deseja jogar: "))

if opcao == 1:
    winPlayer1 = "Jogador 1 ganhou!" #variavel que guarda o texto de vitória do jogador 1, usado para simplificar o código
    winPlayer2 = "Jogador 2 ganhou!" #variavel que guarda o texto de vitória do jogador 2, usado para simplificar o código

    contPlayer1 = 0 #Contador de vitórias do jogador 1
    contPlayer2 = 0 #Contador de vitórias do jogador 2

    continuar = 0 #variavel para guardar o valor inserido se deseja continuar ou sair do jogo

    while continuar != 1:
        opcaoPlayer1 = input("\nPlayer 1. Pedra, papel ou tesoura?: ").lower() #input que recebe a opcao do jogador 1 com lower para transformar em minusculo e encurtar a verificação
        opcaoPlayer2 = input("Player 2. Pedra, papel ou tesoura?: ").lower() #input que recebe a opcao do jogador 2 com lower para transformar em minusculo e encurtar a verificação

        #abaixo, condicionais para verificação dos valores recebidos das variaveis, exibir os resultados e adicionar ao contador do placar

        if opcaoPlayer1 == "pedra" and opcaoPlayer2 == "papel":
            print("\n" + winPlayer2 + "\n")
            contPlayer2 += 1
        elif opcaoPlayer1 == "pedra" and opcaoPlayer2 == "tesoura":
            print("\n" + winPlayer1 + "\n")
            contPlayer1 += 1
        elif opcaoPlayer1 == "pedra" and opcaoPlayer2 == "pedra":
            print("\nEmpate!\n")



        elif opcaoPlayer1 == "papel" and opcaoPlayer2 == "pedra":
            print("\n" + winPlayer1 + "\n")
            contPlayer1 += 1
        elif opcaoPlayer1 == "papel" and opcaoPlayer2 == "tesoura":
            print("\n" + winPlayer2 + "\n")
            contPlayer2 += 1
        elif opcaoPlayer1 == "papel" and opcaoPlayer2 == "papel":
            print("\nEmpate!\n")



        elif opcaoPlayer1 == "tesoura" and opcaoPlayer2 == "pedra":
            print("\n" + winPlayer2 + "\n")
            contPlayer2 += 1
        elif opcaoPlayer1 == "tesoura" and opcaoPlayer2 == "papel":
            print("\n" + winPlayer1 + "\n")
            contPlayer1 += 1
        elif opcaoPlayer1 == "tesoura" and opcaoPlayer2 == "tesoura":
            print("\nEmpate!\n")

        #abaixo, mensagem informando que houve erro de digitação nas opções de jogada

        else:
            print("\nErro! Digite novamente.\n")

        continuar = int(input("Se deseja continuar? Digite 0. Deseja sair e ver o placar final? Digite 1 \nInsira a opção desejada: ")) #input que recebe um número, caso
        # ele seja específicamente 1, termina o laço de repetição e mostra o resto dos códigos abaixo

    print("\n======================")
    print(f"\n    PLACAR FINAL"
          f"\nJogador 1 x Jogador 2"
          f"\n   {contPlayer1}           {contPlayer2}")
    print("\nMuito obrigado por jogar!")
    print("\nFeito por Lucas Girata,\nAndrey Paviani e João Esperança!")
    print("\n======================")

elif opcao == 2:

    opcoes = ("pedra", "papel", "tesoura")
    computador = 0
    humano = 0
    empate = 0

    while True:

        escolha = input("Digite a sua jogada (pedra, papel ou tesoura): ").lower()

        jogadaComputador = random.choice(opcoes)
        jogadaHumano = escolha

        if jogadaComputador == "pedra" and jogadaHumano == "tesoura" or jogadaComputador == "papel" and jogadaHumano == "pedra" or jogadaComputador == "tesoura" and jogadaHumano == "papel":
            print("Humano:", jogadaHumano)
            print("Computador:", jogadaComputador)
            print("Computador venceu!")
            computador += 1
        elif jogadaHumano == "pedra" and jogadaComputador == "tesoura" or jogadaHumano == "papel" and jogadaComputador == "pedra" or jogadaHumano == "tesoura" and jogadaComputador == "papel":
            print("Humano:", jogadaHumano)
            print("Computador:", jogadaComputador)
            print("Humano venceu!")
            humano += 1
        else:
            print("Humano:", jogadaHumano)
            print("Computador:", jogadaComputador)
            print("O jogo deu empate!")
            empate += 1

        placar = (computador, humano, empate)
        print(placar)
        opcao = input("Deseja continuar ou sair?: ").lower()
        if opcao == "sair":
            print("Placar final: ", placar)
            break

elif opcao == 3:
    opcoes = ("pedra", "papel", "tesoura")
    computador1 = 0
    computador2 = 0
    empate = 0

    while True:

        jogadaComp1 = random.choice(opcoes)
        jogadaComp2 = random.choice(opcoes)

        if jogadaComp1 == "pedra" and jogadaComp2 == "tesoura" or jogadaComp1 == "papel" and jogadaComp2 == "pedra" or jogadaComp1 == "tesoura" and jogadaComp2 == "papel":
            print("Computador 1:", jogadaComp1)
            print("Computador 2:", jogadaComp2)
            print("Computador1 venceu!")
            computador1 += 1
        elif jogadaComp1 == "pedra" and jogadaComp2 == "papel" or jogadaComp1 == "papel" and jogadaComp2 == "tesoura" or jogadaComp1 == "tesoura" and jogadaComp2 == "pedra":
            print("Computador 1:", jogadaComp1)
            print("Computador 2:", jogadaComp2)
            print("Computador2 venceu!")
            computador2 += 1
        else:
            print("Computador 1:", jogadaComp1)
            print("Computador 2:", jogadaComp2)
            print("Empate")
            empate += 1

        placar = (computador1, computador2, empate)
        print(placar)
        opcao = input("Deseja continuar ou sair?")
        if opcao == "sair":
            print("Placar final: ", placar)
            print("Obrigado por jogar Andrey Paviani, Lucas Girata e João Esperança!")
            break

else:
    print("\nErro! Tente jogar novamente mais tarde.")