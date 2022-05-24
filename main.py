from domain.sintatico import Sintatico
from project_utils.mensagens_constants import MensagensConstants
import sys


if __name__ == "__main__":
    """
    Início de todo o funcionamento do trabalho
    """
    path = sys.argv[1]
    sintatico = Sintatico()
    valido, erros = sintatico.interpretar(path)

    if valido:
        print(MensagensConstants.PROGRAMA_ACEITO)
    else:
        for erro in erros:
            print(erro)
