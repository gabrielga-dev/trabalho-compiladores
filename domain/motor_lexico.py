from os import path


class MotorLexico:

    global linha

    def __init__(self, path_arquivo):
        self.linha = 1
        self.path_arquivo = path_arquivo
        self.arquivo = None
        # buffer de entrada
        self.buffer = ''

    def abre_arquivo(self):
        if self.arquivo is not None:
            print('ERRO: Arquivo ja aberto')
            quit()
        elif path.exists(self.path_arquivo):
            self.arquivo = open(self.path_arquivo, "r")
        else:
            print('ERRO: Arquivo "%s" inexistente.' % self.path_arquivo)
            quit()

    def fecha_arquivo(self):
        if self.arquivo is None:
            print('ERRO: Nao ha arquivo aberto')
            quit()
        else:
            self.arquivo.close()

    def get_char(self):
        if self.arquivo is None:
            print('ERRO: Nao ha arquivo aberto')
            quit()
        elif len(self.buffer) > 0:
            c = self.buffer[0]
            self.buffer = self.buffer[1:]
            return c
        else:
            c = self.arquivo.read(1)

            if c == '\n':
                self.linha = self.linha + 1

            if len(c) == 0:
                return None
            else:
                return c.lower()

    def unget_char(self, c):
        if c is not None:
            self.buffer = self.buffer + c

    def prox_char(self):
        c = self.get_char()
        self.unget_char(c)
        return c

