from domain.tipo_token import TipoToken
from domain.token import Token
from project_utils.constants import Constants


class Estado1CaractereEhMenorQueSeguidoDeMaiorQueHandler:

    def caractere_matches(self, motor_lexico, caractere):
        return caractere == Constants.MENOR_QUE and motor_lexico.prox_char() == Constants.MAIOR_QUE

    def handle(self, caractere, motor_lexico, set_novo_estado):
        return Token(motor_lexico.linha, TipoToken.OPREL, caractere + motor_lexico.get_char())
