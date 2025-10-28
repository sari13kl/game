import time
from datetime import datetime
import os

class GerenciadorTarefas:
    def __init__(self):
        self.tarefas = []
        self.historico_tarefas = []
  
    def cadastrar_tarefa(self, tarefa):
        if tarefa in self.tarefas:
            return 'Tarefa já cadastrada.'
        else:
            self.tarefas.append(tarefa)
            return f'Tarefa "{tarefa}" cadastrada com sucesso!'
    
    def listar_tarefas(self):
        if len(self.tarefas) == 0:
            return 'Nenhuma tarefa cadastrada.'
        else:
            return 'Tarefas cadastradas:\n' + '\n'.join(f'{i+1}- {tarefa}' for i, tarefa in enumerate(self.tarefas))
   
    def concluir_tarefa(self, num_tarefa):
        if not self.tarefas:
            return 'Nenhuma tarefa cadastrada.'
        try:
                indice = int(num_tarefa) - 1
                tarefa_concluida = self.tarefas.pop(indice)
                self.historico_tarefas.append(f'{tarefa_concluida} - concluída em {datetime.now().strftime("%H:%M:%S")}')
                return f'Tarefa "{tarefa_concluida}" concluída com sucesso!'
            
        except (ValueError, IndexError):
            return 'Tarefa inválida. Por favor, insira um número válido.'
    
    def mostrar_historico(self):
        if not self.historico_tarefas:
            return 'Nenhuma tarefa concluída.'
        else:
            return 'Histórico de tarefas concluídas:\n' + '\n'.join(self.historico_tarefas)

# Gerenciador de Tarefas Simples
os.system('cls' if os.name == 'nt' else 'clear')

print('Gerenciador de Tarefas da Sarah!')
gerenciador = GerenciadorTarefas()

while True:
    print('\nMenu:')
    print('''
        [ 1 ] LISTAR TAREFAS
        [ 2 ] CADASTRAR TAREFA
        [ 3 ] CONCLUIR TAREFA
        [ 4 ] HISTÓRICO DE TAREFAS
        [ 5 ] SAIR''')
    opcao = input('Escolha uma opção: ')

    if opcao == '1':
        print(gerenciador.listar_tarefas())
    
    elif opcao == '2':
        tarefa = input('Digite o nome da tarefa:')
        print(gerenciador.cadastrar_tarefa(tarefa))

    elif opcao == '3':
        print(gerenciador.listar_tarefas())
        numero = input('Digite o número da tarefa concluída:')
        print(gerenciador.concluir_tarefa(numero))
    
    elif opcao == '4':
        print(gerenciador.mostrar_historico())

    elif opcao == '5':
        print('Saindo do gerenciador de tarefas...')
        time.sleep(1)
        break
    else:
        print('Opção inválida. Tente novamente.')
    time.sleep(1)
            