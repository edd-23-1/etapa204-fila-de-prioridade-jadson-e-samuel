class No:
    def __init__(self, valor, prioridade):
        self.valor = valor
        self.prioridade = prioridade
        self.prox = None


class FilaPrioridade:
    """
    Implementação de Fila de Prioridade com Capacidade
    A fila de prioridade a ser implementada deverá ser em ordem crescente
    Os itens com maior prioridade devem ocupar as primeiras posições
    Itens com prioridades iguais devem ser ordenados conforme ordem de inserção
    """

    def __init__(self, capacidade=5):
        self.__inicio = None
        self.__capacidade = capacidade
        self.__qtdItens = 0
        print(f"Criada EDD Fila de Prioridade com capacidade: {capacidade}")

    def is_empty(self) -> bool:
        return self.__qtdItens == 0

    def is_full(self) -> bool:
        return self.__qtdItens == self.__capacidade

    def first(self) -> No:
        return self.__inicio

    def add(self, valor, prioridade) -> bool:
        no = No(valor, prioridade)

        if self.is_full():
            raise Exception("Lista cheia!")

        if self.is_empty() or prioridade > self.__inicio.prioridade:
            no.prox = self.__inicio
            self.__inicio = no
        else:
            pointer = self.__inicio
            while pointer.prox and prioridade <= pointer.prox.prioridade:
                pointer = pointer.prox

            no.prox = pointer.prox
            pointer.prox = no

        self.__qtdItens += 1
        return True

    def remove(self) -> No:
        if self.is_empty():
            raise Exception("Fila vazia")
        else:
            valor = self.__inicio
            self.__inicio = self.__inicio.prox
            self.__qtdItens -= 1
            return valor

    def display(self) -> list[tuple()]:
        if self.is_empty():
            print("Lista vazia!")
            return []

        lista = []
        pointer = self.__inicio
        while pointer:
            lista.append((pointer.valor, pointer.prioridade))
            pointer = pointer.prox
        return lista

    def size(self) -> int:
        return self.__qtdItens
