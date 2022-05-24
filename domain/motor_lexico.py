# Nome Discente: Gabriel Guimarães de Almeida
# Matrícula: 0021722
# Data: 23/05/2022
#
# Declaro que sou o único autor e responsável por este programa. Todas as partes do programa, exceto as que foram fornecidas
# pelo professor ou copiadas do livro ou das bibliotecas de Aho et al., foram desenvolvidas por mim. Declaro também que
# sou responsável por todas as eventuais cópias deste programa e que não distribui nem facilitei a distribuição de cópias.
#
# O arquivo motor_lexico.py comporta a toda a lógica necessária para extrair informações do arquivo que contém o código
# a ser analisado
#
# Referências bibliográficas:
# Exemplos enviados pelo professor Mário
# Repositório de uma aula de SOLID feita pelo próprio Discente: https://github.com/gabrielga-dev/aula-de-SOLID
# AHO, A. V. et al. Compiladores. 2 ed. São Paulo: Pearson Addison-Wesley, 2008.

from os import path

from project_utils.mensagens_de_erro_constants import MensagensDeErroConstants

class MotorLexico:
    """
    Esta classe auxilia a análise lexica com operações diretas no arquivo que contém o programa
    """

    global linha

    def __init__(self, path_arquivo):
        self.linha = 1
        self.path_arquivo = path_arquivo
        self.arquivo = None
        self.buffer = ''

    def abre_arquivo(self):
        """
        Esta função abre o arquivo que foi passado no construtor da classe
        :return: None
        """
        if self.arquivo is not None:
            print(MensagensDeErroConstants.ERROR_MESSAGE_ARQUIVO_JA_ABERTO)
            quit()
        elif path.exists(self.path_arquivo):
            self.arquivo = open(self.path_arquivo, "r")
        else:
            print(MensagensDeErroConstants.ERROR_MESSAGE_ARQUIVO_INEXISTENTE)
            quit()

    def fecha_arquivo(self):
        """
        Esta função fecha o arquivo
        :return: None
        """
        if self.arquivo is None:
            print(MensagensDeErroConstants.ERROR_MESSAGE_ARQUIVO_NAO_ABERTO)
            quit()
        else:
            self.arquivo.close()

    def get_caractere(self):
        """
        Esta função realiza a captura do próximo caractere no arquivo
        :return: None
        """
        if self.arquivo is None:
            print(MensagensDeErroConstants.ERROR_MESSAGE_ARQUIVO_NAO_ABERTO)
            quit()
        elif len(self.buffer) > 0:
            c = self.buffer[0]
            self.buffer = self.buffer[1:]
            return c
        else:
            c = self.arquivo.read(1)

            if c == '\n':
                self.linha = self.linha + 1

            if len(c) == 0:
                return None
            else:
                return c.lower()

    def unget_caractere(self, caractere):
        """
        Esta função devolve o caractere passado ao buffer
        :param caractere: caractere a ser devolvido ao buffer
        :return: None 
        """
        if caractere is not None:
            self.buffer = self.buffer + caractere

    def prox_char(self):
        """
        Esta função busca o próximo caractere
        :return: char, o próximo caractere
        """
        prox_caractere = self.get_caractere()
        self.unget_caractere(prox_caractere)
        return prox_caractere

