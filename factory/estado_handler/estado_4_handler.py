# Nome Discente: Gabriel Guimarães de Almeida
# Matrícula: 0021722
# Data: 23/05/2022
#
# Declaro que sou o único autor e responsável por este programa. Todas as partes do programa, exceto as que foram fornecidas
# pelo professor ou copiadas do livro ou das bibliotecas de Aho et al., foram desenvolvidas por mim. Declaro também que
# sou responsável por todas as eventuais cópias deste programa e que não distribui nem facilitei a distribuição de cópias.
#
# O arquivo estado_4_handler.py comporta o "handle" do estado 4 da analise lexica
#
# Referências bibliográficas:
# Exemplos enviados pelo professor Mário
# Repositório de uma aula de SOLID feita pelo próprio Discente: https://github.com/gabrielga-dev/aula-de-SOLID
# AHO, A. V. et al. Compiladores. 2 ed. São Paulo: Pearson Addison-Wesley, 2008.


from factory.estado_caractere_handler.estado_4.estado_4_lexema_handler_factory import Estado4LexemaHandlerFactory


class Estado4Handler:
    """
    Handler do estado 4, ou seja, o que é responsável por tratar primitivos comuns
    """

    def __init__(self):
        self.lexema_handler = Estado4LexemaHandlerFactory()

    def get_estado_tratado(self):
        """
        Retorna o qual estado esse handler lida
        :return: número
        """
        return 4

    def handle(
            self, motor_lexico, lexema, caractere,
            set_novo_estado, set_novo_lexema, set_novo_caractere
    ):
        """
        Realiza o processo necessário para tratar primitivos comuns
        :param motor_lexico: objeto que auxilia a análise lexica
        :param lexema: lexema atual
        :param caractere: caractere atual
        :param set_novo_estado: função para setar um novo estado
        :param set_novo_lexema: função para setar um novo lexema
        :param set_novo_caractere: função para setar um novo caractere
        :return: Tokens, caso o handler do lexema não retorne nada, None.
        """
        lexema = lexema + caractere
        set_novo_lexema(lexema)

        return self.lexema_handler.get_lexema_handle(
            lexema
        ).handle(
            lexema, motor_lexico
        )
