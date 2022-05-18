from domain.tipo_token import TipoToken
from domain.token import Token
from project_utils.constants import Constants


class Estado7Handler:

    def __init__(self):
        pass

    def get_estado_tratado(self):
        return 7

    def handle(
            self, motor_lexico, lexema, caractere,
            set_novo_estado, set_novo_lexema, set_novo_caractere
    ):
        # consome comentário de bloco
        while caractere is not None:
            caractere = motor_lexico.get_char()
            set_novo_caractere(caractere)

            if caractere == Constants.ASTERISCO and motor_lexico.get_char() == Constants.BARRA:
                break
        if motor_lexico.get_char() is None:
            return Token(motor_lexico.linha, TipoToken.ERROR, 'Bloco de comentário aberto e não fechado')
        set_novo_estado(1)

