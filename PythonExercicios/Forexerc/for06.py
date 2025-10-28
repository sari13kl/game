#Crie um programa que calcule o fatorial de um número (por exemplo, 5! = 5 x 4 x 3 x 2 x 1)
n = 0
numero = int(input('Diga um número entre 1 e 10:'))
for i in range(numero - 1, 0, -1):
    if n == 0:
        n = numero
        print(f'{numero} ', end = '')
    n *= i
    print(f'x {i} ', end = '')
print(f'= {n}')