#Exercício Python 056: Desenvolva um programa que leia o nome, idade e sexo de 4 pessoas. 
#No final do programa, mostre: a média de idade do grupo, qual é o nome do homem mais velho e quantas mulheres têm menos de 20 anos.
contagem = 0 #idades
soma = 0 #idades
mvelho = 0
nomevelho = ''
fmenores = 0
for p in range(1,5):
    print(f'------ {p} Pessoa ------')
    nome = str(input('Nome:'))
    idade = int(input('Idade:'))
    sexo = str(input('Sexo[M/F]:')).lower()
    soma += idade #idades
    contagem += 1 #idades
    if idade > mvelho and sexo == 'm':
        mvelho = idade
        nomevelho = nome
    if idade < 18 and sexo == 'f':
        fmenores += 1

media = soma / contagem #idades
print(f'A media da idades do grupo é de {media} anos.')
print(f'O homem mais velho tem {mvelho} anos e se chama {nomevelho}.')
print(f'Ao todo são {fmenores} mulheres com menos de 20 anos.')

