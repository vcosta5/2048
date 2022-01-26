# Importando a super classe com os métodos genéricos associados com a mecânica do jogo
if __name__ == '__main__':
    from ferramentasDeMecanicaDoJogo import *

else:
    from classes.ferramentasDeMecanicaDoJogo import *

# Classe da seção mecânica do jogo
class MecanicaDoJogo(FerramentasDeMecanicaDoJogo):
    '''Esta classe contém todos os métodos responsável por alterar a tela e o estado do jogo de acordo com os comandos do jogador.'''

    def __init__(self, tamanhoDoTabuleiro = 4):
        '''
        Método construtor que inicializa o tabuleiro. Se nenhum parâmetro for passado, inicializa com o tamanho padrão 4X4.
        self,int -> none
        '''
        # Atributo que armazena a matriz do tabuleiro
        self.tabuleiro = self.geraMatriz(tamanhoDoTabuleiro, tamanhoDoTabuleiro)

        # Atributo que armazena o score
        self.score = 0

        # Atributo que armazena a lista com os números para serem sorteados e inseridos no tabuleiro a cada nova rodada
        # A cada nova rodada, 90% de chance da nova peça ser 2 e 10% de chance da nova peça ser 4
        self.listaComOsNumerosParaSeremSorteadosEInseridosACadaNovaRodada = [2, 2, 2, 2, 2, 2, 2, 2, 2, 4]

        # Conjunto com todos os atributos da classe
        self.__atributos = {
            'self.__atributos',
            'self.__metodos',
            'self.tabuleiro',
            'self.score',
            'self.listaComOsNumerosParaSeremSorteadosEInseridosACadaNovaRodada'
        }

        # Conjunto com todos os métodos da classe
        self.__metodos = {
            '__init__',
            '__str__',
            'getAtributos',
            'getMetodos',
            'manual',
            'geraMatriz',
            'geraNumeroAleatorio',
            'inserePeca',
            'movePecas',
            'checaTabuleiro',
            'getTabuleiro',
            'getScore',
            'carregarJogo'
        }

    def __str__(self):
        '''
        Método que retorna uma string convenientemente formatada com todos os atributos e métodos da classe.
        self -> str
        '''

        string = f'Classe mecanicaDoJogo:\n{MecanicaDoJogo.__doc__}\n\nAtributos:\n'

        # Passa por todos os atributos e insere na string
        for i in self.__atributos:
            string += '\t' + i + ': ' + self.manual()[i] + '\n'

        string += '\nMétodos:\n'

        # Passa por todos os métodos e insere na string
        for i in self.__metodos:
            string += '\t' + i + ': ' + self.manual()[i] + '\n'

        return string

    def getAtributos(self):
        '''
        Método que retorna o conjunto com todos os atributos da classe.
        self -> set
        '''
        return self.__atributos

    def getMetodos(self):
        '''
        Método que retorna o conjunto com todos os métodos da classe.
        self -> set
        '''
        return self.__metodos

    def manual(self):
        '''
        Método que retorna um dicionário com todos os atributos e métodos da classe com suas respectivas documentações.
        self -> dict
        '''
        return {
            'self.__atributos': 'Conjunto com todos os atributos da classe.',
            'self.__metodos': 'Conjunto com todos os métodos da classe.',
            'self.tabuleiro': 'Atributo que armazena a matriz do tabuleiro.',
            'self.score': 'Atributo que armazena o score.',
            'self.listaComOsNumerosParaSeremSorteadosEInseridosACadaNovaRodada': 'Atributo que armazena a lista com os números para serem sorteados e inseridos no tabuleiro a cada nova rodada.',
            '__init__': self.__init__.__doc__,
            '__str__': self.__str__.__doc__,
            'getAtributos': self.getAtributos.__doc__,
            'getMetodos': self.getMetodos.__doc__,
            'manual': self.manual.__doc__,
            'geraMatriz': self.geraMatriz.__doc__,
            'geraNumeroAleatorio': self.geraElementoAleatorio.__doc__,
            'inserePeca': self.inserePeca.__doc__,
            'movePecas': self.movePecas.__doc__,
            'checaTabuleiro': self.checaTabuleiro.__doc__,
            'getTabuleiro': self.getTabuleiro.__doc__,
            'getScore': self.getScore.__doc__,
            'carregarJogo': self.carregarJogo.__doc__
        }

    def inserePeca(self, listaComAsCasasVazias):
        '''
        Método que insere uma nova peça no tabuleiro em uma casa livre.
        self,list -> none
        '''
        # Sorteia a nova peça
        peca = self.geraElementoAleatorio(self.listaComOsNumerosParaSeremSorteadosEInseridosACadaNovaRodada)

        # Sorteia a casa vazia
        casa = self.geraElementoAleatorio(listaComAsCasasVazias)

        # Altera o atributo "tabuleiro" com a nova peça
        self.tabuleiro[int(casa[0])][int(casa[1])] = peca

    def movePecas(self, entradaDoUsuario):
        '''
        Método que move todas as peças do tabuleiro de acordo com a entrada do usuário. Retorna "True" se alguma peça virou 2048 ou "False" se não.
        self,str -> none
        '''
        pass

    def checaTabuleiro(self):
        '''
        Método que verifica todas as casas do tabuleiro.
        Retorna uma lista de strings com todas as posições de casas vazias.
        A primeira posição da string é a posição da linha e a segunda é a posição da coluna.
        self -> list
        '''
        # Lista para armazenar as posições vazias
        lista = []

        # Passa por todas as linhas
        for i in range(len(self.tabuleiro)):
            # Passa por todas as colunas
            for j in range(len(self.tabuleiro[i])):
                # Caso a casa possuir o elemento "None", adiciona na lista a posição da casa
                if self.tabuleiro[i][j] == None:
                    lista.append(f'{i}{j}')

        return lista

    def getTabuleiro(self):
        '''
        Método que retorna a matriz do tabuleiro.
        self -> list
        '''
        return self.tabuleiro

    def getScore(self):
        '''
        Método que retorna o score.
        self -> int
        '''
        return self.score

    def carregarJogo(self, tabuleiro, score):
        '''
        Método que atualiza os atributos com os dados do jogo salvo.
        self,list,int -> none
        '''
        self.tabuleiro = tabuleiro
        self.score = score