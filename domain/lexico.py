# Nome Discente: Gabriel Guimarães de Almeida
# Matrícula: 0021722
# Data: 23/05/2022
#
# Declaro que sou o único autor e responsável por este programa. Todas as partes do programa, exceto as que foram fornecidas
# pelo professor ou copiadas do livro ou das bibliotecas de Aho et al., foram desenvolvidas por mim. Declaro também que
# sou responsável por todas as eventuais cópias deste programa e que não distribui nem facilitei a distribuição de cópias.
#
# O arquivo lexico.py comporta a chamada de toda implementaçã necessária de um analisador léxico para a linguagem do trabalho prático.
# A classe Lexico é responsável "segurar" o estado, lexema e caractere atual da compilação.
#
# Referências bibliográficas:
# Exemplos enviados pelo professor Mário
# Repositório de uma aula de SOLID feita pelo próprio Discente: https://github.com/gabrielga-dev/aula-de-SOLID
# AHO, A. V. et al. Compiladores. 2 ed. São Paulo: Pearson Addison-Wesley, 2008.

from factory.estado_handler.estado_handler_factory import EstadoHandlerFactory


class Lexico:
    """
    Esta classe realiza a análise léxica
    """

    def __init__(self):
        self.handler_factory = EstadoHandlerFactory()
        self.estado = 1
        self.lexema = ''
        self.caractere = None

    def set_estado(self, novo_estado):
        """
        Setter do novo estado
        :param novo_estado: novo estado a ser setado
        :return: None
        """
        self.estado = novo_estado

    def set_lexema(self, novo_lexema):
        """
        Setter do novo lexema
        :param novo_lexema: novo lexema a ser setado
        :return: None
        """
        self.lexema = novo_lexema

    def set_caractere(self, novo_caractere):
        """
        Setter do novo caractere
        :param novo_caractere: novo caractere a ser setado
        :return: None
        """
        self.caractere = novo_caractere

    def get_token(self, motor_lexico):
        """
        Essa função recebe o motor_lexico, objeto que auxilia a execução da análise lexica, e realiza o chamado dos
        handlers corretos de cada estado
        :param motor_lexico: objeto que auxilia a execução da análise lexica
        :return: Tokens
        """
        self.estado = 1
        self.lexema = ''
        self.caractere = None
        while True:
            retorno = self.handler_factory.get_estado_handler(
                self.estado
            ).handle(
                motor_lexico, self.lexema, self.caractere,
                self.set_estado, self.set_lexema, self.set_caractere
            )
            if retorno is not None:
                return retorno
