'''
MergeSort para ordem crescente.
Args: altera o vetor que será ordenado
Returns: O mesmo vetor, porém, ordenado

Execução: Divisão(Dividir para conquistar) e Combinação(MERGE)
[ESTÁVEL] -- O(n log n) 
 	Usa bastante memória na pilha de execução. São 2 tarefas: 
	1. SPLIT - Dividir o vetor em esquerda e direita, 
	para ordenar recursivamente cada sublista. 
	2.1. Ordenar previamente as sublistas, indicando o menor de
	cada um. Adicionamos, um a um, os menores no vetor.
	2.2 A subtarefa anterior acaba quando qualquer sublista não tem elementos.
	O restante da outra sublista será copiada necessariamente naquela ordem.

'''
def mergeSort(vet):
	if len(vet)>1: # Não particionar, se houver apenas 1 elemento
		#1.Split: O vetor se dividirá em duas partes
		meio = len(vet)//2 #índice da metade do vetor
		left = vet[:meio]# vet[0:meio-1]
		right = vet[meio:]# vet[meio:len(vet)]

		#Passos de recursão do algoritmo para ambas as partes
		mergeSort(left)
		mergeSort(right)

		#2.Passo Base: 
		
		#2.1.Sobrescrever vet, de left e de right
		i = j = k = 0 # Índices respectivos a vet, left e right
		while j<len(left) and k<len(right):
			#Encontrar o menor elemento de cada sublista de vet
			if left[j]<right[k]:
			#left[j] será add a vet antes (ordem crescente)
				vet[i] = left[j]
				j += 1 # iterar em left
			else: 
			#right[k] será add a vet antes
				vet[i] = right[k]  
				k += 1 #iterar em right
			i += 1 #Por fim, att a posicao de vet para inserir o menor
		print(left)
		print(right)
		#2.2Add elementos restantes das sublistas, se houver
		while j<len(left):
			vet[i] = left[j]
			#att índices
			i += 1
			j += 1
			
		while k<len(right):
			vet[i] = right[k]
			#att índices
			i += 1
			k += 1
	return vet

vetor = [5,4,3,2,6,1]# lista indexada

print('Antes: ')
print(vetor)
print('Aplicando o MergeSort.')
vetor = mergeSort(vetor)
print('Após: ')
print(vetor)