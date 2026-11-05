from interface import informacaoDosPersonagens

import os

# Função para criação dos personagens
def criarPersonagem(nome, vidaAtual, vidaMaxima , ataque, defesa, golpes):
    personagem = {
        "nome": nome,
        "vidaAtual": vidaAtual,
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
                    os.system("cls")
                    return personagemEscolhido
                else:
                    os.system("cls")
               
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
                    os.system("cls")
                    return personagemAdversario
                else:
                    os.system("cls")

            else:
                print("Personagem inexistente! Tente novamente.")

        except ValueError:
            print("Digite apenas números!")