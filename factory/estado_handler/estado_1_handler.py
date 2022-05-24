# Nome Discente: Gabriel Guimarães de Almeida
# Matrícula: 0021722
# Data: 23/05/2022
#
# Declaro que sou o único autor e responsável por este programa. Todas as partes do programa, exceto as que foram fornecidas
# pelo professor ou copiadas do livro ou das bibliotecas de Aho et al., foram desenvolvidas por mim. Declaro também que
# sou responsável por todas as eventuais cópias deste programa e que não distribui nem facilitei a distribuição de cópias.
#
# O arquivo estado_1_handler.py comporta o "handle" do estado 1 da analise lexica
#
# Referências bibliográficas:
# Exemplos enviados pelo professor Mário
# Repositório de uma aula de SOLID feita pelo próprio Discente: https://github.com/gabrielga-dev/aula-de-SOLID
# AHO, A. V. et al. Compiladores. 2 ed. São Paulo: Pearson Addison-Wesley, 2008.


from factory.estado_caractere_handler.estado_1.estado_1_caractere_handler_factory import Estado1CaractereHandlerFactory


class Estado1Handler:
    """
    Handler do estado 1, ou seja, o que é responsável pela primeira classificação
    """

    def __init__(self):
        self.handler_caractere_factory = Estado1CaractereHandlerFactory()

    def get_estado_tratado(self):
        """
        Retorna o qual estado esse handler lida
        :return: número
        """
        return 1

    def handle(
            self, motor_lexico, lexema, caractere,
            set_novo_estado, set_novo_lexema, set_novo_caractere
    ):
        """
        Realiza o processo necessário para tratar o caractere
        :param motor_lexico: objeto que auxilia a análise lexica
        :param lexema: lexema atual
        :param caractere: caractere atual
        :param set_novo_estado: função para setar um novo estado
        :param set_novo_lexema: função para setar um novo lexema
        :param set_novo_caractere: função para setar um novo caractere
        :return: Tokens, caso o handler do caractere não retorne nada, None.
        """
        caractere = motor_lexico.get_caractere()
        set_novo_caractere(caractere)

        resultado = self.handler_caractere_factory.get_caractere_handler(
            caractere, motor_lexico
        ).handle(
            caractere, motor_lexico, set_novo_estado
        )

        if resultado is not None:
            return resultado
