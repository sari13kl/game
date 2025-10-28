from random import randint
numero_sorteado = randint(0, 10)
print('Irei pensar em um número de 0 a 10, será que você consegue adivinhar...')
acerto = False
palpites = 0
while not acerto:
    numero_dito = int(input('Qual o seu palpite?  '))
    palpites += 1
    if numero_dito == numero_sorteado:
        acerto = True
    else:
        if numero_dito < numero_sorteado:
            print('Mais...')
        elif numero_dito > numero_sorteado:
            print('Menos...')
print(f'Acertou com {palpites} tentaivas. Parabéns!')