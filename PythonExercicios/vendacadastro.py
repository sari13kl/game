import time
from datetime import datetime
import os
print('Seja bem- vindo(a) ao menu da sua loja.')
time.sleep(3)
estoque = []
historico_vendas = []
agora = datetime.now()
hora = agora.strftime('%H:%M:%S')

opção = 0
while opção != 5:
    print('''      [ 1 ] ESTOQUE
      [ 2 ] CADASTRAR PRODUTO
      [ 3 ] VENDA
      [ 4 ] HISTÓRICO DE VENDAS
      [ 5 ] SAIR''')
    opção = int(input('Digite o número da opção desejada:\n>>> '))
    os.system('cls')
    

    if opção == 1:
        if estoque:
            for produtos in estoque:
              print(f'>>{produtos}')
        else:
          print('Não há produto no estoque.')

    elif opção == 2:
        while True:
            existe = False
            id_produto = int(input('Código do produto: '))
            
            for produto in estoque:
                if produto['id'] == id_produto:
                    existe = True
                    break
            
            if existe:
                print('Código existente. Por favor, insira um código diferente.')
                continue
            
            else:
                nome = str(input('Nome do produto: ')).title()
                valor = float(input('Valor do produto: R$'))
                quantidade = int(input('Quantidade no estoque: '))

                estoque.append({
                    'id' : id_produto,
                    'nome' : nome,
                    'valor': valor,
                    'quantidade': quantidade
                })
            print(f'Produto "{nome}" cadastrado com sucesso!')
            break
  
    elif opção == 3:
        carrinho = []
        while True:
            cod = int(input('Informe o id do produto:'))
            os.system('cls')
      
            achou = False
            item = {}

            for produtos in estoque:
                 if produtos['id'] == cod:
                    achou = True
                    item = {
                        'id' : produtos['id'],
                        'nome' : produtos['nome'],
                        'valor': produtos['valor'],
                    }
                    break
            if achou == False:
                print('Código inválido. Tente novamente.')
                continue
            
            quant = int(input('Informe a quantidade desejada:'))
            os.system('cls')
    
            if quant > produtos['quantidade']:
                print(f'Quantidade indisponível. Há somente {produtos["quantidade"]} unidade(s) em estoque.')
            else:
                produtos['quantidade'] -= quant
                item['total'] = quant * produtos['valor']
                carrinho.append(item)
                print(f'{quant} unidade(s) do produto "{item['nome']}" adicionada(s) ao carrinho.')

            continuar = str(input('Deseja adicionar mais alguma coisa ao carrinho? (s/n)')).lower()
            if continuar != 's':
                break
            os.system('cls')

        if carrinho:
            total_compra = sum(item['total'] for item in carrinho)
            for item in carrinho:
                print(f'''----------RESUMO DA COMPRA---------
                        {item['nome']} - R${item['valor']} x {item['total'] / item['valor']} = R${item['total']}
                        ''')
                print(f'TOTAL DA COMPRA: R${total_compra}')
            
            historico_vendas.append({
        'itens': carrinho,
        'total': total_compra,
        'hora': hora
        })
        
        else:
            print('Nenhum produto adicionado ao carrinho')

    
    elif opção == 4:
        if historico_vendas:
            for venda in historico_vendas:
                print(f'Venda às {venda['hora']}')
                for item in venda['itens']:
                    print(f'- {item['nome']} (R${item['valor']}) x {item['total'] / item['valor']} = R${item['total']}')
                print(f'Total da venda: R${venda['total']}')
        else:
            print('Nenhuma venda registrada ainda.')



    elif opção == 5:
        print("Saindo... Obrigado por utilizar o sistema!")
        os.system('cls')
        break          
    
    else:
        print('Opção inválida. Tente novamente.')
        os.system('cls')
    
    time.sleep(2)
