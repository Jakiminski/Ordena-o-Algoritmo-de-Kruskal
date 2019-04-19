'''
ShellSort para ordem crescente.
Args: altera o vetor que será ordenado
Returns: O mesmo vetor, porém, ordenado

Execução: "InsertSort v2"para chaves distantes entre si.
[NÃO ESTÁVEL] -- O(?) 
	Realiza saltos de H posicoes, e é sensível à ordenação prévia.
	A execução de um código similar ao InsertSort acontece
	dentro do laço que controla os saltos realizados.
	Nesse novo loop, o salto sempre será atualizado, a qual,
	cada iteração (para cada salto) significa que ao eleger uma nova
	chave, movimentamos os elementos maioresà sua direita.

'''
def shellSort(vet):
	salto = len(vet)//2 # Salto grande, que diminuirá a cada laço
	while salto>0:
	#"InsertSort" dos elementos sorteados pelo mesmo salto:
	 	for i in range(salto,len(vet)):
 		#"gap iteration" a partir de vet[salto] até o final do vetor 
	 		chave = vet[i] 
	 		j=i
	 		while j>=salto and chave<vet[j-salto]:
	 			vet[j] = vet[j-salto]
	 			j -= salto # corrige o índice
	 		#inserir chave antes dos elementos movidos
	 		vet[j] = chave
 		salto //= 2 # att salto
	return vet

vetor = [5,4,3,2,6,1]# lista indexada

print('Antes da Ordenação: ')
print(vetor)
print('Aplicando o ShellSort: ')
vetor = shellSort(vetor)
print('Após: ')
print(vetor)