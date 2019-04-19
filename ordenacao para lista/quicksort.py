import sys #argv, executable and exit([int or obj])
import random #seed(),randint(),randrange(),shuffle(obj)

'''
QuickSort para ordem crescente.
Args: altera o vetor que será ordenado
Returns: O mesmo vetor, porém, ordenado

Execução: Divisão(Dividir para conquistar)
[NÃO ESTÁVEL] -- O(n log n) 
	

'''
def quickSort(vet,inicio=int(0),fim=len(vet),arg = "last"):
	# inicio e fim são índices da partição
	if inicio<fim:
		# PASSO BASE: método particiona
		if arg=="first":
			index = particionaComeco(vet,inicio,fim) # índice do pivô
		elif arg=="last":
			index = particionaFim(vet,inicio,fim) # índice do pivô
		elif arg=="random":
			index = particionaAleatorio(vet,inicio,fim) # índice do pivô
		elif arg=="mediana":
			index = particiona(vet,inicio,fim) # índice do pivô
		else: 
			sys.exit("Método de particionamento inexistente.")
			pass

		# PASSO RECURSIVO
		quickSort(vet,inicio,index-1,arg) #elementos à esquerda do pivô
		quickSort(vet,index+1,fim,arg) #elementos à direita do pivô
	return vet

'''
Particionamento, excluindo o pivô um nível acima da pilha de execução
Args: vetor e índices de início e fim de cada partição
Returns: O índice do pivô na lista/vetor
'''
def particionaFim(vet,inicio,fim):
	i = inicio-1 #index do menor elemento
	pivot = vet[fim] #pivô
	for j in range(inicio,fim):
		if vet[j]<=pivot:
			i += 1
			vet[i],vet[j] = vet[j],vet[i] #swap
	vet[i+1],vet[fim] = vet[fim],vet[i+1] #swap
	return i+1 #será índice do pivô no vetor

def particionaComeco(vet,inicio,fim):
	return 0

def particionaAleatorio(vet,inicio,fim):
	# Número aleatório DA PARTIÇÃO
	random.seed()
	i = random.randint(inicio,fim) #index do pivô (vet[i])
	# trocar o pivô e o último elemento
	vet[i],vet[fim] = vet[fim],vet[i]
	# executar outro método de partição
	return particionaFim(vet,inicio,fim)

def particiona(vet,inicio,fim):
	return 0


vetor = [5,4,3,2,6,1]# lista indexada

print('Antes: ')
print(vetor)
print('Aplicando o QuickSort.')
vetor = quickSort(vetor,0,len(vetor)-1,"random") #arg está implícito
print('Após: ')
print(vetor)
