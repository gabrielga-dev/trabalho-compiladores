from domain.sintatico import Sintatico

if __name__ == "__main__":
    # nome = input("Entre com o nome do arquivo: ")
        nome = 'exemplos/exemplo_1.txt'
        parser = Sintatico()
        parser.interpretar(nome)
