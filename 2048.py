"""
2048
====

Sobre o jogo:
-------------

2048 é jogado em um tabuleiro de 4X4, com peças numéricas que deslizam
suavemente quando o jogador as move em um dos quatro sentidos
disponíveis: para cima, para baixo, à esquerda e à direita.

Cada vez, um novo número aparece aleatoriamente em um local vazio na
placa (com um valor de 2 ou 4).

Os blocos deslizam o mais longe possível na direção escolhida até que
eles sejam interrompidos por qualquer outro bloco ou a borda do
tabuleiro. Se duas peças do mesmo número colidem durante a movimentação,
elas irão se fundir em uma peça com o valor total das duas peças que
colidiram.

O jogo é vencido quando uma peça com o valor de 2048 aparece no
tabuleiro. Quando o jogador não tem movimentos legais (não há espaços
vazios e nem peças adjacentes com o mesmo valor), o jogo termina.
"""

# Propriedades do documento
__author__ = 'Marcel_Javierre'
__copyright__ = 'Copyright_2022'
__credits__ = __author__
__license__ = 'GPL'
__version__ = '1.0.0'
__maintainer__ = __author__
__email__ = 'javierremarcel@poli.ufrj.br'
__status__ = 'Production'

# Importando as classes de cada seção
from classes.interfaceComOUsuario import *
from classes.mecanicaDoJogo import *
from classes.log import *

# Definindo as configurações padrão do jogo
tamanhoDoTabuleiro = 4
objetivo = 2048

# Inicializando as instâncias de cada seção
interface = InterfaceComOUsuario()
mecanica = MecanicaDoJogo(tamanhoDoTabuleiro, objetivo)
log = Log()

# Função principal
def main():
    '''
    Função principal.

    () -> None
    '''
    # Definindo as variáveis de configuração como globais
    global tamanhoDoTabuleiro
    global objetivo

    # Definindo as instâncias de cada seção como globais
    global interface
    global mecanica
    global log

    # Exibindo o menu principal
    interface.limpaTela()
    interface.menuPrincipal()

    # Recebendo a entrada do usuário
    entrada = interface.entradaDoUsuario()

    # Verifica qual opção o usuário escolheu
    # Novo Jogo
    if entrada == '1':
        # Loop do jogo
        loopDoJogo()

    # Carregar Jogo
    elif entrada == '2':
        # Loop para receber a entrada do usuário da tela de opções
        while True:
            # Limpa a tela
            interface.limpaTela()

            # Lê as partidas salvas
            listaComOsDadosDasPartidasSalvas = log.carregarJogo()

            # Mostra a tela de carregamento
            interface.telaDeCarregamento(listaComOsDadosDasPartidasSalvas)

            # Caso não exista nenhuma partida salva, volta para o menu principal
            if listaComOsDadosDasPartidasSalvas == []:
                interface.entradaDoUsuario('Aperte Enter para Voltar ao Menu Principal\n')
                main()

            # Espera a entrada do usuário
            entrada = interface.entradaDoUsuario()

            # Seleciona uma ação de acordo com a entrada do usuário
            # Carregar jogo
            if entrada == '1':
                entrada = interface.entradaDoUsuario('Selecione a partida que deseja carregar:\n')

                # Converte a entrada para o índice da lista com os dados das partidas salvas
                indice = (int(entrada) - 1) * 5

                # Atualiza as variáveis de configuração com os dados da partida salva
                tamanhoDoTabuleiro = int(listaComOsDadosDasPartidasSalvas[indice + 1])
                objetivo = int(listaComOsDadosDasPartidasSalvas[indice + 2])

                # Reinicia a instância da mecânica do jogo
                mecanica = MecanicaDoJogo(tamanhoDoTabuleiro, objetivo)

                # Atualiza o tabuleiro e o score com os dados da partida salva
                mecanica.carregarJogo(eval(listaComOsDadosDasPartidasSalvas[indice + 3]), int(listaComOsDadosDasPartidasSalvas[indice + 4]))

                # Reinicia o loop do jogo
                loopDoJogo()

            # Apagar partida salva
            elif entrada == '2':
                entrada = interface.entradaDoUsuario('Selecione a partida que deseja apagar:\n')

                # Converte a entrada para o índice da lista com os dados das partidas salvas
                indice = (int(entrada) - 1) * 5

                # Apaga a partida salva
                log.apagarJogoSalvo(indice)

            # Voltar ao menu principal
            elif entrada == '3':
                main()

    # Opções
    elif entrada == '3':
        # Loop para receber a entrada do usuário da tela de opções
        while True:
            # Limpa a tela
            interface.limpaTela()

            # Mostra a tela de opções
            interface.telaDeOpcoes(tamanhoDoTabuleiro, objetivo)
            
            # Espera a entrada do usuário
            entrada = interface.entradaDoUsuario()

            # Seleciona uma ação de acordo com a entrada do usuário
            # Alterar as opções
            if entrada == '1':
                # Espera a entrada do usuário
                entrada = interface.entradaDoUsuario('Insira o tamanho do tabuleiro:\nEx.: 4 -> 4x4.\n')

                # Muda a variável com o novo tamanho do tabuleiro
                tamanhoDoTabuleiro = int(entrada)

                # Espera a entrada do usuário
                entrada = interface.entradaDoUsuario('Insira o valor do objetivo:\n')

                # Muda a variável com o novo objetivo
                objetivo = int(entrada)

                # Reinicia a instância da mecânica do jogo com os novos parâmetros
                mecanica = MecanicaDoJogo(tamanhoDoTabuleiro, objetivo)

            # Voltar ao menu principal
            elif entrada == '2':
                main()

    # Estatísticas
    elif entrada == '4':
        # Limpa a tela
        interface.limpaTela()

        print('Não Implementado')

        # Volta para o menu principal
        interface.entradaDoUsuario('Aperte Enter para Voltar ao Menu Principal\n')
        main()

    # Manual do Desenvolvedor
    elif entrada == '5':
        # Limpa a tela
        interface.limpaTela()

        # Mostra o título da tela
        interface.telaDoManual()

        # Escreve na tela a documentação de todas as classes do jogo
        print(interface, end = '')
        print(mecanica, end = '')
        print(log, end = '')

        # Volta para o menu principal
        interface.entradaDoUsuario('Aperte Enter para Voltar ao Menu Principal\n')
        main()

    # Sair do Jogo
    elif entrada == '6':
        # Limpa a tela
        interface.limpaTela()

        # Sai do jogo
        quit()

    # Caso o usuário insira qualquer outra coisa diferente do pedido, exibe novamente o menu principal
    else:
        main()

