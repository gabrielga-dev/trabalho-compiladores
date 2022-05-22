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
