from domain.tipo_token import TipoToken
from domain.token import Token


class Estado3Handler:
    """
    Handler do estado 3, ou seja, o que é responsável pelo tratamento de números
    """

    def __init__(self):
        pass

    def get_estado_tratado(self):
        """
        Retorna o qual estado esse handler lida
        :return: número
        """
        return 3

    def handle(
            self, motor_lexico, lexema, caractere,
            set_novo_estado, set_novo_lexema, set_novo_caractere
    ):
        """
        Realiza o processo necessário para tratar números
        :param motor_lexico: objeto que auxilia a análise lexica
        :param lexema: lexema atual
        :param caractere: caractere atual
        :param set_novo_estado: função para setar um novo estado
        :param set_novo_lexema: função para setar um novo lexema
        :param set_novo_caractere: função para setar um novo caractere
        :return: Tokens.
        """
        lexema = lexema + caractere
        set_novo_lexema(lexema)

        caractere = motor_lexico.get_caractere()
        set_novo_caractere(caractere)

        if caractere is None or (not caractere.isdigit()):
            motor_lexico.unget_caractere(caractere)
            return Token(motor_lexico.linha, TipoToken.CTE, lexema)
