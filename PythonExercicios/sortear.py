import random
import time
print('Vou pensar em um número entre 0 e 5. Tente adivinhar...')
time.sleep(2)
numero_sorteado = random.randint(0, 5)

numero_dito = int(input('Em que número eu pensei?'))
print('PROCESSANDO...')
time.sleep(2)
if numero_dito == numero_sorteado:
    print('PERDI....Parabéns! Você é um gênio!')
else:
    print(f'GANHEI! Eu pensei no número {numero_sorteado} e não no {numero_dito}!')