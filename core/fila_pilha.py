from collections import deque


class FilaConsumo:
    """Estrutura de Fila para gerenciar consumo em ordem cronológica (FIFO)."""

    def __init__(self, items_iniciais=None):
        if items_iniciais is None:
            items_iniciais = []

        self.fila = deque(items_iniciais)

    def add(self, item):
        """Adiciona um item ao final da fila."""
        self.fila.append(item)

    def remove(self):
        """Remove e retorna o primeiro item da fila."""
        if not self.is_empty():
            return self.fila.popleft()
        return None

    def is_empty(self):
        """Verifica se a fila está vazia."""
        return not self.fila

    def get_all(self):
        """Retorna uma lista com todos os items na ordem da fila."""
        return list(self.fila)


class PilhaConsumo:
    """Estrutura de Pilha para gerenciar consumo em ordem inversa (LIFO)."""

    def __init__(self, items_iniciais=None):
        if items_iniciais is None:
            items_iniciais = []
        self.pilha = list(items_iniciais)

    def append(self, item):
        """Adiciona um item ao topo da pilha."""
        self.pilha.append(item)

    def pop(self):
        """Remove e retorna o item do topo da pilha."""
        if not self.is_empty():
            return self.pilha.pop()
        return None

    def is_empty(self):
        """Verifica se a pilha está vazia."""
        return not self.pilha

    def get_all(self):
        """Retorna uma lista com todos os items na ordem inversa de inserção."""
        return list(reversed(self.pilha))
