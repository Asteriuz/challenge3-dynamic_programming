import json
from pathlib import Path

ARQUIVO_JSON = Path("data/consumo.json")


def load_data():
    """Carrega os dados de consumo do arquivo JSON."""
    if not ARQUIVO_JSON.exists():
        return []
    try:
        with open(ARQUIVO_JSON, "r", encoding="utf-8") as f:
            return json.load(f)
    except (json.JSONDecodeError, FileNotFoundError):
        return []


def save_data(dados):
    """Salva os dados gerados no arquivo JSON."""
    with open(ARQUIVO_JSON, "w", encoding="utf-8") as f:
        json.dump(dados, f, indent=4, ensure_ascii=False)
    print(f"✅ {len(dados)} registros simulados foram salvos em '{ARQUIVO_JSON}'")
