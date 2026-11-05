# Import das funções
from ia import escolherGolpeIA
from interface import exibirLifePoints, exibicaoRodadas

# Import de bibliotecas
import os
import time

# Função para iniciar a luta
def lutar(jogador, adversario):
    # Limpar o terminal depois da escolha de personagens
    os.system("cls")
    os.system("clear")

    # Contador de rodadas
    rodadas = 1

    print("Lutem!\n")

    while jogador["vidaAtual"] > 0 and adversario["vidaAtual"] > 0:
        # Função que exibe as rodadas
        exibicaoRodadas(rodada = rodadas)
        time.sleep(1)

        # Exibe as informações relacionadas a vida de cada um
        exibirLifePoints(jogador, adversario)

        try:
            # Exibe a rodada do player
            exibicaoRodadas(titulo="SUA RODADA")

            # Mostra as habilidades do personagem do player
            print("HABILIDADES")
            print("-" * 30)
            for indice, golpe in enumerate(jogador["golpes"], start=1):
                
                print(f"{indice} - {golpe["nome"]} | Dano: {golpe["dano"]}")

            print("-" * 30)

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
                    exibirLifePoints(jogador, adversario)

                    # Mostra na tela que o player venceu
                    print("=" * 25)
                    print(f"{jogador["nome"]} VENCEU!")
                    print("=" * 25)
                    break

                time.sleep(1)

            else:
                print("Golpe inexistente!")
                continue

            # Exibe a rodada do adversário
            exibicaoRodadas(titulo="RODADA DO ADVERSÁRIO")
            time.sleep(1)
            
            # escolha de habilidades da IA
            if adversario["vidaAtual"] > 0:
                golpeEscolhidoIA = escolherGolpeIA(adversario, jogador)

                jogador["vidaAtual"] -= golpeEscolhidoIA["dano"]

                print(f"{adversario["nome"]} utilizou {golpeEscolhidoIA["nome"]}!")

                 # Condição pra verificar se o adversário já venceu
                if jogador["vidaAtual"] <= 0:
                    # Exibe as informações relacionadas a vida de cada um
                    exibirLifePoints(jogador, adversario)

                    # Mostra na tela que o adversário venceu
                    print("=" * 25)
                    print(f"{adversario["nome"]} VENCEU!")
                    print("=" * 25)
                    break

                time.sleep(1)

            # Incrementa o valor na variável rodadas
            rodadas += 1

        except ValueError:
            print("Digite apenas números!")