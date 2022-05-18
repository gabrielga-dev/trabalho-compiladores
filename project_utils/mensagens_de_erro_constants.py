class MensagensDeErroConstants:
    ERRO = 'ERRO'
    ARQUIVO_JA_ABERTO = ERRO + ': Um programa está sendo compilado no momento.'


def ERRO_AO_TENTAR_CONSUMIR(nao_terminal):
    if nao_terminal is None:
        return 'Nenhum não-terminal encaixa com o valor passado'
    return 'Erro ao tentar consumir o não-terminal ' + nao_terminal
