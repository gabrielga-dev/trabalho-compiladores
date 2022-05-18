from factory.estado_caractere_handler.estado_1.estado_1_caractere_handler_factory import Estado1CaractereHandlerFactory


class Estado1Handler:

    def __init__(self):
        self.handler_caractere_factory = Estado1CaractereHandlerFactory()

    def get_estado_tratado(self):
        return 1

    def handle(
            self, motor_lexico, lexema, caractere,
            set_novo_estado, set_novo_lexema, set_novo_caractere
    ):
        # estado 1 é responsável pela primeira classificação
        caractere = motor_lexico.get_char()
        set_novo_caractere(caractere)

        resultado = self.handler_caractere_factory.handle_caractere(caractere, motor_lexico, set_novo_estado)
        if resultado is not None:
            return resultado
