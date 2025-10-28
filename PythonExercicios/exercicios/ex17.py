 #Crie um programa que leia dois valores e mostre um menu na tela:
#[ 1 ] somar[ 2 ] multiplicar[ 3 ] maior[ 4 ] novos números[ 5 ] sair do programa
#Seu programa deverá realizar a operação solicitada em cada caso.
n1 = int(input('Insira o primeiro valor:\n'))
n2 = int(input('Insira o segundo valor:\n'))
opção = 0
while opção != 5:
    print('''      [ 1 ] SOMAR
      [ 2 ] MULTIPLICAR
      [ 3 ] MAIOR
      [ 4 ] NOVOS NÚMEROS
      [ 5 ] SAIR DO PROGRAMA''')
    opção = int(input('>>>>>> Qual é a sua opção?\n'))

    if opção == 1:
        soma = n1 + n2
        print(f'A soma entre {n1} + {n2} é igual a {soma}.')
    
    elif opção == 2:
        multiplica = n1 * n2
        print(f'A multiplicação entre {n1} x {n2} é igual a {multiplica}.')

    elif opção == 3:
        if n1 > n2:
            maior = n1
        else:
            maior = n2
        print(f'Entre {n1} e {n2} o maior valor é {maior}.')
    elif opção == 4:
        print('Informe os números novamente:')
        n1 = int(input('Insira o primeiro valor:\n'))
        n2 = int(input('Insira o segundo valor:\n'))
    elif opção == 5 :
        print('Finalizando...')
    else:
        print('Opção inválida. Tente novamente.')

print('Fim! Volte sempre.')

