import random #seed(),randint(),randrange(),shuffle(obj)

'''
Introdução:
- Implementar algoritmo de ordenação que receba uma colecão
- A coleção é uma lista de arestas
- Para comparar o peso as arestas entre dois item da coleção basta usar a chave 'weight' (peso)

Exemplos:
- Modo convencional
colecao[i] operador de comparacao colecao[j]
colecao[i] < colecao[j]

- Modo que você vai usar
int(colecao[i]['weight']) operador de comparacao int(colecao[j]['weight'])
int(colecao[i]['weight']) < int(colecao[j]['weight'])

É necessário converter o valor pra Interger no momento da comparação a fim de evitar erros
'''

# Sua classe algoritmo de ordenação precisa ter um método ordenar

'''
InsertSort para ordem crescente.
Args: colecao que será ordenado
Returns: O mesmo colecao, porém, ordenado

Execução: de forma iterativa, a partir do 2o elemento, até o último:
[ESTÁVEL] -- O(n^2)
	Sensível à entrada: Melhor desempenho em arquivos ordenados,
	e o pior quando está ordenado de forma reversa (no caso, decrescente).
	Eleger uma chave e movimentar todos os elementos maiores 
	que ela à direita. A chave, por ser menor que os outros, 
	deve anteceder todos os elementos deslocados.

'''
class InsertSort(object):
	def ordenar(self, colecao):
		for i in range(1,len(colecao)):
		#a partir da 2a posição, até o final da coleção
			chaveW = int(colecao[i]['weight'])
			chaveS, chaveT = int(colecao[i]['source']),int(colecao[i]['target'])
			#print(chaveW)
			j = i-1 #índice do antecessor da chaveW
			while j>=0 and chaveW<int(colecao[j]['weight']):
			#move todos as arestas maiores à direita
				colecao[j+1]['source'] = colecao[j]['source']
				colecao[j+1]['target'] = colecao[j]['target']
				colecao[j+1]['weight'] = colecao[j]['weight']
				j -= 1 #corrige o índice com decremento
			#inserir aresta antes dos elementos movidos
			colecao[j+1]['source'],colecao[j+1]['target'] = chaveS, chaveT
			colecao[j+1]['weight'] = chaveW
		return colecao

'''
SelectionSort para ordem crescente.
Args: altera o colecao que será ordenado
Returns: O mesmo colecao, porém, ordenado

Execução: de forma iterativa, encontrar o menor elemento.
[NÃO ESTÁVEL] -- O(n^2)
	Pouco sensível à entrada: mesmo no melhor caso, seu desempenho é quadrático.
	O menor elemento na 1a pos, 
	depois o menor elemento dos n-1 elementos restantes,
	depois o menor elemento dos n-2 restantes...

'''
class SelectionSort(object):
	def ordenar(self, colecao):
		# i e j são indices iteraveis
		for i in range(len(colecao)-1):
			menor = i # índice do menor elemento
			for j in range(i,len(colecao)):
				if int(colecao[j]['weight'])<int(colecao[menor]['weight']):
					menor = j # att índice do menor elemento
			# troca o menor elemento com o elemento da i-esima posição # SWAP
			colecao[menor],colecao[i] = colecao[i],colecao[menor]

		return colecao

