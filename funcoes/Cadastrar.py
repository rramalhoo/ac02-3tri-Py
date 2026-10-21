import csv
import json
from estilos.caminhos import ARQUIVO_TXT, ARQUIVO_CSV, ARQUIVO_JSON


def cadastrarEquipamento():
    continuar = "s"

    while continuar == "s":
        salvarEquipamento()
        continuar = input("Deseja cadastrar um novo? (s/n): ").strip().lower()


def salvarEquipamento():
    nome = input("Digite o equipamento: ")
    ano = int(input("Digite o ano: "))
    valor = float(input("Digite o valor: "))

    with open(ARQUIVO_TXT, "a", encoding="utf-8") as arquivo:
        arquivo.write(f"{nome} - {ano} - {valor}\n")

    with open(ARQUIVO_CSV, "a", newline="", encoding="utf-8") as arquivo:
        escritor = csv.writer(arquivo)
        escritor.writerow([nome, ano, valor])

    registro = {
        "nome": nome,
        "ano": ano,
        "valor": valor
    }

    try:
        with open(ARQUIVO_JSON, "r", encoding="utf-8") as arquivo:
            equipamentos = json.load(arquivo)
    except (FileNotFoundError, json.JSONDecodeError):
        equipamentos = []

    equipamentos.append(registro)

    with open(ARQUIVO_JSON, "w", encoding="utf-8") as arquivo:
        json.dump(equipamentos, arquivo, indent=4, ensure_ascii=False)

    print("Equipamento salvo\n")
