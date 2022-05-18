from domain.tipo_token import TipoToken
from domain.token import Token
from project_utils.constants import Constants


class Estado1CaractereEhDoisPontosSeguidoDeIgualdadeHandler:

    def caractere_matches(self, motor_lexico, caractere):
        return caractere == Constants.DOIS_PONTOS and motor_lexico.prox_char() == Constants.IGUAL

    def handle(self, caractere, motor_lexico, set_novo_estado):
        return Token(motor_lexico.linha, TipoToken.ATRIB, caractere + motor_lexico.get_char())
