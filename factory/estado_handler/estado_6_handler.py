class Estado6Handler:

    def __init__(self):
        pass

    def get_estado_tratado(self):
        return 6

    def handle(
            self, motor_lexico, lexema, caractere,
            set_novo_estado, set_novo_lexema, set_novo_caractere
    ):
        # consome comentário de linha
        while (caractere is not None) and (caractere != '\n'):
            caractere = motor_lexico.get_char()
            set_novo_caractere(caractere)
        set_novo_estado(1)

