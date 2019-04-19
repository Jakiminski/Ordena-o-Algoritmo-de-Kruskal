import sys		#argv, executable and exit([int or obj])
from grafo import Grafo
from algoritmos import *
from utils import *

if __name__ == '__main__':

	for arg in sys.argv[1:]: 
		print('arg: {}'.format(arg))

	if (len(sys.argv) == 3) or (len(sys.argv)==4):
		
		arquivoEntrada = sys.argv[1]
		# Exemplo:'input/7vertices.json'
		arquivoSaida = 'output/VerticesDaMST.txt'
		
		#print('Arquivo de entrada: {}'.format(arquivoEntrada))
		#print('arquivo de saída: {}'.format(arquivoSaida))
		#print(sys.argv[2].lower()=='insertsort')
		
		if sys.argv[2].lower() == 'insertsort':
			algoritmoDeOrdenacao = InsertSort()
			grafo = Grafo()
			grafo.estabelecerAlgoritmoDeOrdenacao(algoritmoDeOrdenacao)
			grafo.carregarGrafo(arquivoEntrada)

			arvoreGeradoraMinima =  grafo.executarKruskal() 
			SalvarArvoreGeradoraMinimaEmArquivo(arquivoSaida, arvoreGeradoraMinima)

		elif sys.argv[2].lower() == 'selectionsort':
			algoritmoDeOrdenacao = SelectionSort()
			grafo = Grafo()
			grafo.estabelecerAlgoritmoDeOrdenacao(algoritmoDeOrdenacao)
			grafo.carregarGrafo(arquivoEntrada)

			arvoreGeradoraMinima =  grafo.executarKruskal() 
			SalvarArvoreGeradoraMinimaEmArquivo(arquivoSaida, arvoreGeradoraMinima)

		elif sys.argv[2].lower() == 'shellsort':
			algoritmoDeOrdenacao = ShellSort()
			grafo = Grafo()
			grafo.estabelecerAlgoritmoDeOrdenacao(algoritmoDeOrdenacao)
			grafo.carregarGrafo(arquivoEntrada)

			arvoreGeradoraMinima =  grafo.executarKruskal() 
			SalvarArvoreGeradoraMinimaEmArquivo(arquivoSaida, arvoreGeradoraMinima)

		elif sys.argv[2].lower() == 'quicksort':
			if len(sys.argv)==4:
				# QuickSort(metodo)
				algoritmoDeOrdenacao = QuickSort(sys.argv[3])
			
				grafo = Grafo()
				grafo.estabelecerAlgoritmoDeOrdenacao(algoritmoDeOrdenacao)
				grafo.carregarGrafo(arquivoEntrada)

				arvoreGeradoraMinima =  grafo.executarKruskal() 
				SalvarArvoreGeradoraMinimaEmArquivo(arquivoSaida, arvoreGeradoraMinima)
			else:
				print('Se pretende usar o QuickSort, tipos de particionamento: \'first\', \'last\', \'random\' e \'mediana\'')
				print('Formato (QuickSort): <Input File> \'InsertSort\' <particionamento Quick>')
				sys.exit('ERRO: Método de particionamento \'{}\'desconhecido.'.format(sys.argv[3]))

		elif sys.argv[2].lower() == 'mergesort':
			algoritmoDeOrdenacao = MergeSort()
			grafo = Grafo()
			grafo.estabelecerAlgoritmoDeOrdenacao(algoritmoDeOrdenacao)
			grafo.carregarGrafo(arquivoEntrada)
			arvoreGeradoraMinima =  grafo.executarKruskal() 
			SalvarArvoreGeradoraMinimaEmArquivo(arquivoSaida, arvoreGeradoraMinima)

		elif sys.argv[2].lower() == 'heapsort':
			algoritmoDeOrdenacao = HeapSort()
			grafo = Grafo()
			grafo.estabelecerAlgoritmoDeOrdenacao(algoritmoDeOrdenacao)
			grafo.carregarGrafo(arquivoEntrada)

			arvoreGeradoraMinima =  grafo.executarKruskal() 
			SalvarArvoreGeradoraMinimaEmArquivo(arquivoSaida, arvoreGeradoraMinima)


		elif sys.argv[2].lower() == 'countingsort':
			algoritmoDeOrdenacao = CountingSort()
			grafo = Grafo()
			grafo.estabelecerAlgoritmoDeOrdenacao(algoritmoDeOrdenacao)
			grafo.carregarGrafo(arquivoEntrada)

			arvoreGeradoraMinima =  grafo.executarKruskal() 
			SalvarArvoreGeradoraMinimaEmArquivo(arquivoSaida, arvoreGeradoraMinima)
			
		else:
			#Printar erro e fechar programa
			print('ERRO: Método de ordenação \'{}\'desconhecido.'.format(sys.argv[2]))
			sys.exit('Métodos de ordenação registrados: InsertSort, SelectionSort, ShellSort, QuickSort, MergeSort, HeapSort e CountingSort.')
			
		print('Arquivo de saída \'{}\' gerado com sucesso.'.format(arquivoSaida))
	else:
		print('Insira os parâmetros corretamente. Formato: <Input File> <Ordenar> <Adicional Ordenação>')
		print('EXEMPLOS: \'input/7vertices.json InsertSort\' OU \'input/100vertices.json quicksort random\'')
		print('Se pretende usar o QuickSort, tipos de particionamento: \'first\', \'last\', \'random\' e \'mediana\'')
		print('Formato (QuickSort): <Input File> \'QuickSort\' <particionamento Quick>')
	sys.exit(0)