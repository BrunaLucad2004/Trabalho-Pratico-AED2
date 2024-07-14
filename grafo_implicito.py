
#movimento para esquerda
#movimento para direita
#movimento para cima
#movimento para baixo

#verificar se há solução

#corrigir caso não haja solução

#verificar quais os movimentos possiveis

#verificar heuristica

def BuscaA(inicial):
	agenda = []
	estados_passados = set()
	estado = inicial
	agenda.append(estado)
	estados_passados.add(estado)
	while len(agenda) > 0:
		estado = agenda.pop(0)
		if estado == inicial:
			return estado
		for transicao in estado.transicoes():
			prox = transicao
			if not (transicao in estados_passados):
				agenda.append(prox)
				estados_passados.add(prox)
	return None
				




