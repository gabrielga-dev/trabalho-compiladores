# Nome Discente: Gabriel Guimarães de Almeida
# Matrícula: 0021722
# Data: 23/05/2022
#
# Declaro que sou o único autor e responsável por este programa. Todas as partes do programa, exceto as que foram fornecidas
# pelo professor ou copiadas do livro ou das bibliotecas de Aho et al., foram desenvolvidas por mim. Declaro também que
# sou responsável por todas as eventuais cópias deste programa e que não distribui nem facilitei a distribuição de cópias.
#
# O arquivo mensagens_de_erro_constants.py comporta as constantes de mensagens de erro para o usuário
#
# Referências bibliográficas:
# Exemplos enviados pelo professor Mário
# Repositório de uma aula de SOLID feita pelo próprio Discente: https://github.com/gabrielga-dev/aula-de-SOLID
# AHO, A. V. et al. Compiladores. 2 ed. São Paulo: Pearson Addison-Wesley, 2008.



class MensagensDeErroConstants:
    """
    Classe que comporta mensagens de erro
    """
    ERRO = 'ERRO'
    ERROR_MESSAGE_ARQUIVO_NAO_ABERTO = ERRO + ': O arquivo não está aberto.'
    ERROR_MESSAGE_ARQUIVO_JA_ABERTO = ERRO + ': Um programa está sendo compilado no momento.'
    ERROR_MESSAGE_ARQUIVO_INEXISTENTE = ERRO + ': O arquivo especificado é inexistente.'
    ERROR_MESSAGE_IDENTIFICADOR_MAX_DIGITOS = ERRO + ': Identificador com mais de 16 digitos.'
    ERROR_MESSAGE_CADEIA_NAO_FECHADA = ERRO + ': A cadeia foi aberta mas não foi fechada.'
    ERROR_MESSAGE_COMENTARIO_DE_BLOCO_NAO_FECHADO = ERRO + ': O comentário de bloco foi aberto mas não foi fechado.'


def ERRO_AO_TENTAR_CONSUMIR(nao_terminal):
    """
    Esta função gera uma mensagem de erro para quando ocorrer erros na tentativa de consumir um não-terminal
    :param nao_terminal: string do não terminal
    :return: string da mensagem, pode variar de acordo com o valor passado no parâmetro
    """
    if nao_terminal is None:
        return 'Nenhum não-terminal encaixa com o valor passado'
    return 'Erro ao tentar consumir o não-terminal ' + nao_terminal
