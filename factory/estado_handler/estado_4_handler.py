from factory.estado_caractere_handler.estado_4.estado_4_lexema_handler_factory import Estado4LexemaHandlerFactory


class Estado4Handler:

    def __init__(self):
        self.lexema_handler = Estado4LexemaHandlerFactory()

    def get_estado_tratado(self):
        return 4

    def handle(
            self, motor_lexico, lexema, caractere,
            set_novo_estado, set_novo_lexema, set_novo_caractere
    ):
        # estado que trata outros tokens primitivos comuns
        lexema = lexema + caractere
        set_novo_lexema(lexema)

        return self.lexema_handler.handle_lexema(lexema, motor_lexico)
