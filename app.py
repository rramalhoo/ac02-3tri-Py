from funcoes.Cadastrar import cadastrarEquipamento
from funcoes.Historico import historicoEquipamentos
from funcoes.ListarRelatorio import listar
from funcoes.buscarEquipamentos import buscarEquipamento
from estilos.estilo import limparTela, titulo, opcao, erro, sucesso, pausar

while True:
    limparTela()
    titulo("Sistema de Inventário do Laboratório")
    print()
    opcao(1, "Cadastrar equipamento (TXT, CSV e JSON)")
    opcao(2, "Ver histórico de equipamentos (TXT)")
    opcao(3, "Listar inventário e gerar relatório (CSV)")
    opcao(4, "Buscar equipamento e estado de conservação (JSON)")
    opcao(5, "Sair")
    print()

    try:
        opc = int(input("Digite a opção: "))
    except ValueError:
        erro("Digite apenas números")
        pausar()
        continue

    if opc == 1:
        cadastrarEquipamento()
    elif opc == 2:
        historicoEquipamentos()
    elif opc == 3:
        listar()
    elif opc == 4:
        buscarEquipamento()
    elif opc == 5:
        sucesso("Programa encerrado")
        break
    else:
        erro("Opção inválida, digite um número de 1 a 5")

    pausar()
