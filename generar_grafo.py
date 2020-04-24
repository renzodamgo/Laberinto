import random
# n vertices
# m aristas

def generargrafo(n,m):
    grafo = []
    for i in range(1,n+1):
        arr = [i]
        grafo.append(arr)
    for i in range(m):
        i = i + 1
        x = random.randint(0,m+1)
        grafo[x].append(i)
    return grafo


if __name__ == '__main__':
    # Genera un grafo de 8 nodos y 6 aristas
    print(generargrafo(8,6))
