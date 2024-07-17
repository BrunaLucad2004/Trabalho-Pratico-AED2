import Heap

#Configuração Final como variável global
estado_final = [[0, 1, 2], [3, 4, 5], [6, 7, 8]]

#Dicionario com as direções
direcoes = { 'W': (-1, 0), 'S': (1, 0), 'A': (0, -1), 'D': (0, 1)}
#             W -> cima     S -> baixo   A-> esquerda  D -> direita

class Estado:
    def __init__(self, configuracao):
        #Controi uma configuração
        self.configuracao = configuracao
        #Calcula a heuristica dessa configuração
        self.heuristica = self.calcular_heuristica()

    def __lt__(self, other):
        #Vai ordenar pela menor heuristica 
        return self.heuristica < other.heuristica

    def __repr__(self):
        #Definindo a representação da "matriz" do puzzel
        return '\n'.join([' '.join(' ' if item == 0 else str(item) for item in linha) for linha in self.configuracao])

    #Esta função calcula a Heuristica de uma configuração, ou seja, quantas peças estão fora do lugar, exceto o '0'
    def calcular_heuristica(self):
        heuristica = 0
        for i in range(3):
            for j in range(3):
                if (self.configuracao[i][j] != 0) and (self.configuracao[i][j] != estado_final[i][j]):
                    heuristica += 1
        return heuristica
    
    def encontrar_zero(self):
        # Itera sobre cada lista em self.configuracao com seus índices
        for i, lista in enumerate(self.configuracao):
            # Verifica se 0 está na lista
            if 0 in lista:
                # Retorna a posição do zero
                return i, lista.index(0)
        return None, None

    
    def gerar_novo_estado(self, linha, coluna, nova_linha, nova_coluna):
        # Cria um outro estado a partir do atual
        novo_estado = []
        for linha_atual in self.configuracao:
            nova_linha_atual = linha_atual[:]
            novo_estado.append(nova_linha_atual)
        
        # Troca valores
        novo_estado[linha][coluna], novo_estado[nova_linha][nova_coluna] = novo_estado[nova_linha][nova_coluna], novo_estado[linha][coluna]
        
        return novo_estado
    

    #Esta função gera todos os estados possíveis que podem ser alcançados a partir do estado atual
    def transicoes(self):
        transicoes = []

        # Verifica se o valor '0' está na configuração
        linha, coluna = self.encontrar_zero()

        for direcao, (x, y) in direcoes.items():
            nova_linha = linha + x
            nova_coluna = coluna + y
            if ((0 <= nova_linha) and (nova_linha < len(self.configuracao))) and ((0 <= nova_coluna) and (nova_coluna < len(self.configuracao[0]))):
                # Gera um novo estado usando a função modularizada
                novo_estado = self.gerar_novo_estado(linha, coluna, nova_linha, nova_coluna)
                #adiciona essa nova configuração a lista de transições, junto com o movimento que a tornou possivel
                transicoes.append((Estado(novo_estado), direcao))
        
        return transicoes

    #Esta função gera todos os movimentos possiveis a partir do estado atual
    def movimentos_possiveis(self):
        # Verifica se o valor '0' está na configuração
        linha, coluna = self.encontrar_zero()
        
        movimentos = []
        for direcao, (x, y) in direcoes.items():
            nova_linha = linha + x
            nova_coluna = coluna + y
            if 0 <= nova_linha < 3 and 0 <= nova_coluna < 3:
                movimentos.append(direcao)
        return movimentos

    #Esta função realiza um movimento e gera um novo estado
    def realizar_movimento(self, movimento):
        # Verifica se o valor '0' está na configuração
        linha, coluna = self.encontrar_zero()

        if movimento in direcoes:
            x, y = direcoes[movimento]
            nova_linha = linha + x
            nova_coluna = coluna + y
            if (0 <= nova_linha < 3) and (0 <= nova_coluna < 3):
                # Gera um novo estado usando a função modularizada
                novo_estado = self.gerar_novo_estado(linha, coluna, nova_linha, nova_coluna)
            return Estado(novo_estado)
        return self

    #CONTINUAR INSPEÇÃO DAQUI

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

#verificar se concluiu o jogo
