from factory.estado_caractere_handler.estado_4.estado_4_lexema_eh_abre_chave_handler import \
    Estado4LexemaEhAbreChaveHandler
from factory.estado_caractere_handler.estado_4.estado_4_lexema_eh_abre_parentese_handler import \
    Estado4LexemaEhAbreParenteseHandler
from factory.estado_caractere_handler.estado_4.estado_4_lexema_eh_asterisco_handler import \
    Estado4LexemaEhAteriscoHandler
from factory.estado_caractere_handler.estado_4.estado_4_lexema_eh_barra_handler import Estado4LexemaEhBarraHandler
from factory.estado_caractere_handler.estado_4.estado_4_lexema_eh_dois_pontos_handler import \
    Estado4LexemaEhDoisPontosHandler
from factory.estado_caractere_handler.estado_4.estado_4_lexema_eh_exclamacao_handler import \
    Estado4LexemaEhExclamacaoHandler
from factory.estado_caractere_handler.estado_4.estado_4_lexema_eh_fecha_chave_handler import \
    Estado4LexemaEhFechaChaveHandler
from factory.estado_caractere_handler.estado_4.estado_4_lexema_eh_fecha_parentese_handler import \
    Estado4LexemaEhFechaParenteseHandler
from factory.estado_caractere_handler.estado_4.estado_4_lexema_eh_igual_handler import Estado4LexemaEhIgualdadeHandler
from factory.estado_caractere_handler.estado_4.estado_4_lexema_eh_maior_que_handler import \
    Estado4LexemaEhMaiorQueHandler
from factory.estado_caractere_handler.estado_4.estado_4_lexema_eh_menor_que_handler import \
    Estado4LexemaEhMenorQueHandler
from factory.estado_caractere_handler.estado_4.estado_4_lexema_eh_ponto_e_virgula_handler import \
    Estado4LexemaEhPontoVirgulaHandler
from factory.estado_caractere_handler.estado_4.estado_4_lexema_eh_soma_handler import Estado4LexemaEhSomaHandler
from factory.estado_caractere_handler.estado_4.estado_4_lexema_eh_subtracao_handler import \
    Estado4LexemaEhSubtracaoHandler
from factory.estado_caractere_handler.estado_4.estado_4_lexema_eh_virgula_handler import Estado4LexemaEhVirgulaHandler


class Estado4LexemaHandlerFactory:

    def __init__(self):
        self.handlers = [
            Estado4LexemaEhAbreChaveHandler(),
            Estado4LexemaEhAbreParenteseHandler(),
            Estado4LexemaEhAteriscoHandler(),
            Estado4LexemaEhBarraHandler(),
            Estado4LexemaEhDoisPontosHandler(),
            Estado4LexemaEhExclamacaoHandler(),
            Estado4LexemaEhFechaChaveHandler(),
            Estado4LexemaEhFechaParenteseHandler(),
            Estado4LexemaEhIgualdadeHandler(),
            Estado4LexemaEhMaiorQueHandler(),
            Estado4LexemaEhMenorQueHandler(),
            Estado4LexemaEhPontoVirgulaHandler(),
            Estado4LexemaEhSomaHandler(),
            Estado4LexemaEhSubtracaoHandler(),
            Estado4LexemaEhVirgulaHandler(),
        ]

    def handle_lexema(self, lexema, motor_lexico):
        handler = [handler for handler in self.handlers if handler.lexema_matches(lexema)][0]
        return handler.handle(lexema, motor_lexico)
