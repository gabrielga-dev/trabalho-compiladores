from project_utils.constants import Constants


class Estado1CaractereEhAspasDuplasHandler:

    def caractere_matches(self, motor_lexico, caractere):
        return caractere == Constants.ASPAS_DUPLAS

    def handle(self, caractere, motor_lexico, set_novo_estado):
        set_novo_estado(5)
        return None
