class Estado6Handler:
    """
    Handler do estado 6, ou seja, o que é responsável por consumir comentários de linha
    """

    def __init__(self):
        pass

    def get_estado_tratado(self):
        """
        Retorna o qual estado esse handler lida
        :return: número
        """
        return 6

    def handle(
            self, motor_lexico, lexema, caractere,
            set_novo_estado, set_novo_lexema, set_novo_caractere
    ):
        """
        Realiza o processo necessário para consumir comentários de linha
        :param motor_lexico: objeto que auxilia a análise lexica
        :param lexema: lexema atual
        :param caractere: caractere atual
        :param set_novo_estado: função para setar um novo estado
        :param set_novo_lexema: função para setar um novo lexema
        :param set_novo_caractere: função para setar um novo caractere
        :return: None.
        """
        while (caractere is not None) and (caractere != '\n'):
            caractere = motor_lexico.get_caractere()
            set_novo_caractere(caractere)
        set_novo_estado(1)

