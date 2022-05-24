# Nome Discente: Gabriel Guimarães de Almeida
# Matrícula: 0021722
# Data: 23/05/2022
#
# Declaro que sou o único autor e responsável por este programa. Todas as partes do programa, exceto as que foram fornecidas
# pelo professor ou copiadas do livro ou das bibliotecas de Aho et al., foram desenvolvidas por mim. Declaro também que
# sou responsável por todas as eventuais cópias deste programa e que não distribui nem facilitei a distribuição de cópias.
#
# O arquivo lexico.py comporta a implementação necessária de um analisador sintático para a linguagem do trabalho prático.
# A classe Sintatico é responsável pela análise sintática do compilador. Suas funções principais são: interpretar(), a qual
# recebe o path do arquivo que possui o código a ser analisado, e a função consome(), que é responsável por consumir os
# não-terminais da gramatica e verificar a existência de erros.
#
# Referências bibliográficas:
# Exemplos enviados pelo professor Mário
# Repositório de uma aula de SOLID feita pelo próprio Discente: https://github.com/gabrielga-dev/aula-de-SOLID
# AHO, A. V. et al. Compiladores. 2 ed. São Paulo: Pearson Addison-Wesley, 2008.

from domain.lexico import Lexico
from domain.motor_lexico import MotorLexico
from domain.tipo_token import TipoToken
from domain.token import Token
from project_utils.mensagens_de_erro_constants import MensagensDeErroConstants, ERRO_AO_TENTAR_CONSUMIR


