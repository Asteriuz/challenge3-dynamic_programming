from ui import menu
from utils import data_manager, simulador
from core import fila_pilha, busca, ordenacao
import sys
import time
from os import system, name


def clear_console():
    """Limpa o console de forma cross-platform."""
    if name == "nt":
        _ = system("cls")
    else:
        _ = system("clear")


MENU_CONFIG = {
    "panel_title": "[bold magenta]🏥 Gerenciador de Insumos de Diagnóstico[/bold magenta]",
    "panel_border_style": "bold cyan",
    "groups": [
        {
            "title": "📊 VISUALIZAÇÃO DE DADOS",
            "color": "blue",
            "options": [
                {
                    "number": 1,
                    "description": "Visualizar Consumo (Fila - Cronológico)",
                },
                {
                    "number": 2,
                    "description": "Visualizar Consumo (Pilha - Inverso)",
                },
            ],
        },
        {
            "title": "🔍 BUSCA DE INSUMOS",
            "color": "green",
            "options": [
                {
                    "number": 3,
                    "description": "Buscar Insumo (Busca Sequencial)",
                },
                {
                    "number": 4,
                    "description": "Buscar Insumo (Busca Binária)",
                },
            ],
        },
        {
            "title": "📈 ORDENAÇÃO POR CONSUMO/VALIDADE",
            "color": "yellow",
            "options": [
                {
                    "number": 5,
                    "description": "(Merge Sort)",
                },
                {
                    "number": 6,
                    "description": "(Quick Sort)",
                },
            ],
        },
        {
            "title": "⚙️  GERENCIAMENTO",
            "color": "cyan",
            "options": [
                {
                    "number": 7,
                    "description": "Regenerar Dados Simulados",
                },
            ],
        },
        {
            "title": "🚪 SISTEMA",
            "color": "red",
            "options": [
                {
                    "number": 8,
                    "description": "Sair",
                },
            ],
        },
    ],
}


def main():
    """Função principal que executa o loop da aplicação."""
    dados_consumo = data_manager.load_data()

    if not dados_consumo:
        menu.console.print(
            "[bold yellow]Atenção:[/bold yellow] O arquivo 'data/consumo.json' está vazio ou não foi encontrado."
        )
        resposta = menu.ask_input(
            "Deseja gerar dados simulados automaticamente?", choices=["s", "n"]
        )

        if resposta.lower() == "s":
            menu.console.print("[bold blue]Gerando dados simulados...[/bold blue]")
            dados_simulados = simulador.generate_data()
            data_manager.save_data(dados_simulados)
            dados_consumo = dados_simulados
            menu.console.print(
                "[bold green]✅ Dados simulados gerados com sucesso![/bold green]"
            )
        else:
            menu.console.print(
                "[bold red]Sistema encerrado. Execute novamente quando tiver dados disponíveis.[/bold red]"
            )
            sys.exit()

    fila = fila_pilha.FilaConsumo(dados_consumo)
    pilha = fila_pilha.PilhaConsumo(dados_consumo)

    clear_console()

    while True:
        menu.show_main_menu(MENU_CONFIG)
        opcao = menu.ask_input_int("Digite o número da sua opção")
        valid_options = menu.get_valid_menu_options(MENU_CONFIG)

        if (
            opcao in valid_options and opcao != 8
        ):  # Clear console for all options except exit
            clear_console()

        if opcao == 1:
            menu.show_data(
                fila.get_all(), "Consumo em Ordem Cronológica (FIFO - Fila)"
            )

        elif opcao == 2:
            menu.show_data(pilha.get_all(), "Últimos Consumos (LIFO - Pilha)")

        elif opcao == 3:
            nome_insumo = menu.ask_input("🔍 Digite o nome do insumo a buscar")
            resultado = busca.busca_sequencial(
                dados_consumo, "nome_insumo", nome_insumo
            )
            if resultado:
                menu.show_data(
                    resultado, f"Resultado da Busca Sequencial por '{nome_insumo}'"
                )
            else:
                menu.show_message(
                    f"❌ Insumo '{nome_insumo}' não encontrado.", "bold red"
                )

        elif opcao == 4:
            menu.show_message(
                "ℹ️  Para a busca binária, a lista será ordenada por nome.", "bold cyan"
            )
            # A busca binária exige uma lista ordenada
            dados_ordenados = sorted(dados_consumo, key=lambda x: x["nome_insumo"])
            nome_insumo = menu.ask_input("🔍 Digite o nome do insumo a buscar")
            resultado = busca.busca_binaria(dados_ordenados, "nome_insumo", nome_insumo)
            if resultado:
                menu.show_data(
                    resultado, f"Resultado da Busca Binária por '{nome_insumo}'"
                )
            else:
                menu.show_message(
                    f"❌ Insumo '{nome_insumo}' não encontrado.", "bold red"
                )

        elif opcao == 5 or opcao == 6:
            algoritmo = "⚡ Merge Sort" if opcao == 5 else "🚀 Quick Sort"
            menu.show_message(f"📈 Ordenando com {algoritmo}...", "bold blue")
            chave_ordenacao = menu.ask_input(
                "📊 Ordenar por [1] Quantidade Consumida ou [2] Validade?",
                choices=["1", "2"],
            )

            chave = "quantidade_consumida" if chave_ordenacao == "1" else "validade"

            inicio = time.time()

            if opcao == 5:
                dados_ordenados = ordenacao.merge_sort(dados_consumo, chave)
            elif opcao == 6:  # opcao == 6
                dados_ordenados = ordenacao.quick_sort(dados_consumo, chave)

            fim = time.time()
            tempo_ordenacao = (fim - inicio) * 1000

            icon = "⚡" if opcao == 5 else "🚀"
            titulo = f"{icon} Insumos Ordenados por '{chave}' usando {algoritmo} (⏱️ Tempo: {tempo_ordenacao:.2f}ms)"
            menu.show_data(dados_ordenados, titulo)

        elif opcao == 7:
            # Regenerar dados simulados
            num_registros = menu.ask_input_int(
                "📊 Quantos registros deseja gerar?", default=50
            )
            menu.show_message("🔄 Regenerando dados simulados...", "bold blue")
            dados_simulados = simulador.generate_data(num_registros)
            data_manager.save_data(dados_simulados)
            dados_consumo = dados_simulados
            fila = fila_pilha.FilaConsumo(dados_consumo)
            pilha = fila_pilha.PilhaConsumo(dados_consumo)
            menu.show_message(
                "✅ Dados simulados regenerados com sucesso!",
                "bold green",
            )

        elif opcao == 8:
            menu.show_message("👋 Saindo do sistema. Até logo!", "bold magenta")
            break

        else:
            menu.show_message("❌ Opção inválida. Tente novamente.", "bold red")


if __name__ == "__main__":
    clear_console()
    main()
