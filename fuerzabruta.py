import generar_grafo as gg


def bruteforce(entrada, salida, grafo):
    c = 1
    while True:
        if grafo[entrada][c] != salida:
            entrada = grafo[entrada][c]


def bfs(entrada, grafo, salida):
    visitados = []
    parent = [None] * len(grafo)
    camino = [salida]
    i = 1
    frontier = [entrada]
    while frontier:
        next = []
        for u in frontier:
            for v in grafo[u]:
                if v not in visitados:
                    visitados.append(v)
                    next.append(v)
                    parent[v] = u
                if v == salida:
                    while True:
                        salida = parent[salida]
                        camino.append(salida)
                        if parent[salida] == salida:
                            return camino[::-1]

        frontier = next
        i += 1
    return "No se encontro camino"


def dfs(entrada, grafo, salida):
    visitados = []
    parent = [None] * len(grafo)
    camino = [salida]
    i = 1
    frontier = [entrada]
    while frontier:
        next = []
        for u in frontier:
            for v in grafo[u]:
                if v not in visitados:
                    visitados.append(v)
                    next.insert(0, v)
                    parent[v] = u
                if v == salida:
                    while True:
                        salida = parent[salida]
                        camino.append(salida)
                        if parent[salida] == salida:
                            return camino[::-1]

        frontier = next
        i += 1
    return "No se encontro camino"


if __name__ == '__main__':
    #grafo = gg.generargrafov2(5, 15)

    grafo = [[0, 1, 2, 4, 3], [1, 2, 3], [2, 0, 3, 4], [3, 2, 0], [4, 0, 1, 2, 3]]
    print(grafo)

    print("bfs: " + str(bfs(3, grafo, 4)))
    print("dfs: " + str(dfs(3, grafo, 4)))

# [[0, 1, 2, 4, 3], [1, 2, 3], [2, 0, 3, 4], [3, 2, 0], [4, 0, 1, 2, 3]]
# [3, 2, 4] BFS
# DFS
