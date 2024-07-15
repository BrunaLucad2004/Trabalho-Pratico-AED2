import Heap

#Configuração Final como variável global
estado_final = [[0, 1, 2], [3, 4, 5], [6, 7, 8]]

class Estado:
    def __init__(self, configuracao):
        #Controi uma configuração
        self.configuracao = configuracao
        #Calcula a heuristica dessa configuração
        self.heuristica = self.calcular_heuristica()

    def __lt__(self, other):
        return self.heuristica < other.heuristica

    def __repr__(self):
        return '\n'.join([' '.join(' ' if item == 0 else str(item) for item in linha) for linha in self.configuracao])

    #Esta função calcula a Heuristica de uma configuração, ou seja, quantas peças estão fora do lugar, exceto o '0'
    def calcular_heuristica(self):
        heuristica = 0
        for i in range(3):
            for j in range(3):
                if (self.configuracao[i][j] != 0) and (self.configuracao[i][j] != estado_final[i][j]):
                    heuristica += 1
        return heuristica
    
    #Esta função gera todos os estados possíveis que podem ser alcançados a partir do estado atual
    def transicoes(self):
        transicoes = []
        linha, coluna = next((i, sublist.index(0)) for i, sublist in enumerate(self.configuracao) if 0 in sublist)
        
        direcoes = {
            'W': (-1, 0), # W -> cima
            'S': (1, 0),  # S -> baixo
            'A': (0, -1), # A -> esquerda
            'D': (0, 1)   # D -> direita
        }
        
        for direcao, (x, y) in direcoes.items():
            nova_linha = linha + x
            nova_coluna = coluna + y
            if 0 <= nova_linha < len(self.configuracao) and 0 <= nova_coluna < len(self.configuracao[0]):
                novo_estado = [linha[:] for linha in self.configuracao]
                novo_estado[linha][coluna], novo_estado[nova_linha][nova_coluna] = novo_estado[nova_linha][nova_coluna], novo_estado[linha][coluna]
                transicoes.append((Estado(novo_estado), direcao))
        
        return transicoes

    #Esta função gera todos os movimentos possiveis a partir do estado atual
    def movimentos_possiveis(self):
         # Verifica se o valor '0' está na configuração
        linha, coluna = next((i, sublist.index(0)) for i, sublist in enumerate(self.configuracao) if 0 in sublist)
        
        direcoes = {
            'W': (-1, 0), # W -> cima
            'S': (1, 0),  # S -> baixo
            'A': (0, -1), # A -> esquerda
            'D': (0, 1)   # D -> direita
        }
        movimentos = []
        for direcao, (x, y) in direcoes.items():
            nova_linha = linha + x
            nova_coluna = coluna + y
            if 0 <= nova_linha < 3 and 0 <= nova_coluna < 3:
                movimentos.append(direcao)
        return movimentos

    #Esta função realiza um movimento e gera um novo estado
    def realizar_movimento(self, movimento):
        linha, coluna = next((i, sublist.index(0)) for i, sublist in enumerate(self.configuracao) if 0 in sublist)

        direcoes = {
            'W': (-1, 0), # W -> cima
            'S': (1, 0),  # S -> baixo
            'A': (0, -1), # A -> esquerda
            'D': (0, 1)   # D -> direita
        }

        if movimento in direcoes:
            x, y = direcoes[movimento]
            nova_linha = linha + x
            nova_coluna = coluna + y
            if (0 <= nova_linha < 3) and (0 <= nova_coluna < 3):
                novo_estado = [linha[:] for linha in self.configuracao]
                novo_estado[linha][coluna], novo_estado[nova_linha][nova_coluna] = novo_estado[nova_linha][nova_coluna], novo_estado[linha][coluna]
            return Estado(novo_estado)
        return self

    def reconstruir_caminho(veio_de, movimentos, atual):
        caminho = []
        while str(atual.configuracao) in veio_de:
            caminho.append((atual.configuracao, movimentos[str(atual.configuracao)]))
            atual = veio_de[str(atual.configuracao)]
        caminho.append((atual.configuracao, None))  # O estado inicial não tem movimento associado
        return caminho[::-1]

    def a_estrela(inicio):
        agenda = []
        Heap.heappush(agenda, len(agenda), (inicio.heuristica, inicio))
        veio_de = {}
        movimentos = {}
        custo_g = {str(inicio.configuracao): 0}
        custo_f = {str(inicio.configuracao): inicio.heuristica}

        while agenda:
            _, atual = Heap.heappop(agenda)
            if atual.configuracao == estado_final:
                return Estado.reconstruir_caminho(veio_de, movimentos, atual)

            for vizinho, direcao in atual.transicoes():
                custo_g_tentativo = custo_g[str(atual.configuracao)] + 1
                if str(vizinho.configuracao) not in custo_g or custo_g_tentativo < custo_g[str(vizinho.configuracao)]:
                    veio_de[str(vizinho.configuracao)] = atual
                    movimentos[str(vizinho.configuracao)] = direcao
                    custo_g[str(vizinho.configuracao)] = custo_g_tentativo
                    custo_f[str(vizinho.configuracao)] = custo_g_tentativo + vizinho.heuristica
                    Heap.heappush(agenda, len(agenda), (custo_f[str(vizinho.configuracao)], vizinho))

        return None
    
    def mostrar_resolucao(inicio):
        caminho = Estado.a_estrela(inicio)
        if caminho:
            for configuracao, movimento in caminho:
                print("Configuração:")
                for linha in configuracao:
                    print(linha)
                if movimento:
                    print(f"Movimento: {movimento}")
                print()
        else:
            print("Nenhum caminho encontrado.")