# Função do loop do jogo
def loopDoJogo():
    '''
    Função do loop do jogo.

    () -> None
    '''
    # Definindo as variáveis de configuração como globais
    global tamanhoDoTabuleiro
    global objetivo

    # Definindo as instâncias de cada seção como globais
    global interface
    global mecanica
    global log

    # Loop do jogo
    while True:
        # Loop para receber a entrada do usuário da tela do tabuleiro
        while True:
            # Limpa a tela
            interface.limpaTela()

            # Mostra o tabuleiro
            interface.telaDoTabuleiro(mecanica.getTabuleiro(), mecanica.getScore())

            # Espera a entrada do usuário
            entrada = interface.entradaDoUsuario()

            # Seleciona uma ação de acordo com a entrada do usuário
            # Cima
            if entrada == 'w' or entrada == 'W':
                # Loop para realizar toda a movimentação das peças do tabuleiro
                while mecanica.movePecas('cima') == True:
                    interface.pausa(0.1)
                    interface.limpaTela()
                    interface.telaDoTabuleiro(mecanica.getTabuleiro(), mecanica.getScore())
                break

            # Esquerda
            elif entrada == 'a' or entrada == 'A':
                # Loop para realizar toda a movimentação das peças do tabuleiro
                while mecanica.movePecas('esquerda') == True:
                    interface.pausa(0.1)
                    interface.limpaTela()
                    interface.telaDoTabuleiro(mecanica.getTabuleiro(), mecanica.getScore())
                break

            # Baixo
            elif entrada == 's' or entrada == 'S':
                # Loop para realizar toda a movimentação das peças do tabuleiro
                while mecanica.movePecas('baixo') == True:
                    interface.pausa(0.1)
                    interface.limpaTela()
                    interface.telaDoTabuleiro(mecanica.getTabuleiro(), mecanica.getScore())
                break

            # Direita
            elif entrada == 'd' or entrada == 'D':
                # Loop para realizar toda a movimentação das peças do tabuleiro
                while mecanica.movePecas('direita') == True:
                    interface.pausa(0.1)
                    interface.limpaTela()
                    interface.telaDoTabuleiro(mecanica.getTabuleiro(), mecanica.getScore())
                break

            # Pause
            elif entrada == 'p' or entrada == 'P':
                # Loop para receber a entrada do usuário da tela de pause
                while True:
                    # Limpa a tela e mostra a tela de pause
                    interface.limpaTela()
                    interface.telaDePause()

                    # Espera a entrada do usuário
                    entrada = interface.entradaDoUsuario()

                    # Seleciona uma ação de acordo com a entrada do usuário
                    # Voltar ao jogo
                    if entrada == '1':
                        # Limpa a tela, mostra o tabuleiro e volta ao loop de receber uma entrada para mover as peças do tabuleiro
                        interface.limpaTela()
                        interface.telaDoTabuleiro(mecanica.getTabuleiro(), mecanica.getScore())
                        break

                    # Salvar o jogo
                    elif entrada == '2':
                        # Mostra a tela de salvamento
                        interface.limpaTela()
                        interface.telaDeSalvamento()

                        # Salva o jogo
                        log.savarJogo(tamanhoDoTabuleiro, objetivo, mecanica.getTabuleiro(), mecanica.getScore())

                        interface.pausa(1)

                    # Voltar ao menu principal
                    elif entrada == '3':
                        # Reinicia a instância da mecânica do jogo
                        mecanica = MecanicaDoJogo(tamanhoDoTabuleiro, objetivo)

                        # Volta ao menu principal
                        main()

        # Verifica se o alguma peça atingiu o objetivo
        if mecanica.venceuOJogo() == True:
            # Se sim, coloca a variável "venceuOJogo" como "True" e encerra o loop do jogo
            venceuOJogo = True
            break

        # Verifica quais são as casas vazias do tabuleiro
        casasVazias = mecanica.getCasasVazias()

        # Caso o tabuleiro possua casas vazias, insere um nova peça
        if casasVazias != []:
            mecanica.inserePeca(casasVazias)

        # Caso não possua, verifica se ainda têm jogadas válidas
        else:
            # Verifica se ainda tem jogadas válidas
            if mecanica.possuiMovimentosVailidos() == False:
                # Se não possuir, coloca a variável "venceuOJogo" como "False" e encerra o loop do jogo
                venceuOJogo = False
                break

    # Mostra a tela de fim de jogo
    interface.pausa(1)
    interface.limpaTela()
    interface.telaDeFimDeJogo(venceuOJogo, mecanica.getScore())

    # Reinicia a instância da mecânica do jogo
    mecanica = MecanicaDoJogo(tamanhoDoTabuleiro, objetivo)

    # Volta para o menu principal
    interface.pausa(2)
    interface.entradaDoUsuario('Aperte Enter para Voltar ao Menu Principal\n')
    main()

if __name__ == '__main__':
    main()
