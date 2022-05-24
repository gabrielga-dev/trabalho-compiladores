# Nome Discente: Gabriel Guimarães de Almeida
# Matrícula: 0021722
# Data: 23/05/2022
#
# Declaro que sou o único autor e responsável por este programa. Todas as partes do programa, exceto as que foram fornecidas
# pelo professor ou copiadas do livro ou das bibliotecas de Aho et al., foram desenvolvidas por mim. Declaro também que
# sou responsável por todas as eventuais cópias deste programa e que não distribui nem facilitei a distribuição de cópias.
#
# O arquivo estado_1_caractere_eh_menor_que_seguido_maior_que_handler.py comporta o "handle" de quando o analisadoir lexico está no
# estado 1 e o caractere é "<>"
#
# Referências bibliográficas:
# Exemplos enviados pelo professor Mário
# Repositório de uma aula de SOLID feita pelo próprio Discente: https://github.com/gabrielga-dev/aula-de-SOLID
# AHO, A. V. et al. Compiladores. 2 ed. São Paulo: Pearson Addison-Wesley, 2008.


from domain.tipo_token import TipoToken
from domain.token import Token
from project_utils.constants import Constants


class Estado1CaractereEhMenorQueSeguidoDeMaiorQueHandler:
    """
    Handler do caractere do estado 1 da análise léxica, o qual verifica se o caractere é "<="
    """

    def caractere_matches(self, motor_lexico, caractere):
        """
        Esta função verifica se o caractere é lidado pelo handler
        :param motor_lexico: objeto que auxilia a análise léxica
        :param caractere: caractere atual
        :return: booleando
        """
        return caractere == Constants.MENOR_QUE and motor_lexico.prox_char() == Constants.MAIOR_QUE

    def handle(self, caractere, motor_lexico, set_novo_estado):
        """
        Realiza tratamento do caractere
        :param caractere: caractere atual
        :param motor_lexico: objeto que auxilia a análise léxica
        :param set_novo_estado: função que seta o novo estado
        :return: Token
        """
        return Token(motor_lexico.linha, TipoToken.OPREL, caractere + motor_lexico.get_caractere())
