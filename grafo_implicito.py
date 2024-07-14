import heapq

def heuristica(estado, objetivo):
    return sum(1 for i in range(9) if estado[i] != objetivo[i] and estado[i] != 0)

def obter_vizinhos(estado):
    vizinhos = []
    indice_zero = estado.index(0)
    linha, coluna = divmod(indice_zero, 3)
    direcoes = [(-1, 0), (1, 0), (0, -1), (0, 1)]
    for dr, dc in direcoes:
        nova_linha, nova_coluna = linha + dr, coluna + dc
        if 0 <= nova_linha < 3 and 0 <= nova_coluna < 3:
            novo_indice = nova_linha * 3 + nova_coluna
            novo_estado = estado[:]
            novo_estado[indice_zero], novo_estado[novo_indice] = novo_estado[novo_indice], novo_estado[indice_zero]
            vizinhos.append(novo_estado)
    return vizinhos

def reconstruir_caminho(veio_de, atual):
    caminho = []
    while tuple(atual) in veio_de:
        caminho.append(atual)
        atual = veio_de[tuple(atual)]
    caminho.append(atual)
    return caminho[::-1]

def a_estrela(inicio, objetivo):
    conjunto_aberto = []
    heapq.heappush(conjunto_aberto, (heuristica(inicio, objetivo), inicio))
    veio_de = {}
    custo_g = {tuple(inicio): 0}
    custo_f = {tuple(inicio): heuristica(inicio, objetivo)}

    while conjunto_aberto:
        _, atual = heapq.heappop(conjunto_aberto)
        if atual == objetivo:
            return reconstruir_caminho(veio_de, atual)

        for vizinho in obter_vizinhos(atual):
            custo_g_tentativo = custo_g[tuple(atual)] + 1
            if tuple(vizinho) not in custo_g or custo_g_tentativo < custo_g[tuple(vizinho)]:
                veio_de[tuple(vizinho)] = atual
                custo_g[tuple(vizinho)] = custo_g_tentativo
                custo_f[tuple(vizinho)] = custo_g_tentativo + heuristica(vizinho, objetivo)
                heapq.heappush(conjunto_aberto, (custo_f[tuple(vizinho)], vizinho))

    return None

def movimentos_possiveis(estado):
    indice_zero = estado.index(0)
    linha, coluna = divmod(indice_zero, 3)
    direcoes = {
        'cima': (-1, 0),
        'baixo': (1, 0),
        'esquerda': (0, -1),
        'direita': (0, 1)
    }
    movimentos = []
    for direcao, (dr, dc) in direcoes.items():
        nova_linha, nova_coluna = linha + dr, coluna + dc
        if 0 <= nova_linha < 3 and 0 <= nova_coluna < 3:
            movimentos.append(direcao)
    return movimentos

def realizar_movimento(estado, movimento):
    indice_zero = estado.index(0)
    linha, coluna = divmod(indice_zero, 3)
    direcoes = {
        'cima': (-1, 0),
        'baixo': (1, 0),
        'esquerda': (0, -1),
        'direita': (0, 1)
    }
    if movimento in direcoes:
        dr, dc = direcoes[movimento]
        nova_linha, nova_coluna = linha + dr, coluna + dc
        if 0 <= nova_linha < 3 and 0 <= nova_coluna < 3:
            novo_indice = nova_linha * 3 + nova_coluna
            novo_estado = estado[:]
            novo_estado[indice_zero], novo_estado[novo_indice] = novo_estado[novo_indice], novo_estado[indice_zero]
            return novo_estado
    return estado

def mostrar_resolucao(inicio, objetivo):
    caminho = a_estrela(inicio, objetivo)
    if caminho:
        print("Resolução encontrada:")
        for estado in caminho:
            print(estado)
    else:
        print("Nenhuma solução encontrada.")

# Exemplo de uso
estado_inicial = [6, 2, 8, 4, 0, 1, 5, 3, 7]
objetivo = [0, 1, 2, 3, 4, 5, 6, 7, 8]

print("Estado inicial:", estado_inicial)

# Mostrar a resolução automática
mostrar_resolucao(estado_inicial, objetivo)