'''
ShellSort para ordem crescente.
Args: altera o colecao que será ordenado
Returns: O mesmo colecao, porém, ordenado

Execução: 'InsertSort v2'para chaves distantes entre si.
[NÃO ESTÁVEL] -- O(?) 
	Realiza saltos de H posicoes, e é sensível à ordenação prévia.
	A execução de um código similar ao InsertSort acontece
	dentro do laço que controla os saltos realizados.
	Nesse novo loop, o salto sempre será atualizado, a qual,
	cada iteração (para cada salto) significa que ao eleger uma nova
	chave, movimentamos os elementos maioresà sua direita.

'''
class ShellSort(object):
	def ordenar(self,colecao):
		salto = len(colecao)//2 # Salto grande, que diminuirá a cada laço
		while salto>0:
		#'InsertSort' dos elementos sorteados pelo mesmo salto:
			for i in range(salto,len(colecao)):
			#'gap iteration' a partir de colecao[salto] até o final do colecao 
				chaveW = int(colecao[i]['weight'])
				chaveS, chaveT = int(colecao[i]['source']),int(colecao[i]['target'])
				j=i
				while j>=salto and chaveW<int(colecao[j-salto]['weight']):
					colecao[j] = colecao[j-salto]
					j -= salto # corrige o índice
				#inserir chave antes dos elementos movidos
				colecao[j]['weight'] = chaveW
				colecao[j]['source'] = chaveS
				colecao[j]['target'] = chaveT
			salto //= 2 # att salto

		return colecao

'''
QuickSort para ordem crescente.
Args: altera o colecao que será ordenado
Returns: O mesmo colecao, porém, ordenado

Execução: Divisão(Dividir para conquistar)
[NÃO ESTÁVEL] -- O(n log n) 
	Particionamento, excluindo o pivô um nível acima da pilha de execução;
	colecao e índices de início e fim de cada partição; retorna
	o índice do pivô na lista/colecao

'''
class QuickSort(object):
	def __init__(self,metodo=None):#Construtor não-padrão
		self.metodo = metodo
		return

	def ordenar(self,colecao,inicio,fim):
		# inicio e fim são índices da partição
		if inicio<fim:
			# PASSO BASE: método particiona
			if self.metodo=='first':
				index = particionaComeco(colecao,0,len(colecao)) # índice do pivô
			elif self.metodo=='last':
				index = particionaFim(colecao,int,0,len(colecao)) # índice do pivô
			elif self.metodo=='random':
				index = particionaAleatorio(colecao,0,len(colecao)) # índice do pivô
			elif self.metodo=='mediana':
				index = particiona(colecao,0,len(colecao)) # índice do pivô
			else: #metodo == None ou se não corresponder a um método de partição válido
				sys.exit('Método de particionamento inexistente.')

			# PASSO RECURSIVO
			self.ordenar(colecao,0,index-1,metodo) #elementos à esquerda do pivô
			self.ordenar(colecao,index+1,len(colecao),metodo) #elementos à direita do pivô
		
		return colecao

	'''
	Particionamento, excluindo o pivô um nível acima da pilha de execução
	Args: colecao e índices de início e fim de cada partição
	Returns: O índice do pivô na lista/colecao
	'''
	def particionaFim(colecao,inicio,fim):
		i = inicio-1 #index do menor elemento
		pivot = int(colecao[fim]['weight']) #pivô
		for j in range(inicio,fim):
			if int(colecao[j]['weight'])<=pivot:
				i += 1
				colecao[i],colecao[j] = colecao[j],colecao[i] #swap
		colecao[i+1],colecao[fim] = colecao[fim],colecao[i+1] #swap
		
		return i+1 #será índice do pivô na coleção
	
	def particionaComeco(colecao,inicio,fim):
		return 0

	def particionaAleatorio(colecao,inicio,fim):
		# Número aleatório DA PARTIÇÃO
		random.seed()
		i = random.randint(inicio,fim) #index do pivô (colecao[i])
		# trocar o pivô e o último elemento
		colecao[i],colecao[fim] = colecao[fim],colecao[i]#SWAP
		# executar outro método de partição
		return particionaFim(colecao,inicio,fim)
	
	def particiona(colecao,inicio,fim):
		return 0

