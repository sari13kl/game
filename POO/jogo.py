import random
#jogo com heroi e inimigos
class Personagem:
    def __init__(self, nome, vida, nivel):
        self.__nome = nome
        self.__vida = vida
        self.__nivel = nivel

    def get_nome(self):
        return self.__nome
    
    def get_vida(self):
        return self.__vida
    
    def get_nivel(self):
        return self.__nivel
    
    def exibir_detalhes(self):
        return f'Nome: {self.get_nome()}\nVida: {self.get_vida()}\nNível: {self.get_nivel()}\n'
    
    def atacar(self, alvo):
        dano = self.__nivel * 2
        print(f'{self.get_nome()} ataca {alvo.get_nome()} causando {dano} de dano!')
    
    def receber_dano(self, dano):
        self.__vida -= dano
        if self.__vida < 0:
            self.__vida = 0
    
    def atacar(self, alvo):
        dano = random.randint(self.get_nivel() * 2, self.get_nivel() * 4)#baseado na nivel
        alvo.receber_dano(dano)
        print(f'{self.get_nome()} atacou {alvo.get_nome()} causando {dano} de dano!')

class Heroi(Personagem):
    def __init__(self, nome, vida, nivel, poder):
        super().__init__(nome, vida, nivel)
        self.__poder = poder
    
    def get_poder(self):
        return self.__poder

    def exibir_detalhes(self):
        return f'{super().exibir_detalhes()}\nPoder: {self.get_poder()}\n'

    def ataque_especial(self, alvo):
        dano = random.randint(self.get_nivel() * 5, self.get_nivel() * 8)  # dano especial baseado no nível
        alvo.receber_dano(dano)
        print(f'{self.get_nome()} usou ataque especial em {alvo.get_nome()} causando {dano} de dano!')

class Inimigo(Personagem):
    def __init__(self, nome, vida, nivel, tipo):
        super().__init__(nome, vida, nivel)
        self.__tipo = tipo
    
    def get_tipo(self):
        return self.__tipo
    
    def exibir_detalhes(self):
        return f'{super().exibir_detalhes()}\nTipo: {self.get_tipo()}\n'

class Jogo:
    """Classe principal do jogo que gerencia heróis e inimigos."""

    def __init__(self):
        self.heroi = Heroi(nome='Arthur', vida=100, nivel=5, poder='Espada Sagrada')
        self.inimigo = Inimigo(nome='Dragão', vida=70, nivel=4, tipo='Fogo')

    def iniciar_jogo(self):
        """Fazer a gestão da batalha entre herói e inimigo."""
        print('Iniciando batalha!')
        while self.heroi.get_vida() > 0 and self.inimigo.get_vida() > 0:
            print('\nDetalhes dos Personagens:')
            print(f'{self.heroi.exibir_detalhes()}')
            print(f'{self.inimigo.exibir_detalhes()}')

            input('Pressione Enter para atacar...')
            escolha = input('Escolha (1 - Ataque Normal), (2 - Ataque Especial):')
            
            if escolha == '1':
                self.heroi.atacar(self.inimigo)
            elif escolha == '2':
                self.heroi.ataque_especial(self.inimigo)
            else:
                print('Escolha inválida!')
                continue
            
            if self.inimigo.get_vida() > 0:#se o inimigo ainda estiver vivo, ele ataca o heroi
                self.inimigo.atacar(self.heroi)
            

        if self.heroi.get_vida() > 0:
            print('\nParabéns! Você venceu o inimigo!')
        else:
            print('\nVocê foi derrotado!')

#Criar uma instância do jogo e iniciar
jogo = Jogo()
jogo.iniciar_jogo()
