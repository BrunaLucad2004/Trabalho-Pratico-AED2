class Heap:
    def __init__(self, chave, dado):
        self.chave = chave
        self.dado = dado

    def __repr__(self):
        return self.dado
    
    def __lt__(self, outro):
        if self.chave != outro.valor:
            return self.valor < outro.valor
        return self.dado < outro.dado
    
def min_heapify(vet,ind,tam):
	menor = ind
	f_esq = (2*ind) + 1
	f_dir = (2*ind) + 2
	
	if f_esq < tam and vet[f_esq] < vet[menor]:
		menor = f_esq
		
	if f_dir < tam and vet[f_dir] < vet[menor]:
		menor = f_dir
	
	if menor != ind:
		vet[menor], vet[ind] = vet[ind], vet[menor]
		min_heapify(vet, menor, tam)

def montar_heap_mini(vet, tam):
	ult = (tam // 2) - 1
	for i in range (ult, -1, -1):
		min_heapify(vet, i, tam)

def aumentar_chave_min(heap, pos, novo):
	heap[pos] = novo
	
	while pos > 0 and heap[((pos - 1) // 2)] > novo:
		heap[((pos - 1) // 2)], heap[pos] = heap[pos], heap[((pos - 1) // 2)]
		pos = ((pos - 1) // 2)

def inserir_chave_min(heap, tam, chave):
	heap.append(chave)
	aumentar_chave_min(heap, tam, chave)
	
def remover_chave_min(heap, tam, pos):
	heap[pos], heap[tam -1] = heap[tam -1], heap[pos]
	heap.pop(-1) 
	min_heapify(heap, pos, len(heap))