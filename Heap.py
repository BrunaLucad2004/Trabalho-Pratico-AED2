def min_heapify(heap,indice,tamanho):
	menor = indice
	f_esq = (2*indice) + 1
	f_dir = (2*indice) + 2
	
	if f_esq < tamanho and heap[f_esq] < heap[menor]:
		menor = f_esq
		
	if f_dir < tamanho and heap[f_dir] < heap[menor]:
		menor = f_dir
	
	if menor != indice:
		heap[menor], heap[indice] = heap[indice], heap[menor]
		min_heapify(heap, menor, tamanho)

def montar_heap(heap, tamanho):
	ult = (tamanho // 2) - 1
	for i in range (ult, -1, -1):
		min_heapify(heap, i, tamanho)

def aumentar_chave(heap, pos, novo):
	heap[pos] = novo
	
	while pos > 0 and heap[((pos - 1) // 2)] > novo:
		heap[((pos - 1) // 2)], heap[pos] = heap[pos], heap[((pos - 1) // 2)]
		pos = ((pos - 1) // 2)

def heappush(heap, tamanho, chave):
	heap.append(chave)
	aumentar_chave(heap, tamanho, chave)
	
def heappop(heap):
	elemento = heap.pop(0) 
	montar_heap(heap, len(heap))
	return elemento