'''
MergeSort para ordem crescente.
Args: altera o colecao que será ordenado
Returns: O mesmo colecao, porém, ordenado

Execução: Divisão(Dividir para conquistar) e Combinação(MERGE)
[ESTÁVEL] -- O(n log n) 
 	Usa bastante memória na pilha de execução. São 2 tarefas: 
	1. SPLIT - Dividir o colecao em esquerda e direita, 
	para ordenar recursivamente cada sublista. 
	2.1. Ordenar previamente as sublistas, indicando o menor de
	cada um. Adicionamos, um a um, os menores no colecao.
	2.2 A subtarefa anterior acaba quando qualquer sublista não tem elementos.
	O restante da outra sublista será copiada necessariamente naquela ordem.

'''
class MergeSort(object):
	def ordenar(self,colecao):
		if len(colecao)>1: # Não particionar, se houver apenas 1 elemento
			#1.Split: O vetor se dividirá em duas partes
			meio = len(colecao)//2 #índice da metade da colecao
			left = colecao[:meio]# colecao[0:meio-1]
			right = colecao[meio:]# colecao[meio:len(colecao)]

			#Passos de recursão do algoritmo para ambas as partes
			self.ordenar(left)
			self.ordenar(right)
			
			#2.Passo Base: 
			
			#2.1.Sobrescrever colecao, de left e de right
			i = j = k = 0 # Índices respectivos a colecao, left e right
			while j<len(left) and k<len(right):
				#Encontrar o menor elemento de cada sublista de colecao
				if int(left[j]['weight'])<=int(right[k]['weight']):
				#left[j] será add a colecao antes (ordem crescente)
					colecao[i] = colecao[j]
					j += 1 # iterar em left
				else: 
				#right[k] será add a colecao antes
					colecao[i] = right[k]
					k += 1 #iterar em right
				i += 1 #Por fim, att a posicao de colecao para inserir o menor
			
			#2.2Add elementos restantes das sublistas, se houver
			while j<len(left):
				colecao[i] = left[j]
				#att índices
				i += 1
				j += 1
				
			while k<len(right):
				colecao[i] = right[k]
				#att índices
				i += 1
				k += 1
		
		return colecao

'''
HeapSort para ordem crescente.
Args: altera o colecao que será ordenado
Returns: O mesmo colecao, porém, ordenado

Execução: 'SelectionSort', mas para o maior elemento. 
É apresentado como Heap (BinTree)
[NÃO ESTÁVEL] -- O(n log n) 
	
'''
class HeapSort(object):
	def ordenar(self,colecao):
		tam = len(colecao) #tamanho do vetor
		# Construir MaxHeap
		for index in range(tam,-1,-1):
			maxHeapify(self,colecao,tam,index)

		# Extrair os elementos na ordem correta
		for index in range(tam-1,0,-1):
			#print(colecao)
			colecao[index],colecao[0] = colecao[0],colecao[index]#SWAP
			maxHeapify(self,colecao,index,0)
		
		return colecao

	'''
	Construir Heap
	Args: vetor/sublista o tamanho do Heap, e o índice da raíz do heap 
	Returns: implicitamente, a mesma coleção organizada em Heap
	'''
	def maxHeapify(self,colecao,tam,index):
		maior = index # índice da "raiz" do heap,
		left, right = 2*index + 1, 2*index + 2 # índices dos filhos

		# Checa se o filho esquerdo da raíz existe e é maior que o pai
		if left < tam and int(colecao[index]['weight']) < int(colecao[left]['weight']):
			maior = left
		# Checa se o filho direito da raíz existe e é maior que o pai
		if right < tam and int(colecao[maior]['weight']) < int(colecao[right]['weight']):
			maior = right

		# Construir/Manter o Heap, trocando a raíz quando necessário
		if maior != index: # SWAP
			colecao[index], colecao[maior] = colecao[maior], colecao[index]
			# heapify da raíz
			maxHeapify(self,colecao,tam,maior)

		return colecao

'''
CountingSort para ordem crescente.
Args: o colecao que será B
Returns: outro colecao, B

Execução: ???????????????????
[ESTÁVEL] -- O(n) 
	
'''
class CountingSort(object):
	def ordenar(self,colecao):
		return colecao

