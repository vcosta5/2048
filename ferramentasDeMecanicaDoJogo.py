class ferramentasDeMecanicaDoJogo:
    '''Super classe com métodos genéricos associados com a mecânica do jogo.'''

    def __init__(self):
        '''
        Método construtor.
        self -> none
        '''

        # Conjunto com todos os atributos da classe
        self.__atributos = {
            'self.__atributos',
            'self.__metodos'
        }

        # Conjunto com todos os métodos da classe
        self.__metodos = {
            '__init__',
            '__str__',
            'getAtributos',
            'getMetodos',
            'manual',
            'geraMatriz',
            'geraNumeroAleatorio'
        }

    def __str__(self):
        '''
        Método que retorna uma string convenientemente formatada com todos os atributos e métodos da classe.
        self -> str
        '''

        string = f'Classe ferramentasDeMecanicaDoJogo:\n{ferramentasDeMecanicaDoJogo.__doc__}\n\nAtributos:\n'

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
            '__init__': self.__init__.__doc__,
            '__str__': self.__str__.__doc__,
            'getAtributos': self.getAtributos.__doc__,
            'getMetodos': self.getMetodos.__doc__,
            'manual': self.manual.__doc__,
            'geraMatriz': self.geraMatriz.__doc__,
            'geraNumeroAleatorio': self.geraNumeroAleatorio.__doc__
        }

    def geraMatriz(self, numeroDeLinhas, numeroDeColunas):
        '''
        Método para gerar uma matriz. Retorna uma lista de listas (matriz).
        self,int,int -> list
        '''
        return None

    def geraNumeroAleatorio(self, listaDeNumeros):
        '''
        Método para sortear um número aleatório de uma dada lista. Retorna o número sorteado.
        self,list -> int
        '''
        pass