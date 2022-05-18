class Estado1CaractereEhDigitoHandler:

    def caractere_matches(self, motor_lexico, caractere):
        return (caractere is not None) and caractere.isdigit()

    def handle(self, caractere, motor_lexico, set_novo_estado):
        set_novo_estado(3)
        return None
