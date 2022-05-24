# Nome Discente: Gabriel Guimarães de Almeida
# Matrícula: 0021722
# Data: 23/05/2022
#
# Declaro que sou o único autor e responsável por este programa. Todas as partes do programa, exceto as que foram fornecidas
# pelo professor ou copiadas do livro ou das bibliotecas de Aho et al., foram desenvolvidas por mim. Declaro também que
# sou responsável por todas as eventuais cópias deste programa e que não distribui nem facilitei a distribuição de cópias.
#
# O arquivo tipo_token.py comporta as constantes (tuplas) de todos os tipos de tokens presentes e necessários na linguagem
# e sua análise
#
# Referências bibliográficas:
# Exemplos enviados pelo professor Mário
# Repositório de uma aula de SOLID feita pelo próprio Discente: https://github.com/gabrielga-dev/aula-de-SOLID
# AHO, A. V. et al. Compiladores. 2 ed. São Paulo: Pearson Addison-Wesley, 2008.

class TipoToken:
    """
    Esta classe guarda quais são os tipos de tokens possíveis
    """
    ID = (1, 'id')
    CTE = (2, 'cte')  # numero
    CADEIA = (3, 'cadeia')
    PROGRAMA = (4, 'programa')
    VARIAVEIS = (5, 'variaveis')
    INTEIRO = (6, 'inteiro')
    REAL = (7, 'real')
    LOGICO = (8, 'logico')
    CARACTER = (9, 'caracter')
    SE = (10, 'se')
    SENAO = (11, 'senao')
    ENQUANTO = (12, 'enquanto')
    LEIA = (13, 'leia')
    ESCREVA = (14, 'escreva')
    FALSO = (15, 'falso')
    VERDADEIRO = (16, 'verdadeiro')
    ATRIB = (17, ':=')
    OPREL = (18, 'operadores-relacionais')
    OPAD = (19, 'operadores-adicao')
    OPMUL = (20, 'operadores-multiplicacao')
    OPNEG = (21, '!')
    PVIRG = (22, ';')
    DPONTOS = (24, ':')
    VIRG = (25, ',')
    ABREPAR = (26, '(')
    FECHAPAR = (27, ')')
    ABRECH = (28, '{')
    FECHACH = (29, '}')
    ERROR = (31, 'erro')
    FIMARQ = (32, 'fim-de-arquivo')
