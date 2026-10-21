import csv
import json

def cadastrarEquipamento():
    nome = input("Digite o equipamento: ")
    ano = int(input("Digite o ano: "))
    valor = float(input("Digite o valor: "))

    with open("equipamentos.txt", "a", encoding="utf-8") as arquivo:
        arquivo.write(f"{nome} - {ano} - {valor}\n")

    with open("equipamentos.csv", "a", newline="", encoding="utf-8") as arquivo:
        escritor = csv.writer(arquivo)
        escritor.writerow([nome, ano, valor])

    registro = {
        "nome": nome,
        "ano": ano,
        "valor": valor
    }

    try:
        with open("equipamentos.json", "r", encoding="utf-8") as arquivo:
            equipamentos = json.load(arquivo)
    except (FileNotFoundError, json.JSONDecodeError):
        equipamentos = []

    equipamentos.append(registro)

    with open("equipamentos.json", "w", encoding="utf-8") as arquivo:
        json.dump(equipamentos, arquivo, indent=4, ensure_ascii=False)

    print("Equipamento salvo")

opc = 1

if opc == 1:
    cadastrarEquipamento()
else:
    print("Erro")
