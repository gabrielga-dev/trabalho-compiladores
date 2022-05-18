from domain.tipo_token import TipoToken
from domain.token import Token
from project_utils.constants import Constants


class Estado1CaractereEhMaiorQueSeguidoDeIgualdadeHandler:

    def caractere_matches(self, motor_lexico, caractere):
        return caractere == Constants.MAIOR_QUE and motor_lexico.prox_char() == Constants.IGUAL

    def handle(self, caractere, motor_lexico, set_novo_estado):
        return Token(motor_lexico.linha, TipoToken.OPREL, caractere + motor_lexico.get_char())
