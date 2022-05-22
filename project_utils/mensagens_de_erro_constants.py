class MensagensDeErroConstants:
    """
    Classe que comporta mensagens de erro
    """
    ERRO = 'ERRO'
    ERROR_MESSAGE_ARQUIVO_NAO_ABERTO = ERRO + ': O arquivo não está aberto.'
    ERROR_MESSAGE_ARQUIVO_JA_ABERTO = ERRO + ': Um programa está sendo compilado no momento.'
    ERROR_MESSAGE_ARQUIVO_INEXISTENTE = ERRO + ': O arquivo especificado é inexistente.'
    ERROR_MESSAGE_IDENTIFICADOR_MAX_DIGITOS = ERRO + ': Identificador com mais de 16 digitos.'


def ERRO_AO_TENTAR_CONSUMIR(nao_terminal):
    """
    Esta função gera uma mensagem de erro para quando ocorrer erros na tentativa de consumir um não-terminal
    :param nao_terminal: string do não terminal
    :return: string da mensagem, pode variar de acordo com o valor passado no parâmetro
    """
    if nao_terminal is None:
        return 'Nenhum não-terminal encaixa com o valor passado'
    return 'Erro ao tentar consumir o não-terminal ' + nao_terminal
