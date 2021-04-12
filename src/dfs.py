from bfs import BFS
import sys


class DFS(BFS):
    def __init__(self, raiz: str, objetivo="12345678_"):
        super().__init__(raiz, objetivo)

    def pop_nodo_fronteira(self):
        return self.fronteira.pop()


if __name__ == "__main__":
    estado = sys.argv[1]
    grafo = DFS(estado)
    caminho = grafo.acha_objetivo()
    if caminho:
        print(' '.join([nodo.acao for nodo in caminho[1:]]))
