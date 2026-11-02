import random

# Jogo de luta inspirado no anime Bleach

# Função para criação dos personagens
def criarPersonagem(nome, vida, ataque, defesa, golpes):
    personagem = {
        "nome": nome,
        "vida": vida,
        "ataque": ataque,
        "defesa": defesa,
        "golpes": golpes
    }

    return personagem

# Golpes e Transformações
ichigoHabilidades = [
    {"nome": "Getsuga Tenshou", "dano": 30},
    {"nome": "Estocada", "dano": 12},
    ]
    
ulquiorraHabilidades = [
    {"nome": "Estocada", "dano": 10},
    {"nome": "Cero", "dano": 20}
]

# Criando os personagens através da função criarPersonagem
ichigo = criarPersonagem("Ichigo Kurosaki", 100, 5, 20, ichigoHabilidades)
ulquiorra = criarPersonagem("Ulquiorra Ciffer", 100, 7, 18, ulquiorraHabilidades)

# Função para escolha de personagem
def escolherPersonagem(personagens):
    while True:
        try:
            for indice, personagem in enumerate(personagens, start=1):
                print(f"{indice} - {personagem['nome']}")

            escolha = int(input("Escolha um personagem: "))
            print("\n")

            if 1 <= escolha <= len(personagens):
                personagemEscolhido = personagens[escolha - 1]

                informacaoDosPersonagens(personagemEscolhido)

                confirmar = str(input("\nDeseja escolher ele mesmo (S/N): ")).strip().upper()

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
    print("Lutem!\n")

    while jogador["vida"] > 0 and adversario["vida"] > 0:
        print(f"{jogador["nome"]} - {jogador["vida"]}")
        print(f"{adversario["nome"]} - {adversario["vida"]}\n")

        try:
            for indice, golpe in enumerate(jogador["golpes"], start=1):
                print(f"{indice} - {golpe["nome"]} | Dano: {golpe["dano"]}")


            # escolha de golpe do usuário
            escolhaGolpe = int(input("Escolha o golpe que deseja utilizar: "))

            if 1 <= escolhaGolpe <= len(jogador["golpes"]):
                golpeEscolhido = jogador["golpes"][escolhaGolpe - 1]

                vidaRestante = adversario["vida"] - golpeEscolhido["dano"]

                adversario["vida"] = vidaRestante

            else:
                print("Golpe inexistente!")

            print(adversario["vida"])

            # escolha de golpe da IA
            if adversario["vida"] > 0:
                golpeEscolhidoIA = escolherGolpeIA(adversario, jogador)

                jogador["vida"] -= golpeEscolhidoIA["dano"]

                print(f"{adversario["nome"]} utilizou {golpeEscolhidoIA["nome"]}!")

            print(jogador["vida"])

        except ValueError:
            print("Digite apenas números!")

# Função para escolha de golpes do adversário
def escolherGolpeIA(adversario, jogador):
    for golpe in adversario["golpes"]:
        if golpe["dano"] >= jogador["vida"]:
            return golpe

    return random.choice(adversario["golpes"])
            


# Função exibir informação dos personagens
def informacaoDosPersonagens(personagem):

    print("=" * 35)
    print(" " * 10 + f"{personagem['nome']}")
    print("=" * 35)
    print(f"Vida: {personagem["vida"]} | Ataque: {personagem["ataque"]} | Defesa: {personagem["defesa"]}\n")

    print("HABILIDADES")
    print("-" * 30)
    for golpe in personagem["golpes"]:
        print(f"- {golpe['nome']} | Dano: {golpe['dano']}")
    print("-" * 30)


personagens = [ichigo, ulquiorra]
# Variável para armazenar escolha do usuário
personagemEscolhido = escolherPersonagem(personagens)
# Variável para armazenar escolha de adversário do usuário
personagemAdversario = escolherAdversario(personagens)
# Variável para começar a luta
lutar(personagemEscolhido, personagemAdversario)