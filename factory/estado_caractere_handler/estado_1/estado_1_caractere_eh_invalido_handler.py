from domain.tipo_token import TipoToken
from domain.token import Token


class Estado1CaractereEhInvalidoHandler:
    """
    Handler do caractere do estado 1 da análise léxica, o qual verifica se o caractere é inválido
    """

    def caractere_matches(self, motor_lexico, caractere):
        """
        Este handler sempre é chamado quando nenum handler encaixa com o caractere
        :param motor_lexico: objeto que auxilia a análise léxica
        :param caractere: caractere atual
        :return: True
        """
        return True

    def handle(self, caractere, motor_lexico, set_novo_estado):
        """
        Realiza tratamento do caractere
        :param caractere: caractere atual
        :param motor_lexico: objeto que auxilia a análise léxica
        :param set_novo_estado: função que seta o novo estado
        :return: Token de Erro
        """
        return Token(motor_lexico.linha, TipoToken.ERROR, '[' + caractere + ']', 'Caracter inválido ' + caractere)
