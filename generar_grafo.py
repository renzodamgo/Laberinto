from random import *


# n vertices
# m aristas


def generargrafo(n, m):
    grafo = []
    for i in range(1, n + 1):
        arr = [i]
        grafo.append(arr)
    for i in range(m):
        i = i + 1
        x = randint(0, m + 1)
        grafo[x].append(i)
    return grafo


def generargrafov2(n, m):
    """
    :param int n: número de vértices
    :param int m: número de aristas
    :return: Un grafo de n vértices y m aristas
    """
    if (n * n) - n < m:
        return "Sobrepasa el máximo de aristas permitido"
    grafo = []
    edge_count = 0
    for i in range(n):
        arr = [i]
        grafo.append(arr)
    while edge_count < m:
        for i in range(n):
            for ari in range(n):
                aleatorio = getrandbits(1)
                if ari not in grafo[i] and aleatorio and edge_count < m:
                    grafo[i].append(ari)
                    edge_count = edge_count + 1

    return grafo


if __name__ == '__main__':
    print(generargrafov2(3,"dds"))
    randint("holas")
