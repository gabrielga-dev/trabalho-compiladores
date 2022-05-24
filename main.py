# Nome Discente: Gabriel Guimarães de Almeida
# Matrícula: 0021722
# Data: 23/05/2022
#
# Declaro que sou o único autor e responsável por este programa. Todas as partes do programa, exceto as que foram fornecidas
# pelo professor ou copiadas do livro ou das bibliotecas de Aho et al., foram desenvolvidas por mim. Declaro também que
# sou responsável por todas as eventuais cópias deste programa e que não distribui nem facilitei a distribuição de cópias.
#
# O arquivo main.py comporta o "start" de toda a aplicação
#
# Referências bibliográficas:
# Exemplos enviados pelo professor Mário
# Repositório de uma aula de SOLID feita pelo próprio Discente: https://github.com/gabrielga-dev/aula-de-SOLID
# AHO, A. V. et al. Compiladores. 2 ed. São Paulo: Pearson Addison-Wesley, 2008.


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
