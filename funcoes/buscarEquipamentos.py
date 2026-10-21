import json
from estilos.caminhos import ARQUIVO_JSON


def definir_nivel(valor):
    if valor < 50:
        return "Necessita Substituição"
    elif valor < 80:
        return "Regular"
    else:
        return "Excelente Estado"


def buscarEquipamento():
    busca = input("Digite o nome do equipamento: ").strip().lower()

    try:
        with open(ARQUIVO_JSON, "r", encoding="utf-8") as arquivo:
            equipamentos = json.load(arquivo)
    except (FileNotFoundError, json.JSONDecodeError):
        equipamentos = []

    encontrado = False

    for e in equipamentos:
        if e["nome"].lower() == busca:
            encontrado = True
            print("\n=== EQUIPAMENTO ENCONTRADO ===\n")
            print("Nome:", e["nome"])
            print("Ano:", e["ano"])
            print(f"Valor: R$ {e['valor']:.2f}")
            print("Estado de Conservação:", definir_nivel(e["valor"]))

    if not encontrado:
        print("\nEquipamento não localizado")

    print()
