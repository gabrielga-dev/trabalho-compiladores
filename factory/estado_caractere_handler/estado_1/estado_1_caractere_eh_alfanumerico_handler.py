class Estado1CaractereEhAlfanumericoHandler:

    def caractere_matches(self, motor_lexico, caractere):
        return (caractere is not None) and caractere.isalpha()

    def handle(self, caractere, motor_lexico, set_novo_estado):
        set_novo_estado(2)
        return None
