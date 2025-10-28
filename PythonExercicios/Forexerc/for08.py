#Exercício 2: Crie uma lista com 10 números e calcule a soma de todos os números dessa lista.
print('Me informe 10 números:')
s = 0
for c in range(1, 11):
    n = int(input(f' {c}-Número:  '))
    s += n
print(f'Soma desses números resulta no valor = {s}')
