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
    grafo = []
    edge_count = 0
    for i in range(n):
        arr = [i]
        grafo.append(arr)
        for ari in range(randint(0,n)):
            aleatorio = getrandbits(1)
            if ari != i and aleatorio:
                grafo[i].append(ari)

    return grafo


if __name__ == '__main__':
    # Genera un grafo de 8 nodos y 6 aristas
    print(generargrafov2(8, 10))
