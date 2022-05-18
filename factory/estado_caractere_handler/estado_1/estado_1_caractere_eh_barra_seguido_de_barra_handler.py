from project_utils.constants import Constants


class Estado1CaractereEhBarraSeguidoDeBarraHandler:

    def caractere_matches(self, motor_lexico, caractere):
        return caractere == Constants.BARRA and motor_lexico.prox_char() == Constants.BARRA

    def handle(self, caractere, motor_lexico, set_novo_estado):
        set_novo_estado(6)
        return None
