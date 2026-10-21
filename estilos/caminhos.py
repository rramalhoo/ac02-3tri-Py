import os

PASTA_PROJETO = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
PASTA_DADOS = os.path.join(PASTA_PROJETO, "dados")

ARQUIVO_TXT = os.path.join(PASTA_DADOS, "equipamentos.txt")
ARQUIVO_CSV = os.path.join(PASTA_DADOS, "equipamentos.csv")
ARQUIVO_JSON = os.path.join(PASTA_DADOS, "equipamentos.json")
