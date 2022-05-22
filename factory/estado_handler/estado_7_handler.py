from domain.tipo_token import TipoToken
from domain.token import Token
from project_utils.constants import Constants


class Estado7Handler:
    """
    Handler do estado 7, ou seja, o que é responsável por consumir comentários de bloco
    """

    def __init__(self):
        pass

    def get_estado_tratado(self):
        """
        Retorna o qual estado esse handler lida
        :return: número
        """
        return 7

    def handle(
            self, motor_lexico, lexema, caractere,
            set_novo_estado, set_novo_lexema, set_novo_caractere
    ):
        """
        Realiza o processo necessário para consumir comentários de bloco
        :param motor_lexico: objeto que auxilia a análise lexica
        :param lexema: lexema atual
        :param caractere: caractere atual
        :param set_novo_estado: função para setar um novo estado
        :param set_novo_lexema: função para setar um novo lexema
        :param set_novo_caractere: função para setar um novo caractere
        :return: Token, caso o bloco esteja escrito de maneira errada, None.
        """
        while caractere is not None:
            caractere = motor_lexico.get_caractere()
            set_novo_caractere(caractere)

            if caractere == Constants.ASTERISCO and motor_lexico.get_caractere() == Constants.BARRA:
                break
        if motor_lexico.get_caractere() is None:
            return Token(motor_lexico.linha, TipoToken.ERROR, 'Bloco de comentário aberto e não fechado')
        set_novo_estado(1)

