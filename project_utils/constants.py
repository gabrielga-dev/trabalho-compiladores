# Nome Discente: Gabriel Guimarães de Almeida
# Matrícula: 0021722
# Data: 23/05/2022
#
# Declaro que sou o único autor e responsável por este programa. Todas as partes do programa, exceto as que foram fornecidas
# pelo professor ou copiadas do livro ou das bibliotecas de Aho et al., foram desenvolvidas por mim. Declaro também que
# sou responsável por todas as eventuais cópias deste programa e que não distribui nem facilitei a distribuição de cópias.
#
# O arquivo constants.py comporta as constantes da linguagem, referente à caracteres
#
# Referências bibliográficas:
# Exemplos enviados pelo professor Mário
# Repositório de uma aula de SOLID feita pelo próprio Discente: https://github.com/gabrielga-dev/aula-de-SOLID
# AHO, A. V. et al. Compiladores. 2 ed. São Paulo: Pearson Addison-Wesley, 2008.


class Constants:
    """
    Classe que comporta constantes da linguagem
    """
    TAMANHO_MAXIMO_IDENTIFICADOR = 16
    CARACTERES_IGNORAVEIS = [' ', '\t', '\n']
    BARRA = '/'
    ASTERISCO = '*'
    DOIS_PONTOS = ':'
    IGUAL = '='
    MENOR_QUE = '<'
    MAIOR_QUE = '>'
    PONTO_E_VIRGULA = ';'
    VIRGULA = ','
    ABRE_PARENTESE = '('
    FECHA_PARENTESE = ')'
    ABRE_CHAVE = '{'
    FECHA_CHAVE = '}'
    SOMA = '+'
    SUBTRACAO = '-'
    EXCLAMACAO = '-'
    ASPAS_DUPLAS = '"'
    PRIMITIVOS_COMUNS = [
        PONTO_E_VIRGULA,
        DOIS_PONTOS,
        VIRGULA,
        ABRE_PARENTESE,
        FECHA_PARENTESE,
        ABRE_CHAVE,
        FECHA_CHAVE,
        IGUAL,
        MENOR_QUE,
        MAIOR_QUE,
        SOMA,
        SUBTRACAO,
        ASTERISCO,
        BARRA,
        EXCLAMACAO
    ]
