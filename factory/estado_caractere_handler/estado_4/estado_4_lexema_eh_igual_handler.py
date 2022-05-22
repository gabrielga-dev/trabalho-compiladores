from domain.tipo_token import TipoToken
from domain.token import Token
from project_utils.constants import Constants


class Estado4LexemaEhIgualdadeHandler:
    """
    Handler de lexema do estado 4. Este verifica se o lexema é "="
    """

    def lexema_matches(self, lexema):
        """
        Esta função realiza a verificação se o lexema é lidado por este handler
        :param lexema: lexema atual
        :return: booleano
        """
        return lexema == Constants.IGUAL

    def handle(self, lexema, motor_lexico):
        """
        Esta função realiza o tratamento do lexema
        :param lexema: lexema atual
        :param motor_lexico: objeto que auxilia a análise lexica
        :return: Token
        """
        return Token(motor_lexico.linha, TipoToken.OPREL, lexema)
