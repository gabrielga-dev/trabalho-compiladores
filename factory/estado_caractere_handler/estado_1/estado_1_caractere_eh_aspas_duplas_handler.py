# Nome Discente: Gabriel Guimarães de Almeida
# Matrícula: 0021722
# Data: 23/05/2022
#
# Declaro que sou o único autor e responsável por este programa. Todas as partes do programa, exceto as que foram fornecidas
# pelo professor ou copiadas do livro ou das bibliotecas de Aho et al., foram desenvolvidas por mim. Declaro também que
# sou responsável por todas as eventuais cópias deste programa e que não distribui nem facilitei a distribuição de cópias.
#
# O arquivo estado_1_caractere_eh_aspas_duplas_handler.py comporta o "handle" de quando o analisadoir lexico está no
# estado 1 e o caractere é aspas duplas
#
# Referências bibliográficas:
# Exemplos enviados pelo professor Mário
# Repositório de uma aula de SOLID feita pelo próprio Discente: https://github.com/gabrielga-dev/aula-de-SOLID
# AHO, A. V. et al. Compiladores. 2 ed. São Paulo: Pearson Addison-Wesley, 2008.

from project_utils.constants import Constants


class Estado1CaractereEhAspasDuplasHandler:
    """
    Handler do caractere do estado 1 da análise léxica, o qual verifica se o caractere é áspas duplas
    """

    def caractere_matches(self, motor_lexico, caractere):
        """
        Esta função verifica se o caractere é lidado pelo handler
        :param motor_lexico: objeto que auxilia a análise léxica
        :param caractere: caractere atual
        :return: booleando
        """
        return caractere == Constants.ASPAS_DUPLAS

    def handle(self, caractere, motor_lexico, set_novo_estado):
        """
        Realiza tratamento do caractere
        :param caractere: caractere atual
        :param motor_lexico: objeto que auxilia a análise léxica
        :param set_novo_estado: função que seta o novo estado
        :return: None
        """
        set_novo_estado(5)
        return None
