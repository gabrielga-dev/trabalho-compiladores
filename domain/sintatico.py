from domain.lexico import Lexico
from domain.motor_lexico import MotorLexico
from domain.tipo_token import TipoToken
from domain.token import Token
from project_utils.mensagens_constants import MensagensConstants
from project_utils.mensagens_de_erro_constants import MensagensDeErroConstants, ERRO_AO_TENTAR_CONSUMIR


class Sintatico:

    def __init__(self):
        self.erros = []
        self.lexico = None
        self.motor_lexico = None
        self.token_atual = None

    def interpretar(self, path_arquivo):
        if self.lexico is not None:
            print(MensagensDeErroConstants.ARQUIVO_JA_ABERTO)
        else:
            self.lexico = Lexico()
            self.motor_lexico = MotorLexico(path_arquivo)
            self.motor_lexico.abre_arquivo()
            self.token_atual = self.lexico.get_token(self.motor_lexico)
            self.PROG()
            self.consome(TipoToken.FIMARQ)

            self.motor_lexico.fecha_arquivo()

            if len(self.erros) > 0:
                for erro in self.erros:
                    print(erro)
            else:
                print(MensagensConstants.PROGRAMA_ACEITO)

    def atual_igual(self, token):
        (const, msg) = token
        return self.token_atual.const == const

    def consome(self, token):
        if self.atual_igual(token):
            self.token_atual = self.get_token()
        else:
            self.erros.append(
                Token(
                    self.token_atual.linha,
                    TipoToken.ERROR,
                    '[' + self.token_atual.lexema + ']',
                    'Caracter inesperado. Esperado: ' + token[1] + ' Recebido: ' + self.token_atual.lexema
                )
            )
            self.token_atual = self.get_token()

    def PROG(self):
        self.consome(TipoToken.PROGRAMA)
        self.consome(TipoToken.ID)
        self.consome(TipoToken.PVIRG)
        self.DECLS()
        self.C_COMP()

    def DECLS(self):
        if self.atual_igual(TipoToken.VARIAVEIS):
            self.consome(TipoToken.VARIAVEIS)
            self.LIST_DECLS()
        else:
            pass

    def LIST_DECLS(self):
        self.DECL_TIPO()
        self.D()

    def D(self):
        if self.atual_igual(TipoToken.ID):
            self.LIST_DECLS()
        else:
            pass

    def DECL_TIPO(self):
        self.LIST_ID()
        self.consome(TipoToken.DPONTOS)
        self.TIPO()
        self.consome(TipoToken.PVIRG)

    def LIST_ID(self):
        self.consome(TipoToken.ID)
        self.E()

    def E(self):
        if self.atual_igual(TipoToken.VIRG):
            self.consome(TipoToken.VIRG)
            self.LIST_ID()
        else:
            pass

    def TIPO(self):
        if self.atual_igual(TipoToken.INTEIRO):
            self.consome(TipoToken.INTEIRO)
        elif self.atual_igual(TipoToken.REAL):
            self.consome(TipoToken.REAL)
        elif self.atual_igual(TipoToken.LOGICO):
            self.consome(TipoToken.LOGICO)
        else:
            self.consome(TipoToken.CARACTER)

    def C_COMP(self):
        self.consome(TipoToken.ABRECH)
        self.LISTA_COMANDOS()
        self.consome(TipoToken.FECHACH)

    def LISTA_COMANDOS(self):
        self.COMANDOS()
        self.G()

    def G(self):
        x = self.atual_igual(TipoToken.SE) or \
            self.atual_igual(TipoToken.ENQUANTO) or \
            self.atual_igual(TipoToken.LEIA) or \
            self.atual_igual(TipoToken.ESCREVA) or \
            self.atual_igual(TipoToken.ID)

        if x:
            self.LISTA_COMANDOS()

    def COMANDOS(self):
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
            self.erros.append(
                Token(
                    None,
                    TipoToken.ERROR,
                    None,
                    erro_no_sintatico=True,
                    mensagem_erro_no_sintatico=ERRO_AO_TENTAR_CONSUMIR(None)
                )
            )

    def IF(self):
        self.consome(TipoToken.SE)
        self.consome(TipoToken.ABREPAR)
        self.EXPR()
        self.consome(TipoToken.FECHAPAR)
        self.C_COMP()
        self.H()

    def H(self):
        if self.atual_igual(TipoToken.SENAO):
            self.consome(TipoToken.SENAO)
            self.C_COMP()
        else:
            pass

    def WHILE(self):
        self.consome(TipoToken.ENQUANTO)
        self.consome(TipoToken.ABREPAR)
        self.EXPR()
        self.consome(TipoToken.FECHAPAR)
        self.C_COMP()

    def READ(self):
        self.consome(TipoToken.LEIA)
        self.consome(TipoToken.ABREPAR)
        self.LIST_ID()
        self.consome(TipoToken.FECHAPAR)
        self.consome(TipoToken.PVIRG)

    def ATRIB(self):
        self.consome(TipoToken.ID)
        self.consome(TipoToken.ATRIB)
        self.EXPR()
        self.consome(TipoToken.PVIRG)

    def WRITE(self):
        self.consome(TipoToken.ESCREVA)
        self.consome(TipoToken.ABREPAR)
        self.LIST_W()
        self.consome(TipoToken.FECHAPAR)
        self.consome(TipoToken.PVIRG)

    def LIST_W(self):
        self.ELEM_W()
        self.L()

    def L(self):
        if self.atual_igual(TipoToken.VIRG):
            self.consome(TipoToken.VIRG)
            self.LIST_W()
        else:
            pass

    def ELEM_W(self):
        if self.atual_igual(TipoToken.CADEIA):
            self.consome(TipoToken.CADEIA)
        else:
            self.EXPR()

    def EXPR(self):
        self.SIMPLES()
        self.P()

    def P(self):
        if self.atual_igual(TipoToken.OPREL):
            self.consome(TipoToken.OPREL)
            self.SIMPLES()
        else:
            pass

    def SIMPLES(self):
        self.TERMO()
        self.R()

    def R(self):
        if self.atual_igual(TipoToken.OPAD):
            self.consome(TipoToken.OPAD)
            self.SIMPLES()
        else:
            pass

    def TERMO(self):
        self.FAT()
        self.S()

    def S(self):
        if self.atual_igual(TipoToken.OPMUL):
            self.consome(TipoToken.OPMUL)
            self.TERMO()
        else:
            pass

    def FAT(self):
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
                Token(
                    None,
                    TipoToken.ERROR,
                    None,
                    erro_no_sintatico=True,
                    mensagem_erro_no_sintatico=ERRO_AO_TENTAR_CONSUMIR('FAT')
                )
            )

    def get_token(self):
        new_token = self.lexico.get_token(self.motor_lexico)
        if new_token.tipo == TipoToken.ERROR:
            self.erros.append(new_token)
            return self.get_token()
        else:
            return new_token
