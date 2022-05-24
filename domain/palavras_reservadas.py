# Nome Discente: Gabriel Guimarães de Almeida
# Matrícula: 0021722
# Data: 23/05/2022
#
# Declaro que sou o único autor e responsável por este programa. Todas as partes do programa, exceto as que foram fornecidas
# pelo professor ou copiadas do livro ou das bibliotecas de Aho et al., foram desenvolvidas por mim. Declaro também que
# sou responsável por todas as eventuais cópias deste programa e que não distribui nem facilitei a distribuição de cópias.
#
# O arquivo palavras_reservadas.py comporta as constantes das palavras reservadas da linguagem
#
# Referências bibliográficas:
# Exemplos enviados pelo professor Mário
# Repositório de uma aula de SOLID feita pelo próprio Discente: https://github.com/gabrielga-dev/aula-de-SOLID
# AHO, A. V. et al. Compiladores. 2 ed. São Paulo: Pearson Addison-Wesley, 2008.

from domain.tipo_token import TipoToken
"""
Este arquivo guarda as palavras reservadas da linguagem
"""
PALAVRAS_RESERVADAS = {
        'programa': TipoToken.PROGRAMA,
        'variaveis': TipoToken.VARIAVEIS,
        'inteiro': TipoToken.INTEIRO,
        'real': TipoToken.REAL,
        'logico': TipoToken.LOGICO,
        'caracter': TipoToken.CARACTER,
        'se': TipoToken.SE,
        'senao': TipoToken.SENAO,
        'enquanto': TipoToken.ENQUANTO,
        'leia': TipoToken.LEIA,
        'escreva': TipoToken.ESCREVA,
        'falso': TipoToken.FALSO,
        'verdadeiro': TipoToken.VERDADEIRO
}
