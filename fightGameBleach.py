import random
import time
import os

# Jogo de luta inspirado no anime Bleach

# Função para criação dos personagens
def criarPersonagem(nome, vidaAtual, vidaMaxima , ataque, defesa, golpes):
    personagem = {
        "nome": nome,
        "vida": vidaAtual,
        "vidaMaxima": vidaMaxima,
        "ataque": ataque,
        "defesa": defesa,
        "golpes": golpes
    }

    return personagem

# Golpes e Transformações
ichigoHabilidades = [
    {"nome": "Estocada", "dano": 12},
    {"nome": "Getsuga Tenshou", "dano": 30},
]
    
ulquiorraHabilidades = [
    {"nome": "Estocada", "dano": 10},
    {"nome": "Cero", "dano": 20}
]

# Criando os personagens através da função criarPersonagem
ichigo = criarPersonagem("Ichigo Kurosaki", 100, 100 , 5, 20, ichigoHabilidades)
ulquiorra = criarPersonagem("Ulquiorra Ciffer", 100, 100 ,7 , 18, ulquiorraHabilidades)

# Função para escolha de personagem
def escolherPersonagem(personagens):
    while True:
        try:
            for indice, personagem in enumerate(personagens, start=1):
                print(f"{indice} - {personagem["nome"]}")

            escolha = int(input("Escolha um personagem: "))
            print("\n")

            if 1 <= escolha <= len(personagens):
                personagemEscolhido = personagens[escolha - 1]

                informacaoDosPersonagens(personagemEscolhido)

                confirmar = str(input("\nDeseja escolher ele mesmo (S/N): ")).strip().upper()
                print("\n")

                if confirmar == "S":
                    return personagemEscolhido
                else:
                    print("\n")
               
            else:
                print("Personagem inexistente! Tente novamente.")


        except ValueError:
            print("Digite apenas números!")

# Função para que o usuário escolha seu adversário
def escolherAdversario(personagens):
    while True:
        try:
            for indice, personagem in enumerate(personagens, start=1):
                print(f"{indice} - {personagem["nome"]}")

            escolha = int(input("Escolha seu adversário: "))
            print("\n")


            if 1 <= escolha <= len(personagens):
                personagemAdversario = personagens[escolha - 1]

                informacaoDosPersonagens(personagemAdversario)

                confirmar = str(input("Deseja escolher ele mesmo (S/N): ")).strip().upper()

                if confirmar == "S":
                    return personagemAdversario
                else:
                    print("\n")

            else:
                print("Personagem inexistente! Tente novamente.")

        except ValueError:
            print("Digite apenas números!")


# Função para iniciar a luta
def lutar(jogador, adversario):
    # Limpar o terminal depois da escolha de personagens
    os.system("cls")
    os.system("clear")
    rodada = 1

    print("Lutem!\n")

    rodada = 1
    while jogador["vida"] > 0 and adversario["vida"] > 0:
        print("=" * 20)
        print(" " * 5 + f"RODADA {rodada}")
        print("=" * 20)
        print(f"{jogador["nome"]} - HP: {jogador["vida"]}")
        print(f"{adversario["nome"]} - HP: {adversario["vida"]}\n")

        try:
            for indice, golpe in enumerate(jogador["golpes"], start=1):
                print(f"{indice} - {golpe["nome"]} | Dano: {golpe["dano"]}")

            print("=" * 10)
            print("SUA RODADA")
            print("=" * 10)
            # escolha de golpe do usuário
            escolhaGolpe = int(input("Escolha o golpe que deseja utilizar: "))

            if 1 <= escolhaGolpe <= len(jogador["golpes"]):
                golpeEscolhido = jogador["golpes"][escolhaGolpe - 1]

                vidaRestante = adversario["vidaAtual"] - golpeEscolhido["dano"]

                adversario["vida"] = vidaRestante

                time.sleep(1)
                print(f"{jogador["nome"]} utilizou: {golpeEscolhido["nome"]}\n")

            else:
                print("Golpe inexistente!")
                continue


            print(f"vida atual de {adversario["nome"]} = {adversario["vidaAtual"]}\n")

            # escolha de golpe da IA
            print("=" * 10)
            print("RODADA DO ADVERSÁRIO")
            print("=" * 10)
            if adversario["vida"] > 0:
                golpeEscolhidoIA = escolherGolpeIA(adversario, jogador)

                jogador["vidaAtual"] -= golpeEscolhidoIA["dano"]

                time.sleep(1)
                print(f"{adversario["nome"]} utilizou {golpeEscolhidoIA["nome"]}!\n")

            print(f"Vida atual de {jogador["nome"]} = {jogador["vidaAtual"]}\n")

            rodada += 1

        except ValueError:
            print("Digite apenas números!")

# Função para escolha de golpes do adversário
def escolherGolpeIA(adversario, jogador):
    for golpe in adversario["golpes"]:
        if golpe["dano"] >= jogador["vidaAtual"]:
            return golpe

    return random.choice(adversario["golpes"])
            


# Função exibir informação dos personagens
def informacaoDosPersonagens(personagem):

    print("=" * 35)
    print(" " * 10 + f"{personagem["nome"]}")
    print("=" * 35)
    print(f"Vida: {personagem["vidaMaxima"]} | Ataque: {personagem["ataque"]} | Defesa: {personagem["defesa"]}\n")

    print("HABILIDADES")
    print("-" * 30)
    for golpe in personagem["golpes"]:
        print(f"- {golpe['nome']} | Dano: {golpe['dano']}")
    print("-" * 30)

# Função para exibir HP (health points) dos personagens
def informacaoDaVidaDosPersonagens(personagem):
    VERDE = "\033[32m"
    AMARELO = "\033[33m"
    VERMELHO = "\033[31m"
    RESET = "\033[0m"

    tamanhoDaBarra = 20 # Define tamanho da barra
    proporcao = personagem["vidaAtual"] / personagem["vidaMaxima"] # faz o cálculo da divisão da vida atual pela vida máxima
    
    blocosPreenchidos = int(proporcao * tamanhoDaBarra) # faz o cálculo de multiplicação pra descobrir quantos caracteres serão preenchidos
    blocosVazios = tamanhoDaBarra - blocosPreenchidos

    barraPrenchida = "█" * blocosPreenchidos
    barraVazia = "░" * blocosVazios

    barra = barraPrenchida + barraVazia 

    if proporcao > 0.5:
        cor = VERDE
    elif proporcao > 0.2:
        cor = AMARELO
    else:
        cor = VERMELHO

    print(cor + barra + RESET)


personagens = [ichigo, ulquiorra]
# Variável para armazenar escolha do usuário
personagemEscolhido = escolherPersonagem(personagens)
# Variável para armazenar escolha de adversário do usuário
personagemAdversario = escolherAdversario(personagens)
# Variável para começar a luta
lutar(personagemEscolhido, personagemAdversario)