# Import das funções
from ia import escolherGolpeIA
from interface import exibirLifePoints, exibicaoRodadas, exibirVitoria, exibirHabilidades

# Import de bibliotecas
import os
import time

# Função para calcular o dano dos personagens
def calcularDano(atacante, defensor, habilidade):

    dano = atacante["ataque"] + habilidade["dano"]
    danoBruto = dano - defensor["defesa"]
    somaTotal = max(1, danoBruto)

    return somaTotal

# Função para verificar se a habilidade tem cargas suficientes
def verificarCargas(habilidade):
    return habilidade["cargas"] > 0

# Função para executar o turno do jogador
def executarTurnoJogador(jogador, adversario):
    # escolha de habilidades do usuário
    escolhaGolpe = int(input("Escolha o golpe que deseja utilizar: "))

    # Estrutura de condição para verificar se o golpe escolhido é válido
    if 1 <= escolhaGolpe <= len(jogador["golpes"]):
        golpeEscolhido = jogador["golpes"][escolhaGolpe - 1]

        if not verificarCargas(golpeEscolhido):
            print("Essa habilidade está sem cargas!")
            return False

        golpeEscolhido["cargas"] -= 1

        # Calcula o dano do player
        danoEfetivo = calcularDano(jogador, adversario, golpeEscolhido)
        adversario["vidaAtual"] = max(0, adversario["vidaAtual"] - danoEfetivo)

        print(f"{jogador["nome"]} utilizou: {golpeEscolhido["nome"]}\n")

        time.sleep(1)
        # Condição pra verificar se o usuário já venceu
        if adversario["vidaAtual"] <= 0:
            # Exibe as informações relacionadas a vida de cada um
            exibirLifePoints(jogador, adversario)

            # Mostra na tela que o player venceu
            exibirVitoria(jogador)
            
            time.sleep(1)

    else:
        print("Golpe inexistente!")

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
            exibicaoRodadas(titulo="SEU TURNO")

            # Mostra as habilidades do personagem do player
            exibirHabilidades(jogador)

            # Verifica se o golpe escolhido pelo usuário existe e tem cargas
            resultado = executarTurnoJogador(jogador, adversario)

            # Se o golpe não existir ou não tiver cargas, retorna falso
            if resultado is False:
                continue

            #### Transição de turno ###

            # Exibe a rodada do adversário
            exibicaoRodadas(titulo="TURNO DO ADVERSÁRIO")
            time.sleep(1)
            
            # escolha de habilidades da IA
            if adversario["vidaAtual"] > 0:
                # Permite a IA escolher um golpe
                golpeEscolhidoIA = escolherGolpeIA(adversario, jogador, calcularDano, verificarCargas)

                # Decrementa uma carga da habilidade usada da IA
                golpeEscolhidoIA["cargas"] -= 1

                danoEfetivoIA = calcularDano(adversario, jogador, golpeEscolhidoIA)
                jogador["vidaAtual"] = max(0, jogador["vidaAtual"] - danoEfetivoIA)

                print(f"{adversario["nome"]} utilizou {golpeEscolhidoIA["nome"]}!\n")

                # Condição pra verificar se o adversário já venceu
                if jogador["vidaAtual"] <= 0:
                    # Exibe informações da vida dos personagens
                    exibirLifePoints(jogador, adversario)

                    # Exibe que o adversário venceu a batalha
                    exibirVitoria(adversario)
                    
                time.sleep(1)

            # Incrementa o valor na variável rodadas
            rodadas += 1

        except ValueError:
            print("Digite apenas números!")