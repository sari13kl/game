#exemplo de herança
class Tarefas:
    def __init__(self, nome):
        self.nome = nome

    def prioridade(self):
        return "Alta"

class TarefasImportantes(Tarefas):
    def prioridade(self):
        return f'{self.nome} é uma tarefa importante e tem prioridade alta.'
    
tarefa = TarefasImportantes('Estudar POO')

print('Nome da tarefa:', tarefa.nome)
print('Prioridade da tarefa:', tarefa.prioridade())

print('--' * 30)

#exemplo de decoradores
def decorador(funcao):
    def funcao_decorada():
        print('Antes da função decorada')
        funcao()
        print('Depois da dunção decorada')
    return funcao_decorada

@decorador
def mimnha_funcao():
    print('Minha funcao decorada')

print('--' * 30)

class Estudo:
    def __init__(self, título, conteudo, importancia, horas):
        self.titulo = título
        self.conteudo = conteudo
        self.importancia = importancia
        self.horas = horas
    
    @classmethod
    def criar_estudo(cls, etapa1):
        titulo, conteudo, importancia, horas = etapa1.split(';')
        return cls(titulo, conteudo, importancia, horas)

etapa1 = 'Programação;POO;Alta;13:00'
estudo1 = Estudo.criar_estudo(etapa1)
print(f'Nome do estudo: {estudo1.titulo}\nConteúdo: {estudo1.conteudo}\nImportância: {estudo1.importancia}\nHorário: {estudo1.horas}')

print('--' * 30)
