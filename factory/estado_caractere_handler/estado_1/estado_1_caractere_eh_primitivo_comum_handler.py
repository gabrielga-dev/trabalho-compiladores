from project_utils.constants import Constants


class Estado1CaractereEhPrimitivoComumHandler:

    def caractere_matches(self, motor_lexico, caractere):
        return caractere in Constants.PRIMITIVOS_COMUNS

    def handle(self, caractere, motor_lexico, set_novo_estado):
        set_novo_estado(4)
        return None
