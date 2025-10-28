n = int(input('Digite um número para gerar a tabuada:\n>>'))

print(f'A tabuada do {n}:')
for i in range(1, 11):
    print(f'{n} x {i} = {n * i}')
