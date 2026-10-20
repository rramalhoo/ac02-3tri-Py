import csv
import json

def cadastrarEquipamento():
    equipamentos = []
    equipamento = input("Digite o equipamento: ")
    ano = input("Digite o ano: ")
    valor = input("Digite o valor: ")

    with open("equipamentos.txt", "a", encoding="utf-8") as arquivo:
        arquivo.write(equipamento + " - " + ano + " - " + valor + "\n")

    with open("equipamentos.csv", "a", newline="", encoding="utf-8") as arquivo:
        escritor = csv.writer(arquivo)
        escritor.writerow([equipamento, ano, valor])

    registro = {
        "equipamento": equipamento,
        "ano": ano,
        "valor": valor
    }

    with open("equipamentos.json", "r", encoding="utf-8") as arquivo:
        equipamentos = json.load(arquivo)

    equipamentos.append(registro)

    with open("equipamentos.json", "w", encoding="utf-8") as arquivo:
        json.dump(equipamentos, arquivo, indent=4, ensure_ascii=False)

    print("Equipamento salvo")

opc = 1

if opc == 1:
    cadastrarEquipamento()
else:
    print("Erro")
