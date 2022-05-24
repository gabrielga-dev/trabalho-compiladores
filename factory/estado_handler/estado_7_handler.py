# Nome Discente: Gabriel Guimarães de Almeida
# Matrícula: 0021722
# Data: 23/05/2022
#
# Declaro que sou o único autor e responsável por este programa. Todas as partes do programa, exceto as que foram fornecidas
# pelo professor ou copiadas do livro ou das bibliotecas de Aho et al., foram desenvolvidas por mim. Declaro também que
# sou responsável por todas as eventuais cópias deste programa e que não distribui nem facilitei a distribuição de cópias.
#
# O arquivo estado_7_handler.py comporta o "handle" do estado 7 da analise lexica
#
# Referências bibliográficas:
# Exemplos enviados pelo professor Mário
# Repositório de uma aula de SOLID feita pelo próprio Discente: https://github.com/gabrielga-dev/aula-de-SOLID
# AHO, A. V. et al. Compiladores. 2 ed. São Paulo: Pearson Addison-Wesley, 2008.


from domain.tipo_token import TipoToken
from domain.token import Token
from project_utils.constants import Constants
from project_utils.mensagens_de_erro_constants import MensagensDeErroConstants


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

            if caractere == Constants.ASTERISCO and motor_lexico.prox_char() == Constants.BARRA:
                break
        if motor_lexico.get_caractere() is None:
            return Token(
                motor_lexico.linha,
                TipoToken.ERROR,
                None,
                MensagensDeErroConstants.ERROR_MESSAGE_COMENTARIO_DE_BLOCO_NAO_FECHADO
            )
        set_novo_estado(1)

