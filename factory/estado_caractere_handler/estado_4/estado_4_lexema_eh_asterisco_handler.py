from domain.tipo_token import TipoToken
from domain.token import Token
from project_utils.constants import Constants


class Estado4LexemaEhAteriscoHandler:

    def lexema_matches(self, lexema):
        return lexema == Constants.ASTERISCO

    def handle(self, lexema, motor_lexico):
        return Token(motor_lexico.linha, TipoToken.OPMUL, lexema)
