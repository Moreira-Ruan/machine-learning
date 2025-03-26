from collections import deque

grafo = {
    'A': ['B', 'C'],
    'B': ['D', 'E'],
    'C': ['F'],
    'D': [],
    'E': ['F'],
    'F': []
}


def bfs(grafo, inicio, objetivo):
    fila = deque([[inicio]])

    while fila:
        caminho = fila.popleft()
        nodo = caminho[-1]

        if nodo == objetivo:
            return caminho

        for vizinho in grafo.get(nodo, []):
            novo_caminho = list(caminho)
            novo_caminho.append(vizinho)
            fila.append(novo_caminho)

    return None

print(bfs(grafo, 'A', 'F'))
