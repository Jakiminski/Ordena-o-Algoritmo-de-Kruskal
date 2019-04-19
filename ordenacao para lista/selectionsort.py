'''
SelectionSort para ordem crescente.
Args: altera o vetor que será ordenado
Returns: O mesmo vetor, porém, ordenado

Execução: de forma iterativa, encontrar o menor elemento.
[NÃO ESTÁVEL] -- O(n^2)
	Pouco sensível à entrada: mesmo no melhor caso, seu desempenho é quadrático.
	O menor elemento na 1a pos, 
	depois o menor elemento dos n-1 elementos restantes,
	depois o menor elemento dos n-2 restantes...

'''
def selectionSort(vet):
	# i e j são indices iteraveis
	for i in range(len(vet)-1):
		menor = i # índice do menor elemento
		for j in range(i,len(vet)):
			if vet[j]<vet[menor]:
				menor = j # att índice do menor elemento
		# troca o menor elemento com o elemento da i-esima posição
		vet[menor],vet[i] = vet[i],vet[menor]
	return vet


vetor = [5,4,3,2,6,1]# lista indexada

print('Antes da Ordenação: ')
print(vetor)
print('Aplicando o SelectionSort: ')
vetor = selectionSort(vetor)
print('Após: ')
print(vetor)