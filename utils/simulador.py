import random
import datetime
from pathlib import Path
from utils.data_manager import save_data

# Garante que o diretório 'data' exista
Path("data").mkdir(exist_ok=True)


def generate_data(num_registros=50):
    """Gera uma lista de registros de consumo simulados."""
    insumos = [
        "Reagente Alpha",
        "Reagente Beta",
        "Placa de Petri",
        "Luvas Descartáveis M",
        "Agulha 30G",
        "Tubo de Ensaio",
        "Lâmina de Vidro",
        "Seringa 5ml",
    ]
    dados = []
    hoje = datetime.date.today()

    for i in range(num_registros):
        data_consumo = hoje - datetime.timedelta(days=i)
        item = {
            "nome_insumo": random.choice(insumos),
            "lote": f"L{random.randint(1000, 9999)}",
            "quantidade_consumida": random.randint(10, 200),
            "data_consumo": data_consumo.isoformat(),
            "validade": (
                data_consumo + datetime.timedelta(days=random.randint(90, 365))
            ).isoformat(),
        }
        dados.append(item)

    # Ordena por data de consumo para simular um registro cronológico
    dados.sort(key=lambda x: x["data_consumo"])

    for idx, item in enumerate(dados, start=1):
        item["id_insumo"] = idx

    return dados


if __name__ == "__main__":
    dados_simulados = generate_data()
    save_data(dados_simulados)
