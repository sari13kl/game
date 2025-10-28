#Faça um programa que leia o sexo de uma pessoa, mas só aceite os valores 'M' ou 'F'. Caso esteja errado, peça a digitação novamente até ter um valor correto.
M = 'M'
F = 'F'
sexo = str(input('Informe seu sexo: [M/F]\n')).upper()
if sexo == M:
    print('Certo! Seu sexo é Masculino.')
else:
    print('Certo! Seu sexo é Feminino.')

while sexo != M and sexo != F:
    sexo = str(input('Digito incorreto. Informe novamente seu sexo:\n')).upper()
