from domain.tipo_token import TipoToken
from domain.token import Token
from project_utils.constants import Constants


class Estado4LexemaEhSubtracaoHandler:

    def lexema_matches(self, lexema):
        return lexema == Constants.SUBTRACAO

    def handle(self, lexema, motor_lexico):
        return Token(motor_lexico.linha, TipoToken.OPAD, lexema)
