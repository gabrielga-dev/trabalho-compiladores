from domain.palavras_reservadas import PALAVRAS_RESERVADAS as PalavrasReservadas
from domain.tipo_token import TipoToken
from domain.token import Token
from project_utils.constants import Constants


class Estado2Handler:

    def __init__(self):
        pass

    def get_estado_tratado(self):
        return 2

    def handle(
            self, motor_lexico, lexema, caractere,
            set_novo_estado, set_novo_lexema, set_novo_caractere
    ):
        # estado que trata identificadores e palavras reservada
        lexema = lexema + caractere
        set_novo_lexema(lexema)

        caractere = motor_lexico.get_char()
        set_novo_caractere(caractere)

        if caractere is None or (not caractere.isalnum()):
            motor_lexico.unget_char(caractere)
            if lexema in PalavrasReservadas:
                return Token(motor_lexico.linha, PalavrasReservadas[lexema], lexema)
            elif len(lexema) > Constants.TAMANHO_MAXIMO_IDENTIFICADOR:
                return Token(motor_lexico.linha, TipoToken.ERROR, '[ identificador com mais de 16 dig. ]')
            else:
                return Token(motor_lexico.linha, TipoToken.ID, lexema)
