#Melhore o jogo do DESAFIO 028 onde o computador vai "pensar" em um número entre 0 e 10. Só que agora o jogador vai tentar adivinhar até acertar, mostrando no final quantos palpites foram necessários para vencer.
import random

print('Irei pensar em um número de 0 a 10, tente adivinhar...')
numero_sorteado = random.randint(0, 10)
numero_dito = int(input('Em que número pensei?\n'))
palpite = 1

while numero_dito != numero_sorteado:
    print(f'Errou! Eu pensei no número {numero_sorteado} e não no {numero_dito}.')
    numero_sorteado = random.randint(0, 10)
    numero_dito = int(input('Tente novamente. Em que número pensei?\n'))
    palpite += 1


print(f'Perdi...Você é um gênio! Eu pensei no número {numero_sorteado}.')
print(f'Precisou apenas de {palpite} palpites')
