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
personagemEscolhido = escolherPersonagem(personagens)
personagemAdversario = escolherAdversario(personagens)