from bfs import BFS
import heapq
import sys


class AStarHamming(BFS):
    def __init__(self, raiz: str, objetivo="12345678_"):
        super().__init__(raiz, objetivo)
        self.indice = 0

    def inicia_fronteira(self):
        fronteira = [(0, self.nodo_raiz)]
        return fronteira

    def push_nodo_fronteira(self, sucessor):
        heuristica = self.get_heuristica(sucessor)
        heapq.heappush(self.fronteira, (heuristica+sucessor.custo_caminho, self.indice, sucessor))
        self.indice += 1

    def pop_nodo_fronteira(self):
        return heapq.heappop(self.fronteira)[-1]

    def nao_estah_sucessor_na_fronteira(self, sucessor):
        for *_, nodo in self.fronteira:
            if nodo == sucessor:
                return False
        return True

    def get_heuristica(self, sucessor):
        objetivo = "185432_67"
        return sum(peca_sucessor != peca_objetivo for peca_sucessor, peca_objetivo in zip(sucessor.estado, objetivo))


if __name__ == "__main__":
    estado = sys.argv[1]
    grafo = AStarHamming(estado)
    caminho = grafo.acha_objetivo()
    if caminho:
        print(' '.join([nodo.acao for nodo in caminho[1:]]))
