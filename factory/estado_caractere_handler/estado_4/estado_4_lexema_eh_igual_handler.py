# Nome Discente: Gabriel Guimarães de Almeida
# Matrícula: 0021722
# Data: 23/05/2022
#
# Declaro que sou o único autor e responsável por este programa. Todas as partes do programa, exceto as que foram fornecidas
# pelo professor ou copiadas do livro ou das bibliotecas de Aho et al., foram desenvolvidas por mim. Declaro também que
# sou responsável por todas as eventuais cópias deste programa e que não distribui nem facilitei a distribuição de cópias.
#
# O arquivo estado_4_lexema_eh_igual_handler.py comporta o "handle" de quando o analisador lexico está no
# estado 4 e o lexema é igual ("==")
#
# Referências bibliográficas:
# Exemplos enviados pelo professor Mário
# Repositório de uma aula de SOLID feita pelo próprio Discente: https://github.com/gabrielga-dev/aula-de-SOLID
# AHO, A. V. et al. Compiladores. 2 ed. São Paulo: Pearson Addison-Wesley, 2008.


from domain.tipo_token import TipoToken
from domain.token import Token
from project_utils.constants import Constants


class Estado4LexemaEhIgualdadeHandler:
    """
    Handler de lexema do estado 4. Este verifica se o lexema é "="
    """

    def lexema_matches(self, lexema):
        """
        Esta função realiza a verificação se o lexema é lidado por este handler
        :param lexema: lexema atual
        :return: booleano
        """
        return lexema == Constants.IGUAL

    def handle(self, lexema, motor_lexico):
        """
        Esta função realiza o tratamento do lexema
        :param lexema: lexema atual
        :param motor_lexico: objeto que auxilia a análise lexica
        :return: Token
        """
        return Token(motor_lexico.linha, TipoToken.OPREL, lexema)
