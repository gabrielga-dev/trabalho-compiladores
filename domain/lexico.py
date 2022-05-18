from factory.estado_handler.estado_handler_factory import EstadoHandlerFactory


class Lexico:

    def __init__(self):
        self.handler_factory = EstadoHandlerFactory()
        self.estado = 1
        self.lexema = ''
        self.caractere = None

    def set_estado(self, novo_estado):
        self.estado = novo_estado

    def set_lexema(self, novo_lexema):
        self.lexema = novo_lexema

    def set_caractere(self, novo_caractere):
        self.caractere = novo_caractere

    def get_token(self, motor_lexico):
        self.estado = 1
        self.lexema = ''
        self.caractere = None
        while True:
            retorno = self.handler_factory.get_estado_handler(
                self.estado
            ).handle(
                motor_lexico, self.lexema, self.caractere,
                self.set_estado, self.set_lexema, self.set_caractere
            )
            if retorno is not None:
                return retorno
