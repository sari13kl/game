valor = float(input('Qual o sálario atual do funcionário?\nR$'))
novo = valor + (valor * 15 / 100)

print('O funcionário que ganhava R${} teve um aumento salarial de 15% e agora recebe R${:.2f}!'.format(valor , novo))
