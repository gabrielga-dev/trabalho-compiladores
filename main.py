from domain.sintatico import Sintatico
from project_utils.mensagens_constants import MensagensConstants

if __name__ == "__main__":
    """
    Início de todo o funcionamento do trabalho
    """
    nome = 'exemplos/exemplo_1.txt'
    parser = Sintatico()
    valido, erros = parser.interpretar(nome)

    if valido:
        print(MensagensConstants.PROGRAMA_ACEITO)
    else:
        for erro in erros:
            print(erro)
