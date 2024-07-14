import heapq

#Configuração Final como variável global
estado_final = [[0, 1, 2], [3, 4, 5], [6, 7, 8]]


class Estado:
    def __init__(self, configuracao):
        #Controi uma configuração
        self.configuracao = configuracao
        #Calcula a heuristica dessa configuração
        self.heuristica = self.calcular_heuristica()

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
