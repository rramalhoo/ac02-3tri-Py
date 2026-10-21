import os

# Códigos de cor ANSI para o terminal
RESET = "\033[0m"
NEGRITO = "\033[1m"
CIANO = "\033[96m"
VERDE = "\033[92m"
AMARELO = "\033[93m"
VERMELHO = "\033[91m"

LARGURA = 56


def limparTela():
    os.system("cls" if os.name == "nt" else "clear")


def titulo(texto):
    print(CIANO + "╔" + "═" * LARGURA + "╗")
    print("║" + NEGRITO + texto.center(LARGURA) + RESET + CIANO + "║")
    print("╚" + "═" * LARGURA + "╝" + RESET)


def opcao(numero, texto):
    print(f"  {AMARELO}{NEGRITO}[{numero}]{RESET} {texto}")


def sucesso(texto):
    print(VERDE + "✔ " + texto + RESET)


def erro(texto):
    print(VERMELHO + "✖ " + texto + RESET)


def pausar():
    input(f"\n{CIANO}Pressione ENTER para voltar ao menu...{RESET}")
