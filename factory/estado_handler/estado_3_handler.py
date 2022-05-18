from domain.tipo_token import TipoToken
from domain.token import Token


class Estado3Handler:

    def __init__(self):
        pass

    def get_estado_tratado(self):
        return 3

    def handle(
            self, motor_lexico, lexema, caractere,
            set_novo_estado, set_novo_lexema, set_novo_caractere
    ):
        lexema = lexema + caractere
        set_novo_lexema(lexema)

        caractere = motor_lexico.get_char()
        set_novo_caractere(caractere)

        if caractere is None or (not caractere.isdigit()):
            motor_lexico.unget_char(caractere)
            return Token(motor_lexico.linha, TipoToken.CTE, lexema)
