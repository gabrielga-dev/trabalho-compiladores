# Nome Discente: Gabriel Guimarães de Almeida
# Matrícula: 0021722
# Data: 23/05/2022
#
# Declaro que sou o único autor e responsável por este programa. Todas as partes do programa, exceto as que foram fornecidas
# pelo professor ou copiadas do livro ou das bibliotecas de Aho et al., foram desenvolvidas por mim. Declaro também que
# sou responsável por todas as eventuais cópias deste programa e que não distribui nem facilitei a distribuição de cópias.
#
# O arquivo estado_3_handler.py comporta a chamada do "handle" correto do estado atual da analise lexica
#
# Referências bibliográficas:
# Exemplos enviados pelo professor Mário
# Repositório de uma aula de SOLID feita pelo próprio Discente: https://github.com/gabrielga-dev/aula-de-SOLID
# AHO, A. V. et al. Compiladores. 2 ed. São Paulo: Pearson Addison-Wesley, 2008.


from factory.estado_handler.estado_1_handler import Estado1Handler
from factory.estado_handler.estado_2_handler import Estado2Handler
from factory.estado_handler.estado_3_handler import Estado3Handler
from factory.estado_handler.estado_4_handler import Estado4Handler
from factory.estado_handler.estado_5_handler import Estado5Handler
from factory.estado_handler.estado_6_handler import Estado6Handler
from factory.estado_handler.estado_7_handler import Estado7Handler


class EstadoHandlerFactory:
    """
    Esta classe comporta todos os handlers dos estados possíveis da análise léxica
    """
    def __init__(self):
        self.handlers = [
            Estado1Handler(),
            Estado2Handler(),
            Estado3Handler(),
            Estado4Handler(),
            Estado5Handler(),
            Estado6Handler(),
            Estado7Handler()
        ]

    def get_estado_handler(self, estado):
        """
        Essa função recebe um estado e procura qual é o handler dele e o retorna
        :param estado: estado pelo qual deve ser procurado o handler
        :return: handler do estado
        """
        handlers_filtrados = [handler for handler in self.handlers if handler.get_estado_tratado() == estado]
        return handlers_filtrados[0]
