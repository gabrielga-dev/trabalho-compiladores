from domain.tipo_token import TipoToken
from domain.token import Token


class Estado1CaractereEhInvalidoHandler:

    def caractere_matches(self, motor_lexico, caractere):
        return True

    def handle(self, caractere, motor_lexico, set_novo_estado):
        return Token(motor_lexico.linha, TipoToken.ERROR, '[' + caractere + ']', 'Caracter inválido ' + caractere)