class Sintatico:
    """
    Esta classe realiza o processo de análise sintática e, para ela conseguir fazer isso é necessário isntanciar um
    objeto e chamar a função "interpretar".
    """

    def __init__(self):
        self.erros = []
        self.lexico = None
        self.motor_lexico = None
        self.token_atual = None
        self.buffer_de_token = None

    def interpretar(self, path_arquivo):
        """
        Essa função executa a análise sintática juntamente com a lexica.
        :param path_arquivo: string com o caminho até o arquivo que contém a palavra a ser analisada
        :return: Tupla composta por um booleano e um array de erros
        """
        if self.lexico is not None:
            return False, [
                Token(
                    None,
                    TipoToken.ERROR,
                    None,
                    erro_no_sintatico=True,
                    mensagem_erro_no_sintatico=MensagensDeErroConstants.ERROR_MESSAGE_ARQUIVO_JA_ABERTO
                )
            ]
        else:
            self.lexico = Lexico()
            self.motor_lexico = MotorLexico(path_arquivo)
            self.motor_lexico.abre_arquivo()
            self.token_atual = self.lexico.get_token(self.motor_lexico)
            self.PROG()
            self.consome(TipoToken.FIMARQ)

            self.motor_lexico.fecha_arquivo()

            if len(self.erros) > 0:
                return False, self.erros
            else:
                return True, self.erros

    def atual_igual(self, tipo_token):
        """
        Verifica se o tipo do token passado é igual ao do token atual da classe
        :param tipo_token: TipoToken a ser verificado
        :return: Booleano
        """
        try:
            (const, msg) = tipo_token
        except:
            const = tipo_token.const
        return self.token_atual.const == const

    def consome(self, tipo_token):
        """
        Esta função verifica se o tipo_token tem atuação igual ao token atual. Se sim, continua o processamento, se não,
        adiciona um erro na lista de erros.
        :param tipo_token:
        :return:
        """
        if self.atual_igual(tipo_token):
            # se tiver algum token no buffer, ele é consumido
            if self.buffer_de_token is not None:
                self.token_atual = self.buffer_de_token
                self.buffer_de_token = None
            else:
                self.token_atual = self.get_token()
        else:
            (const, mensagem) = tipo_token
            self.erros.append(
                'ERRO NO SINTÁTICO! (Linha %d) Caractere inesperado. Esperado: %s, Recebido: %s' % (
                    self.token_atual.linha,
                    mensagem,
                    self.token_atual.lexema
                )
            )
            token = self.get_token()
            if const == token.const:
                # se próximo token é igual ao que foi consumido, então ele é ignorado e a execução continua
                self.token_atual = self.get_token()
            else:
                # e próximo token não é igual ao que foi consumido, guarda ele no buffer de tokens
                self.buffer_de_token = token

    def PROG(self):
        """
        Função do não-terminal PROG
        :return: None
        """
        self.consome(TipoToken.PROGRAMA)
        self.consome(TipoToken.ID)
        self.consome(TipoToken.PVIRG)
        self.DECLS()
        self.C_COMP()

    def DECLS(self):
        """
        Função do não-terminal DECLS
        :return: None
        """
        if self.atual_igual(TipoToken.VARIAVEIS):
            self.consome(TipoToken.VARIAVEIS)
            self.LIST_DECLS()
        else:
            pass

    def LIST_DECLS(self):
        """
        Função do não-terminal LIST-DECLS
        :return: None
        """
        self.DECL_TIPO()
        self.D()

    def D(self):
        """
        Função do não-terminal D
        :return: None
        """
        if self.atual_igual(TipoToken.ID):
            self.LIST_DECLS()
        else:
            pass

    def DECL_TIPO(self):
        """
        Função do não-terminal DECL-TIPO
        :return: None
        """
        self.LIST_ID()
        self.consome(TipoToken.DPONTOS)
        self.TIPO()
        self.consome(TipoToken.PVIRG)

    def LIST_ID(self):
        """
        Função do não-terminal LIST-ID
        :return: None
        """
        self.consome(TipoToken.ID)
        self.E()

    def E(self):
        """
        Função do não-terminal E
        :return: None
        """
        if self.atual_igual(TipoToken.VIRG):
            self.consome(TipoToken.VIRG)
            self.LIST_ID()
        else:
            pass

    def TIPO(self):
        """
        Função do não-terminal TIPO
        :return: None
        """
        if self.atual_igual(TipoToken.INTEIRO):
            self.consome(TipoToken.INTEIRO)
        elif self.atual_igual(TipoToken.REAL):
            self.consome(TipoToken.REAL)
        elif self.atual_igual(TipoToken.LOGICO):
            self.consome(TipoToken.LOGICO)
        elif self.atual_igual(TipoToken.CARACTER):
            self.consome(TipoToken.CARACTER)
        else:
            self.erros.append(
                'ERRO NO SINTÁTICO! (linha %d): Era esperado uma tipagem.' % (
                    self.token_atual.linha
                )
            )

    def C_COMP(self):
        """
        Função do não-terminal C-COMP
        :return: None
        """
        self.consome(TipoToken.ABRECH)
        self.LISTA_COMANDOS()
        self.consome(TipoToken.FECHACH)

    def LISTA_COMANDOS(self):
        """
        Função do não-terminal LISTA-COMANDOS
        :return: None
        """
        self.COMANDOS()
        self.G()

    def G(self):
        """
        Função do não-terminal G
        :return: None
        """
        x = self.atual_igual(TipoToken.SE) or \
            self.atual_igual(TipoToken.ENQUANTO) or \
            self.atual_igual(TipoToken.LEIA) or \
            self.atual_igual(TipoToken.ESCREVA) or \
            self.atual_igual(TipoToken.ID)

        if x:
            self.LISTA_COMANDOS()

    def COMANDOS(self):
        """
        Função do não-terminal COMANDOS
        :return: None
        """
        if self.atual_igual(TipoToken.SE):
            self.IF()
        elif self.atual_igual(TipoToken.ENQUANTO):
            self.WHILE()
        elif self.atual_igual(TipoToken.LEIA):
            self.READ()
        elif self.atual_igual(TipoToken.ESCREVA):
            self.WRITE()
        elif self.atual_igual(TipoToken.ID):
            self.ATRIB()
        else:
            self.erros.append('ERRO NO SINTÁTICO! (linha %d): COMANDOS não foi encontrado encontrados' % (
                    self.token_atual.linha
                )
          )

    def IF(self):
        """
        Função do não-terminal IF
        :return: None
        """
        self.consome(TipoToken.SE)
        self.consome(TipoToken.ABREPAR)
        self.EXPR()
        self.consome(TipoToken.FECHAPAR)
        self.C_COMP()
        self.H()

    def H(self):
        """
        Função do não-terminal H
        :return: None
        """
        if self.atual_igual(TipoToken.SENAO):
            self.consome(TipoToken.SENAO)
            self.C_COMP()
        else:
            self.erros.append(
                'ERRO NO SINTÁTICO! (linha %d): Esperado: %s, Recebido: %s' % (
                    self.token_atual.linha,
                    TipoToken.SENAO[1],
                    self.token_atual.lexema
                )
            )
            self.C_COMP()

    def WHILE(self):
        """
        Função do não-terminal WHILE
        :return: None
        """
        self.consome(TipoToken.ENQUANTO)
        self.consome(TipoToken.ABREPAR)
        self.EXPR()
        self.consome(TipoToken.FECHAPAR)
        self.C_COMP()

    def READ(self):
        """
        Função do não-terminal READ
        :return: None
        """
        self.consome(TipoToken.LEIA)
        self.consome(TipoToken.ABREPAR)
        self.LIST_ID()
        self.consome(TipoToken.FECHAPAR)
        self.consome(TipoToken.PVIRG)

    def ATRIB(self):
        """
        Função do não-terminal ATRIB
        :return: None
        """
        self.consome(TipoToken.ID)
        self.consome(TipoToken.ATRIB)
        self.EXPR()
        self.consome(TipoToken.PVIRG)

    def WRITE(self):
        """
        Função do não-terminal WRITE
        :return: None
        """
        self.consome(TipoToken.ESCREVA)
        self.consome(TipoToken.ABREPAR)
        self.LIST_W()
        self.consome(TipoToken.FECHAPAR)
        self.consome(TipoToken.PVIRG)

    def LIST_W(self):
        """
        Função do não-terminal LIST-W
        :return: None
        """
        self.ELEM_W()
        self.L()

    def L(self):
        """
        Função do não-terminal L
        :return: None
        """
        if self.atual_igual(TipoToken.VIRG):
            self.consome(TipoToken.VIRG)
            self.LIST_W()
        else:
            pass

    def ELEM_W(self):
        """
        Função do não-terminal ELEM-W
        :return: None
        """
        if self.atual_igual(TipoToken.CADEIA):
            self.consome(TipoToken.CADEIA)
        else:
            self.EXPR()

    def EXPR(self):
        """
        Função do não-terminal EXPR
        :return: None
        """
        self.SIMPLES()
        self.P()

    def P(self):
        """
        Função do não-terminal P
        :return: None
        """
        if self.atual_igual(TipoToken.OPREL):
            self.consome(TipoToken.OPREL)
            self.SIMPLES()
        else:
            pass

    def SIMPLES(self):
        """
        Função do não-terminal SIMPLES
        :return: None
        """
        self.TERMO()
        self.R()

    def R(self):
        """
        Função do não-terminal R
        :return: None
        """
        if self.atual_igual(TipoToken.OPAD):
            self.consome(TipoToken.OPAD)
            self.SIMPLES()
        else:
            pass

    def TERMO(self):
        """
        Função do não-terminal TERMO
        :return: None
        """
        self.FAT()
        self.S()

    def S(self):
        """
        Função do não-terminal S
        :return: None
        """
        if self.atual_igual(TipoToken.OPMUL):
            self.consome(TipoToken.OPMUL)
            self.TERMO()
        else:
            pass

    def FAT(self):
        """
        Função do não-terminal FAT
        :return: None
        """
        if self.atual_igual(TipoToken.ID):
            self.consome(TipoToken.ID)
        elif self.atual_igual(TipoToken.CTE):
            self.consome(TipoToken.CTE)
        elif self.atual_igual(TipoToken.ABREPAR):
            self.consome(TipoToken.ABREPAR)
            self.EXPR()
            self.consome(TipoToken.FECHAPAR)
        elif self.atual_igual(TipoToken.VERDADEIRO):
            self.consome(TipoToken.VERDADEIRO)
        elif self.atual_igual(TipoToken.FALSO):
            self.consome(TipoToken.FALSO)
        elif self.atual_igual(TipoToken.OPNEG):
            self.consome(TipoToken.OPNEG)
            self.FAT()
        else:
            self.erros.append(
                'ERRO NO SINTÁTICO! (linha %d) Argumentos não encontrados' % (
                    self.token_atual.linha
                )
            )

    def get_token(self):
        """
        Esta função retorna o token gerado pelo lexico
        :return: Token
        """
        new_token = self.lexico.get_token(self.motor_lexico)
        if new_token.tipo == TipoToken.ERROR:
            self.erros.append(
                'ERRO NO LÉXICO! (linha %d): %s' % (
                    new_token.linha, new_token.msg
                )
            )
            # aqui entra o MODO PÂNICO
            return self.get_token()
        else:
            return new_token
