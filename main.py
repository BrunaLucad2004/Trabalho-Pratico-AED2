import random
import Estado

#gerar um estado
def gerar_estado_aleatorio():
    valores = list(range(9))  # Cria uma lista com números de 0 a 8
    random.shuffle(valores)   # Embaralha os números aleatoriamente
    matriz = [valores[i:i + 3] for i in range(0, 9, 3)]  # Divide a lista em sublistas de 3 elementos
    return matriz

#verificar se há solução contando as inversões
def contar_inversoes(matriz):
    lista = [num for linha in matriz for num in linha]  # Converte a matriz em uma lista
    inversoes = 0
    for i in range(len(lista)):
        for j in range(i + 1, len(lista)):
            if lista[i] > lista[j] and lista[i] != 0 and lista[j] != 0:
                inversoes += 1
    return inversoes

#corrigir caso não haja solução realizando uma troca
def verificar_estado(matriz):
    if contar_inversoes(matriz) % 2 != 0:
        lista = [num for linha in matriz for num in linha] # Converte a matriz em uma lista
        i, j = random.sample(range(1, 9), 2)  # Escolhe duas peças aleatórias (ignorando o zero)
        lista[i], lista[j] = lista[j], lista[i]  # Troca as posições das duas peças
        matriz = [lista[k:k + 3] for k in range(0, 9, 3)] # Converte a lista de volta para uma matriz
    return matriz




teste = gerar_estado_aleatorio()
teste = verificar_estado(teste)
estado_inicial = Estado.Estado(teste)
print(estado_inicial)
print()
print(Estado.Estado.mostrar_resolucao(estado_inicial))






