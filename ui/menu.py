from rich.console import Console
from rich.panel import Panel
from rich.table import Table
from rich.prompt import Prompt, IntPrompt
from rich.text import Text

console = Console()


def show_main_menu(config):
    """Exibe o menu principal estilizado com grupos e cores"""
    menu_text = Text()

    for group_index, group in enumerate(config["groups"]):
        menu_text.append(f"{group['title']}\n", style=" bold " + group["color"])
        for option in group["options"]:
            is_last_group = group_index == len(config["groups"]) - 1
            is_last_option = option == group["options"][-1]
            option_line = f"  [{option['number']}] {option['description']}"
            if not (is_last_group and is_last_option):
                option_line += "\n"
            menu_text.append(option_line, style=f"{group['color']}")
        if group_index < len(config["groups"]) - 1:
            menu_text.append("\n")

    panel = Panel.fit(
        menu_text,
        title=config["panel_title"],
        border_style=config["panel_border_style"],
        padding=(1, 2),
    )
    console.print(panel, new_line_start=True)


def get_valid_menu_options(config):
    """Retorna uma lista com os números de opções válidas do menu."""
    valid_options = []
    for group in config["groups"]:
        for option in group["options"]:
            valid_options.append(option["number"])
    return valid_options


def get_menu_option_description(option_number, config):
    """Retorna a descrição de uma opção específica do menu."""
    for group in config["groups"]:
        for option in group["options"]:
            if option["number"] == option_number:
                return option["description"]
    return None


def ask_input(prompt_text="Escolha uma opção: ", choices=None):
    """Solicita uma entrada do usuário."""
    return Prompt.ask(prompt_text, choices=choices)


def ask_input_int(prompt_text="Escolha uma opção: ", default=None):
    """Solicita um número inteiro do usuário."""
    return IntPrompt.ask(prompt_text, default=default)


def show_data(data, title="Registros de Consumo"):
    """Exibe uma lista de dados de consumo em uma tabela bonita."""
    if not data:
        console.print(f"[bold red]❌ Nenhum dado para exibir.[/bold red]")
        return

    if isinstance(data, dict):
        data = [data]

    table = Table(title=f"📋 {title}", show_header=True, header_style="bold bright_white")
    table.add_column("🆔 ID", style="white", width=6)
    table.add_column("🧪 Nome do Insumo", min_width=20, style="cyan")
    table.add_column("📦 Lote", style="yellow")
    table.add_column("📊 Qtd. Consumida", justify="right", style="green")
    table.add_column("📅 Data Consumo", style="magenta")
    table.add_column("⏰ Validade", style="dark_magenta")

    for item in data:
        table.add_row(
            str(item["id_insumo"]),
            item["nome_insumo"],
            item["lote"],
            str(item["quantidade_consumida"]),
            item["data_consumo"],
            item["validade"],
        )

    console.print(table, new_line_start=True, end="\n\n")


def show_message(message, style="bold green"):
    """Exibe uma mensagem simples estilizada."""
    console.print(f"\n[{style}]{message}[/{style}]\n")
