valor_casa = float(input('Valor da casa: R$'))
valor_salario = float(input('Salário do comprador: R$'))
anos = int(input('Quantos anos de financiamento:'))
prestaçao_base = valor_casa / (anos * 12)

taxa_juros_ano = 11.49 / 100
valor_juros = valor_casa * taxa_juros_ano * anos

prestacao_com_juros = (valor_casa + valor_juros) / (anos * 12)

minimo =  valor_salario * 30 / 100
print('Para pagar uma casa de R${:.2f} pela CAIXA em {} anos'.format(valor_casa, anos), end='')
print(' a prestação com juros será de R${:.2f}'.format(prestacao_com_juros)) 

if prestacao_com_juros <= minimo:
    print('EMPRÉSTIMO PODE SER CONCEDIDO!')

else:
    print('EMPRÉSTIMO NEGADO!')