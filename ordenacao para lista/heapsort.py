'''
HeapSort para ordem crescente.
Args: altera o vetor que será ordenado
Returns: O mesmo vetor, porém, ordenado

Execução: "SelectionSort", mas para o maior elemento. 
É apresentado como Heap (BinTree)
[NÃO ESTÁVEL] -- O(n log n) 
	
'''
def heapSort(vet):
	tam = len(vet) #tamanho do vetor
	# Construir MaxHeap
	for index in range(tam,-1,-1):
		maxHeapify(vet,tam,index)
	# Extrair os elementos na ordem correta
	for index in range(tam-1,0,-1):
		#print(vet)
		vet[index],vet[0] = vet[0],vet[index]#SWAP
		maxHeapify(vet,index,0)
	pass
'''
Construir Heap
Args: vetor/sublista o tamanho do Heap, e o índice da raíz do heap 
Returns: implicitamente, o mesmo vetor organizado em Heap
'''
def maxHeapify(vet,tam,index):
	maior = index # índice da "raiz" do heap,
	left, right = 2*index + 1, 2*index + 2 # índices dos filhos

	# Checa se o filho esquerdo da raíz existe e é maior que o pai
	if left < tam and vet[index] < vet[left]:
		maior = left
	# Checa se o filho direito da raíz existe e é maior que o pai
	if right < tam and vet[maior] < vet[right]:
		maior = right

	# Construir/Manter o Heap, trocando a raíz quando necessário
	if maior != index: # SWAP
		vet[index], vet[maior] = vet[maior], vet[index]
		# heapify da raíz
		maxHeapify(vet,tam,maior)

	return vet


vetor = [5,4,3,2,6,1]# lista indexada
print('Antes: ')
print(vetor)
print('Aplicando o HeapSort.')
vetor = heapSort(vetor)
print('Após: ')
print(vetor)
