from estilos.caminhos import ARQUIVO_TXT

def historicoEquipamentos():
    equipamentos = []

    arquivo = open(ARQUIVO_TXT, "r")
    linhas = arquivo.readlines()
    arquivo.close()

    for linha in linhas:
        partes = linha.strip().split("-")
        nome = partes[0].strip()
        ano = int(partes[1].strip())
        valor = float(partes[2].strip())

        equipamentos.append((nome, ano, valor))

    equipamentos.sort(key=lambda x: x[2], reverse=True)

    print("\n=== Total de equipamentos ===\n")
    posicao = 1

    for e in equipamentos:
        print(posicao, "- Equipamento:", e[0], "- Ano:", e[1], "- Valor:", "R$", e[2])
        posicao += 1

    print("\nTotal de Equipamentos:", len(equipamentos))


