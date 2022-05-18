from project_utils.constants import Constants


class Estado1CaractereEhIgnoravelHandler:

    def caractere_matches(self, motor_lexico, caractere):
        return caractere in Constants.CARACTERES_IGNORAVEIS

    def handle(self, caractere, motor_lexico, set_novo_estado):
        return None
