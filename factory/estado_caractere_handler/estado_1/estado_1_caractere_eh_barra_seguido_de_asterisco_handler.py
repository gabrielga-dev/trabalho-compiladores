from project_utils.constants import Constants


class Estado1CaractereEhBarraSeguidoDeEsteriscoHandler:

    def caractere_matches(self, motor_lexico, caractere):
        return caractere == Constants.BARRA and motor_lexico.prox_char() == Constants.ASTERISCO

    def handle(self, caractere, motor_lexico, set_novo_estado):
        set_novo_estado(7)
        return None
