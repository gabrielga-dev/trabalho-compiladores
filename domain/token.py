class Token:
    def __init__(
            self,
            linha,
            tipo,
            lexema,
            mensagem_auxiliar=None,
            erro_no_sintatico=False,
            mensagem_erro_no_sintatico=None
    ):
        self.linha = linha
        self.tipo = tipo
        (const, msg) = tipo
        self.const = const
        if mensagem_auxiliar is None:
            self.msg = msg
        else:
            self.msg = mensagem_auxiliar
        self.lexema = lexema
        self.erro_no_sintatico = erro_no_sintatico
        self.mensagem_erro_no_sintatico = mensagem_erro_no_sintatico

    def __str__(self):
        if self.erro_no_sintatico:
            return 'Token(Erro na etapa sintática, tipo=' + self.tipo[1] + ', msg=' + self.mensagem_erro_no_sintatico\
                   + ') '

        return '\tToken(linha=' + str(self.linha) + ', tipo=' + self.tipo[1] + ', const=' + str(self.const) + ', msg=' + \
               self.msg + ', lexema=' + self.lexema + ')'
