from domain.tipo_token import TipoToken
from domain.token import Token
from project_utils.constants import Constants


class Estado5Handler:
    """
    Handler do estado 5, ou seja, o que é responsável por tratar cadeias
    """

    def __init__(self):
        pass

    def get_estado_tratado(self):
        """
        Retorna o qual estado esse handler lida
        :return: número
        """
        return 5

    def handle(
            self, motor_lexico, lexema, caractere,
            set_novo_estado, set_novo_lexema, set_novo_caractere
    ):
        """
        Realiza o processo necessário para tratar cadeias
        :param motor_lexico: objeto que auxilia a análise lexica
        :param lexema: lexema atual
        :param caractere: caractere atual
        :param set_novo_estado: função para setar um novo estado
        :param set_novo_lexema: função para setar um novo lexema
        :param set_novo_caractere: função para setar um novo caractere
        :return: Tokens
        """
        lexema = lexema + caractere
        set_novo_lexema(lexema)

        caractere = motor_lexico.get_caractere()
        set_novo_caractere(caractere)

        lexema = lexema + caractere
        set_novo_lexema(lexema)

        while (caractere is not None) and (caractere != Constants.ASPAS_DUPLAS):
            caractere = motor_lexico.get_caractere()
            set_novo_caractere(caractere)

            lexema = lexema + caractere
            set_novo_lexema(lexema)
        return Token(motor_lexico.linha, TipoToken.CADEIA, lexema)

