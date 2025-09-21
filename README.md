# 🏥 Gerenciador de Insumos de Diagnóstico

![Python Version](https://img.shields.io/badge/python-3.13%2B-blue)
![License](https://img.shields.io/badge/license-MIT-green)

## 🌐 Link do Projeto

Acesse o repositório completo no GitHub: [Asteriuz/challenge3-dynamic_programming](https://github.com/Asteriuz/challenge3-dynamic_programming)

## 📖 Sobre o Projeto

Este projeto foi desenvolvido como uma solução para o desafio de gerenciar o consumo de insumos em unidades de diagnóstico. A falta de um registro preciso dificulta o controle de estoque e a previsão de reposição.

A aplicação simula o consumo diário de insumos (reagentes, descartáveis, etc.) e utiliza estruturas de dados e algoritmos clássicos para organizar e consultar esses dados de forma eficiente, tudo através de uma interface de linha de comando interativa e amigável construída com a biblioteca `rich`.

## ✨ Funcionalidades Principais

O sistema oferece um menu com diversas opções para manipulação e visualização dos dados de consumo:

- **Simulação de Dados**: Gera um conjunto de dados de consumo de insumos com informações como nome, lote, quantidade, data de consumo e validade.
- **Visualização Cronológica (Fila)**: Exibe os registros de consumo na ordem em que aconteceram (FIFO - _First-In, First-Out_), simulando um log de eventos.
- **Visualização Inversa (Pilha)**: Mostra os últimos consumos registrados primeiro (LIFO - _Last-In, First-Out_), útil para consultar as atividades mais recentes.
- **Busca de Insumos**:
  - **Busca Sequencial**: Permite encontrar um insumo pelo nome, percorrendo toda a lista de registros.
  - **Busca Binária**: Realiza uma busca otimizada por nome em uma lista pré-ordenada, sendo significativamente mais rápida para grandes volumes de dados.
- **Ordenação Avançada**:
  - **Merge Sort**: Organiza os dados de consumo com base em um campo escolhido (ID, nome, lote, quantidade, etc.) usando um algoritmo estável e eficiente.
  - **Quick Sort**: Oferece uma alternativa de ordenação rápida (em média) para os mesmos campos.
- **Persistência de Dados**: Os dados simulados são salvos em um arquivo `consumo.json`, permitindo que o estado da aplicação seja mantido entre as execuções.

## 🚀 Tecnologias Utilizadas

- **[Python 3.13+](https://www.python.org/)**: Linguagem principal do projeto.
- **[Rich](https://github.com/Textualize/rich)**: Para criar uma interface de linha de comando rica e colorida, com tabelas, painéis e texto estilizado.

## 🛠️ Instalação e Execução

Siga os passos abaixo para configurar e executar o projeto em seu ambiente local.
Você pode usar **pip** (tradicional) ou **uv** (recomendado, mais rápido e simples).

1. **Clone o repositório:**

   ```sh
   git clone https://github.com/Asteriuz/challenge3-dynamic_programming.git
   cd gerenciador-insumos
   ```

### 🔹 Opção 1 — Usando `pip` (tradicional)

2. **Crie e ative um ambiente virtual:**

   ```sh
   python -m venv .venv

   # Windows
   .\.venv\Scripts\activate

   # macOS/Linux
   source .venv/bin/activate
   ```

3. **Instale as dependências:**

   ```sh
   pip install -r requirements.txt
   ```

4. **Execute a aplicação:**

   ```sh
   python main.py
   ```

   _Na primeira execução, se o arquivo `data/consumo.json` não existir, o programa perguntará se você deseja gerar dados simulados._

### 🔹 Opção 2 — Usando `uv` (recomendado 🚀)

2. **Instale o `uv` (se ainda não tiver):**

   ```sh
   pip install uv
   ```

3. **Sincronize as dependências automaticamente (Opcional | _uv run realiza o sync antes_):**

   ```sh
   uv sync
   ```

   > Isso cria e gerencia o ambiente virtual automaticamente, sem precisar rodar `venv` manualmente.

4. **Execute a aplicação dentro do ambiente:**

   ```sh
   uv run python main.py
   ```

## 🧠 Implementação de Estruturas e Algoritmos

- **Fila e Pilha (`core/fila_pilha.py`)**:

  - `FilaConsumo`: Utiliza `collections.deque`, uma implementação otimizada de fila em Python, para gerenciar os dados em ordem cronológica (FIFO).
  - `PilhaConsumo`: Implementada com uma lista Python (`list`), onde `append()` e `pop()` simulam as operações de _push_ e _pop_ de uma pilha (LIFO). A visualização é feita invertendo a ordem da lista.

- **Busca (`core/busca.py`)**:

  - `busca_sequencial`: Itera sobre cada item da lista, comparando o valor da chave especificada. Tem complexidade **O(n)**.
  - `busca_binaria`: Funciona em uma lista pré-ordenada, dividindo repetidamente o intervalo de busca pela metade. Tem complexidade **O(log n)**, sendo muito mais eficiente para grandes conjuntos de dados.

- **Ordenação (`core/ordenacao.py`)**:
  - `merge_sort`: Um algoritmo de "dividir para conquistar" que divide a lista em metades, ordena-as recursivamente e depois as mescla. Garante uma complexidade de **O(n log n)** em todos os casos.
  - `quick_sort`: Também de "dividir para conquistar", escolhe um pivô e particiona a lista. Sua complexidade média é **O(n log n)**, mas pode degradar para **O(n²)** no pior caso. A implementação aqui é _out-of-place_ para maior simplicidade.

## 📂 Estrutura do Projeto

```
.
├── core/               # Módulos com a lógica principal (estruturas e algoritmos)
│   ├── busca.py
│   ├── fila_pilha.py
│   └── ordenacao.py
├── data/               # Armazena os dados simulados
│   └── consumo.json
├── ui/                 # Módulos responsáveis pela interface
│   ├── menu.py
│   └── menu_logic.py
├── utils/              # Módulos de utilidades
│   ├── data_manager.py
│   └── simulador.py
├── .gitignore
├── main.py             # Arquivo principal para executar a aplicação
├── pyproject.toml
├── README.md
└── requirements.txt
```
