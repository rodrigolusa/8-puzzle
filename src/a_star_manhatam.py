import numpy as np

from a_star_hamming import AStarHamming
import sys


class AStarManhattan(AStarHamming):
    def __init__(self, raiz: str, objetivo="12345678_"):
        super().__init__(raiz, objetivo)
        self.indice = 0

    def get_matrix(self, nodo):
        return np.array(list(nodo.estado)).reshape(3, 3)

    def procura_termo(self, estado, termo):
        i, j = np.where(estado == termo)
        return i[0], j[0]

    def get_heuristica(self, sucessor):
        posicoes_corretas = {"1": (0, 0), "2": (0, 1), "3": (0, 2),
                             "4": (1, 0), "5": (1, 1), "6": (1, 2),
                             "7": (2, 0), "8": (2, 1), "_": (2, 2)}

        sucessor = self.get_matrix(sucessor)
        custo = 0
        for elemento, (i_correto, j_correto) in posicoes_corretas.items():
            i, j = self.procura_termo(sucessor, elemento)
            custo += abs(i-i_correto) + abs(j-j_correto)
        return custo


if __name__ == "__main__":
    estado = sys.argv[1]
    grafo = AStarManhattan(estado)
    caminho = grafo.acha_objetivo()
    if caminho:
        print(' '.join([nodo.acao for nodo in caminho[1:]]))
