from domain.tipo_token import TipoToken
from domain.token import Token
from project_utils.constants import Constants


class Estado1CaractereEhMenorQueSeguidoDeMaiorQueHandler:
    """
    Handler do caractere do estado 1 da análise léxica, o qual verifica se o caractere é "<="
    """

    def caractere_matches(self, motor_lexico, caractere):
        """
        Esta função verifica se o caractere é lidado pelo handler
        :param motor_lexico: objeto que auxilia a análise léxica
        :param caractere: caractere atual
        :return: booleando
        """
        return caractere == Constants.MENOR_QUE and motor_lexico.prox_char() == Constants.MAIOR_QUE

    def handle(self, caractere, motor_lexico, set_novo_estado):
        """
        Realiza tratamento do caractere
        :param caractere: caractere atual
        :param motor_lexico: objeto que auxilia a análise léxica
        :param set_novo_estado: função que seta o novo estado
        :return: Token
        """
        return Token(motor_lexico.linha, TipoToken.OPREL, caractere + motor_lexico.get_caractere())
