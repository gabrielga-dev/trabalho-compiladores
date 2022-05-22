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
