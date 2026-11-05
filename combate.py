# Import das funções
from ia import escolherGolpeIA
from interface import informacaoDaVidaDosPersonagens

# Import de bibliotecas
import os
import time

# Função para iniciar a luta
def lutar(jogador, adversario):
    # Limpar o terminal depois da escolha de personagens
    os.system("cls")
    os.system("clear")
    rodada = 1

    print("Lutem!\n")

    rodada = 1
    while jogador["vidaAtual"] > 0 and adversario["vidaAtual"] > 0:
        print("=" * 20)
        print(" " * 5 + f"RODADA {rodada}")
        print("=" * 20)
        time.sleep(1)

        # Exibe as informações relacionadas a vida de cada um
        print(f"{jogador["nome"]} | HP: {jogador["vidaAtual"]}")
        informacaoDaVidaDosPersonagens(jogador)
        print("\n") # pular linha
        print(f"{adversario["nome"]} | HP: {adversario["vidaAtual"]}")
        informacaoDaVidaDosPersonagens(adversario)
        print("\n") # pular linha

        try:
            # Mostra as habilidades do personagem do player
            print("HABILIDADES")
            print("=" * 25)
            for indice, golpe in enumerate(jogador["golpes"], start=1):
                
                print(f"{indice} - {golpe["nome"]} | Dano: {golpe["dano"]}")

            print("=" * 25)
            
            print("=" * 10)
            print("SUA RODADA")
            print("=" * 10)

            # escolha de habilidades do usuário
            escolhaGolpe = int(input("Escolha o golpe que deseja utilizar: "))

            # Estrutura de condição para verificar se o golpe escolhido é válido
            if 1 <= escolhaGolpe <= len(jogador["golpes"]):
                golpeEscolhido = jogador["golpes"][escolhaGolpe - 1]

                vidaRestante = adversario["vidaAtual"] - golpeEscolhido["dano"]

                adversario["vidaAtual"] = vidaRestante

                print(f"{jogador["nome"]} utilizou: {golpeEscolhido["nome"]}\n")

                time.sleep(1)
                # Condição pra verificar se o usuário já venceu
                if adversario["vidaAtual"] <= 0:
                    # Exibe as informações relacionadas a vida de cada um
                    print(f"{jogador["nome"]} | HP: {jogador["vidaAtual"]}")
                    informacaoDaVidaDosPersonagens(jogador)
                    print("\n") # pular linha
                    print(f"{adversario["nome"]} | HP: {adversario["vidaAtual"]}")
                    informacaoDaVidaDosPersonagens(adversario)
                    print("\n") # pular linha
                    # Mostra na tela que o player venceu
                    print("=" * 25)
                    print(f"{jogador["nome"]} VENCEU!")
                    print("=" * 25)
                    break

                time.sleep(1)

            else:
                print("Golpe inexistente!")
                continue
            
            # escolha de habilidades da IA
            print("=" * 20)
            print("RODADA DO ADVERSÁRIO")
            print("=" * 20)


            if adversario["vidaAtual"] > 0:
                golpeEscolhidoIA = escolherGolpeIA(adversario, jogador)

                jogador["vidaAtual"] -= golpeEscolhidoIA["dano"]

                print(f"{adversario["nome"]} utilizou {golpeEscolhidoIA["nome"]}!\n")

                time.sleep(1)
                 # Condição pra verificar se o adversário já venceu
                if jogador["vidaAtual"] <= 0:
                    # Exibe as informações relacionadas a vida de cada um
                    print(f"{jogador["nome"]} | HP: {jogador["vidaAtual"]}")
                    informacaoDaVidaDosPersonagens(jogador)
                    print("\n") # pular linha
                    print(f"{adversario["nome"]} | HP: {adversario["vidaAtual"]}")
                    informacaoDaVidaDosPersonagens(adversario)
                    print("\n") # pular linha
                    # Mostra na tela que o adversário venceu
                    print("=" * 25)
                    print(f"{adversario["nome"]} VENCEU!")
                    print("=" * 25)
                    break

                time.sleep(1)

            rodada += 1

        except ValueError:
            print("Digite apenas números!")