from factory.estado_caractere_handler.estado_1.estado_1_caractere_eh_alfanumerico_handler import \
    Estado1CaractereEhAlfanumericoHandler
from factory.estado_caractere_handler.estado_1.estado_1_caractere_eh_aspas_duplas_handler import \
    Estado1CaractereEhAspasDuplasHandler
from factory.estado_caractere_handler.estado_1.estado_1_caractere_eh_barra_seguido_de_asterisco_handler import \
    Estado1CaractereEhBarraSeguidoDeEsteriscoHandler
from factory.estado_caractere_handler.estado_1.estado_1_caractere_eh_barra_seguido_de_barra_handler import \
    Estado1CaractereEhBarraSeguidoDeBarraHandler
from factory.estado_caractere_handler.estado_1.estado_1_caractere_eh_digito_handler import \
    Estado1CaractereEhDigitoHandler
from factory.estado_caractere_handler.estado_1.estado_1_caractere_eh_dois_pontos_seguido_de_igualdade_handler import \
    Estado1CaractereEhDoisPontosSeguidoDeIgualdadeHandler
from factory.estado_caractere_handler.estado_1.estado_1_caractere_eh_ignoravel_handler import \
    Estado1CaractereEhIgnoravelHandler
from factory.estado_caractere_handler.estado_1.estado_1_caractere_eh_invalido_handler import \
    Estado1CaractereEhInvalidoHandler
from factory.estado_caractere_handler.estado_1.estado_1_caractere_eh_maior_que_seguido_de_igualdade_handler import \
    Estado1CaractereEhMaiorQueSeguidoDeIgualdadeHandler
from factory.estado_caractere_handler.estado_1.estado_1_caractere_eh_menor_que_seguido_maior_que_handler import \
    Estado1CaractereEhMenorQueSeguidoDeMaiorQueHandler
from factory.estado_caractere_handler.estado_1.estado_1_caractere_eh_none_handler import Estado1CaractereEhNoneHandler
from factory.estado_caractere_handler.estado_1.estado_1_caractere_eh_menor_que_seguido_de_igualdade_handler import \
    Estado1CaractereEhMenorQueSeguidoDeIgualdadeHandler
from factory.estado_caractere_handler.estado_1.estado_1_caractere_eh_primitivo_comum_handler import \
    Estado1CaractereEhPrimitivoComumHandler


class Estado1CaractereHandlerFactory:
    """
    Essa classe realiza o tratamento em cima dos caraceters encontrados no estado 1 da análise léxica
    """

    def __init__(self):
        self.handlers = [
            Estado1CaractereEhNoneHandler(),
            Estado1CaractereEhIgnoravelHandler(),
            Estado1CaractereEhBarraSeguidoDeBarraHandler(),
            Estado1CaractereEhBarraSeguidoDeEsteriscoHandler(),
            Estado1CaractereEhAlfanumericoHandler(),
            Estado1CaractereEhDigitoHandler(),
            Estado1CaractereEhDoisPontosSeguidoDeIgualdadeHandler(),
            Estado1CaractereEhMenorQueSeguidoDeIgualdadeHandler(),
            Estado1CaractereEhMaiorQueSeguidoDeIgualdadeHandler(),
            Estado1CaractereEhMenorQueSeguidoDeMaiorQueHandler(),
            Estado1CaractereEhPrimitivoComumHandler(),
            Estado1CaractereEhAspasDuplasHandler(),
        ]
        self.handler_de_caractere_invalido = Estado1CaractereEhInvalidoHandler()

    def get_caractere_handler(self, caractere, motor_lexico):
        """
        Esta função recebe um caractere e retorna o handler dele
        :param caractere: char que será usado para filtrar os handlers
        :param motor_lexico: objeto que auxilia a análise léxica
        :return: handler para o caractere
        """
        handlers_filtrados = [
            handler
            for handler in self.handlers
            if handler.caractere_matches(motor_lexico, caractere)
        ]
        handler = None
        if len(handlers_filtrados) > 0:
            handler = [handler for handler in self.handlers if handler.caractere_matches(motor_lexico, caractere)][0]
        if handler is None:
            return self.handler_de_caractere_invalido
        return handler
