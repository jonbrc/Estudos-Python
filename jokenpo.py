from random import choice

opcoes = ['pedra', 'papel', 'tesoura']
jogando = True

while jogando:
    maquina = choice(opcoes)

    print("# pedra\n# papel\n# tesoura\n# sair")
    jogada = input("Escolha entre uma das opções: ").lower()

    if jogada == 'sair':
        print("Obrigado por jogar")
        break

    print(f"Jogada da máquina: {maquina}")

    if jogada not in opcoes:
        print("Jogada inválida, verifique se digitou a opção corretamente!")
    elif jogada == maquina:
        print("Empatou!")
    elif (jogada == 'pedra' and maquina == 'tesoura') \
        or (jogada == 'papel' and maquina == 'pedra') \
        or (jogada == 'tesoura' and maquina == 'papel'):
        print("Você ganhou! 🎉")
    else:
        print("Você perdeu! 😢")

    print('-' * 45)
