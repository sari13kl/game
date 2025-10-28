nome = input(str('Informe seu nome completo:\n')).strip()

print('Seu nome em maiúsculo é: {}'.format(nome.upper()))

print('Seu nome em minúsculo é: {}'.format(nome.lower()))

print('Seu nome ao todo possui {} letras'.format(len(nome) - nome.count(' ')))

print('Seu primeiro nome tem {} letras'.format(nome.find(' ')))



#Outra forma de fazer:
separa = nome.split()
print('Seu primeiro nome é {} e ele tem {} letras'.format(separa[0], len(separa[0])))