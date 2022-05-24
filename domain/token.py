class Token:
    """
    Esta classe representa os tokens
    """
    def __init__(
            self,
            linha,
            tipo_token,
            lexema,
            mensagem_auxiliar=None
    ):
        self.linha = linha
        self.tipo = tipo_token
        (const, msg) = tipo_token
        self.const = const
        if mensagem_auxiliar is None:
            self.msg = msg
        else:
            self.msg = mensagem_auxiliar
        self.lexema = lexema

    def __str__(self):

        return '\tlinha=' + str(self.linha) + ', const=' + str(self.const) + ', msg=' + self.msg + \
               ', lexema=' + self.lexema
