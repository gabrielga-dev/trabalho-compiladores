# Nome Discente: Gabriel Guimarães de Almeida
# Matrícula: 0021722
# Data: 23/05/2022
#
# Declaro que sou o único autor e responsável por este programa. Todas as partes do programa, exceto as que foram fornecidas
# pelo professor ou copiadas do livro ou das bibliotecas de Aho et al., foram desenvolvidas por mim. Declaro também que
# sou responsável por todas as eventuais cópias deste programa e que não distribui nem facilitei a distribuição de cópias.
#
# O arquivo estado_4_lexema_handler_factory.py comporta a chamada do "handle" correto para o lexema atual
# do analisador lexico
#
# Referências bibliográficas:
# Exemplos enviados pelo professor Mário
# Repositório de uma aula de SOLID feita pelo próprio Discente: https://github.com/gabrielga-dev/aula-de-SOLID
# AHO, A. V. et al. Compiladores. 2 ed. São Paulo: Pearson Addison-Wesley, 2008.


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
    """
    Esta classe recebe o lexema atual e retorna o handler que lida com o tal
    """

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

    def get_lexema_handle(self, lexema):
        """
        Esta função recebe o lexema e retorna o handler que lidará com ele
        :param lexema: lexema atual
        :return: handler do lexema passado
        """
        return [handler for handler in self.handlers if handler.lexema_matches(lexema)][0]
