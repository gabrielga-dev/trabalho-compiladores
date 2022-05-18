from domain.tipo_token import TipoToken
from domain.token import Token


class Estado1CaractereEhNoneHandler:

    def caractere_matches(self, motor_lexico, caractere):
        return caractere is None

    def handle(self, caractere, motor_lexico, set_novo_estado):
        return Token(motor_lexico.linha, TipoToken.FIMARQ, 'fda')
