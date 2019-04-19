'''
InsertSort para ordem crescente.
Args: vetor que será ordenado
Returns: O mesmo vetor, porém, ordenado

Execução: de forma iterativa, a partir do 2o elemento, até o último:
[ESTÁVEL] -- O(n^2)
	Sensível à entrada: Melhor desempenho em arquivos ordenados,
	e o pior quando está ordenado de forma reversa (no caso, decrescente).
	Eleger uma chave e movimentar todos os elementos maiores 
	que ela à direita. A chave, por ser menor que os outros, 
	deve anteceder todos os elementos deslocados.

'''
def insertSort(vet):
	for i in range(1,len(vet)): 
	#a partir da 2a posição, vet[1]  até o final do vetor
		chave = vet[i]
		print(chave)
		j = i-1 #índice do antecessor da chave
		while j>=0 and chave<vet[j]:
		#move todos os maiores à direita
			vet[j+1] = vet[j]
			j -= 1 #corrige o índice com decremento
		#inserir chave antes dos elementos movidos
		vet[j+1] = chave
	return vet


vetor = [5,4,3,2,6,1]# lista indexada

print('Antes da Ordenação: ')
print(vetor)
print('Aplicando o InsertSort: ')
vetor = insertSort(vetor)
print('Após: ')
print(vetor)