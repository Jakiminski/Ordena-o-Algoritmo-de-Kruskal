'''
CountingSort para ordem crescente.
Args: o vetor que será B
Returns: outro vetor, B

Execução: ???????????????????
[ESTÁVEL] -- O(n) 
	
'''
def countingSort(vet):
	maior = maiorElem(vet)
	n = len(vet)
	# Cria vetores temporários
	B = [0 for i in range(n)] #Vetor vazio de cópia; ou = [0] * len(vet); intervalo [0,n-1]
	C = [0] * (maior+1) #Encontrar o maior elemento de vet; intervalo [0,maior]
	print("C {}".format(C))
	# C[i] contabilizará a qnt de elementos >= a i 
	for i in range(n):# [0,n-1]
		C[vet[i]] += 1
	for j in range(1,len(C)): # intervalo indice[1,len-1], indice[0,len-2]
		C[j] += C[j-1] # Soma com os anteriores
	#Determinar a posição de cada elemento no vetor copia
	j = n-1
	while j>=0: #Maior para o menor índice
		print('vet[{}]:{}'.format(j, vet[j]))
		print('C[{}]:{}'.format(vet[j],C[vet[j]]))
		print('B[{}]:{}'.format(C[vet[j]],B[C[vet[j]]]))
		B[C[vet[j-1]+1]] = vet[j-1]
		C[vet[j-1]+1] -= 1
		j -= 1
	return B


def maiorElem(vet): #encontra o maior elemento de um vetor
	maior = vet[0]
	if len(vet)>1: 
		for i in range(1,len(vet)):
			if maior < vet[i]: maior = vet[i]
	return maior

vetor = [5,4,3,2,1,2,8,8,3] #lista indexada

print('Antes: ')
print(vetor)
print('Aplicando o CountingSort.')
vetor = countingSort(vetor)
print('Após: ')
print(vetor)