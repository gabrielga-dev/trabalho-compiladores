from domain.tipo_token import TipoToken
from domain.token import Token


class Estado1CaractereEhNoneHandler:
    """
    Handler do caractere do estado 1 da análise léxica, o qual verifica se o caractere é None
    """

    def caractere_matches(self, motor_lexico, caractere):
        """
        Esta função verifica se o caractere é lidado pelo handler
        :param motor_lexico: objeto que auxilia a análise léxica
        :param caractere: caractere atual
        :return: booleando
        """
        return caractere is None

    def handle(self, caractere, motor_lexico, set_novo_estado):
        """
        Realiza tratamento do caractere
        :param caractere: caractere atual
        :param motor_lexico: objeto que auxilia a análise léxica
        :param set_novo_estado: função que seta o novo estado
        :return: Token
        """
        return Token(motor_lexico.linha, TipoToken.FIMARQ, 'fda')
