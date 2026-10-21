import csv
from estilos.caminhos import ARQUIVO_CSV

def listar():
    print("\n=== EQUIPAMENTOS ===\n")

    total = 0
    soma = 0
    maiorValor = 0
    maisValioso = ""

    with open(ARQUIVO_CSV, "r", encoding="utf-8") as arquivo:
        leitor = csv.reader(arquivo)

        for linha in leitor:
            nome = linha[0]
            ano = linha[1]
            valor = float(linha[2])
            print("Equipamento:", nome, "- Ano:", ano, "- Valor: R$", valor)

            total += 1
            soma += valor

            if total == 1 or valor > maiorValor:
                maiorValor = valor
                maisValioso = nome

    print("\n=== RELATÓRIO ===\n")

    if total == 0:
        print("Nenhum equipamento cadastrado\n")
        return

    media = soma / total

    print("Total de equipamentos:", total)
    print(f"Média de valor: R$ {media:.2f}")
    print("Item mais valioso:", maisValioso)
    print(f"Maior valor registrado: R$ {maiorValor:.2f}\n")
