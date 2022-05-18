from domain.tipo_token import TipoToken
from domain.token import Token
from project_utils.constants import Constants


class Estado5Handler:

    def __init__(self):
        pass

    def get_estado_tratado(self):
        return 5

    def handle(
            self, motor_lexico, lexema, caractere,
            set_novo_estado, set_novo_lexema, set_novo_caractere
    ):
        lexema = lexema + caractere
        set_novo_lexema(lexema)

        caractere = motor_lexico.get_char()
        set_novo_caractere(caractere)

        lexema = lexema + caractere
        set_novo_lexema(lexema)

        while (caractere is not None) and (caractere != Constants.ASPAS_DUPLAS):
            caractere = motor_lexico.get_char()
            set_novo_caractere(caractere)

            lexema = lexema + caractere
            set_novo_lexema(lexema)
        return Token(motor_lexico.linha, TipoToken.CADEIA, lexema)

