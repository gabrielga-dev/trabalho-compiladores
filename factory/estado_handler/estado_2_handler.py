# Nome Discente: Gabriel Guimarães de Almeida
# Matrícula: 0021722
# Data: 23/05/2022
#
# Declaro que sou o único autor e responsável por este programa. Todas as partes do programa, exceto as que foram fornecidas
# pelo professor ou copiadas do livro ou das bibliotecas de Aho et al., foram desenvolvidas por mim. Declaro também que
# sou responsável por todas as eventuais cópias deste programa e que não distribui nem facilitei a distribuição de cópias.
#
# O arquivo estado_2_handler.py comporta o "handle" do estado 2 da analise lexica
#
# Referências bibliográficas:
# Exemplos enviados pelo professor Mário
# Repositório de uma aula de SOLID feita pelo próprio Discente: https://github.com/gabrielga-dev/aula-de-SOLID
# AHO, A. V. et al. Compiladores. 2 ed. São Paulo: Pearson Addison-Wesley, 2008.


from domain.palavras_reservadas import PALAVRAS_RESERVADAS as PalavrasReservadas
from domain.tipo_token import TipoToken
from domain.token import Token
from project_utils.constants import Constants
from project_utils.mensagens_de_erro_constants import MensagensDeErroConstants


class Estado2Handler:
    """
    Handler do estado 2, ou seja, o que é responsável pelo tratamento de identificadores e palavras reservada
    """

    def __init__(self):
        pass

    def get_estado_tratado(self):
        """
        Retorna o qual estado esse handler lida
        :return: número
        """
        return 2

    def handle(
            self, motor_lexico, lexema, caractere,
            set_novo_estado, set_novo_lexema, set_novo_caractere
    ):
        """
        Realiza o tratamento de identificadores e palavras reservada
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

        if caractere is None or (not caractere.isalnum()):
            motor_lexico.unget_caractere(caractere)
            if lexema in PalavrasReservadas:
                return Token(motor_lexico.linha, PalavrasReservadas[lexema], lexema)
            elif len(lexema) > Constants.TAMANHO_MAXIMO_IDENTIFICADOR:
                return Token(motor_lexico.linha, TipoToken.ERROR, lexema, '[ ' +
                             MensagensDeErroConstants.ERROR_MESSAGE_IDENTIFICADOR_MAX_DIGITOS + ' ]')
            else:
                return Token(motor_lexico.linha, TipoToken.ID, lexema)
