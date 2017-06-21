#coding: utf-8

#IMPRIME NA FORMA MATRIZ
def imprimeMatriz(matrizA, matrizB):
	print '\nA x I = B\n'
	v = 0
	for linha in matrizA:
		print '|	',
		c = 0
		for l in linha:
			print str(l) + '	',
			c += 1
		print '| ',
		print '=', '|	', matrizB[v], '	|'
		v += 1

#OBTEM O SISTEMA DE TRABALHO
#Cada elemento da linha é divido pelo elemento diagonal da linha, ou seja, pelo elemento que que i = j da linha
#tornando os coeficientes da diagonal 1. Necessário para os calculos!
def obterSistemaTrabalho(matrizA, matrizB):
	for i in range(len(matrizA)):
		diagonal = matrizA[i][i]
		for j in range(len(matrizA[i])):
			matrizA[i][j] = matrizA[i][j] / diagonal
		matrizB[i] = matrizB[i] / diagonal

#TESTE PARA SABER SE A MATRIZ É CONVERGENTE(SASSENFELD)
#é definido uma lista 'beta' em que cada elemento equivale a operações com os elementos de cada linha
#o valor beta de cada linha é definido pela soma dos modulos dos elementos não diagonais da linha no qual
#se a cordenada j for maior que a cordenada i, soma-se apenas o modulo do elemento, caso contrário,
#o módulo do elemento é multiplicado pelo beta calculado na linha anterior
#Ao final do processo é verificado se algum dos betas calculados supera o valor de 1
#Caso negativo, a matriz é convergente!
def testeSassenfeld(matriz):
	beta = []
	calcBeta = 0
	for i in range(len(matriz)):
		for j in range(len(matriz)):
			if j > i:
				calcBeta += abs(matriz[i][j])
			elif j < i:
				calcBeta += abs(matriz[i][j]) * beta[i - 1]
			if j == (len(matriz[i]) - 1):
				beta.append(calcBeta)
				calcBeta = 0
	
	for b in range(len(beta)):
		if beta[b] > 1:
			return False
	
	return True

#COLETA NUMERO DE LINHAS
#Cada malha representa uma equação do sistema e o número de equações define a ordem da matriz dos coeficientes
numMalhas = int(raw_input('DIGITE O NÚMERO DE MALHAS DO CIRCUITO:\n'))

#INICIALIZAÇÃO DA MATRIZ E DO VETOR DE TERMOS INDEPENDENTES
matrizCoeficientes = []
vetorTermosIndependentes = []

#COLETA DE DADOS DO USUÁRIO
#O usuário ira digitar os coeficientes de cada equação do sistema, incluindo o termo independente
#Ex.: para a equação de um sistema qualquer 2x + 3y = 10, o usuário deve digitar '2 3 10'
print "\nDIGITE OS ELEMENTOS DA MATRIZ DE COEFICIENTES DO SISTEMA PARA O CIRCUITO:\n"

for i in range(numMalhas):
	entrada = map(float, raw_input('	LINHA ' + str(i + 1) + ': ').split(" "))
	matrizCoeficientes.append(entrada[:(len(entrada) - 1)])
	vetorTermosIndependentes.append(entrada[(len(entrada) - 1)])

#imprime a matriz para visualizar a matriz inserida
imprimeMatriz(matrizCoeficientes, vetorTermosIndependentes) 

#DIAGONALIZANDO A MATRIZ
#chama-se as funções que iram transformar a matriz em uma matriz de trabalho e logo em seguida
#é impressa a matriz para verificação do usuário
obterSistemaTrabalho(matrizCoeficientes, vetorTermosIndependentes)
imprimeMatriz(matrizCoeficientes, vetorTermosIndependentes) #teste

#VERIFICANDO CONVERGENCIA DA 
#O boleano testeConvergencia será aplicado como condição para a execução do método
#True -> o método de Gauss-Seidel é executado
#False -> significa que a matriz não é convergente e sendo assim não possui um resultado determinado
testeConvergencia = testeSassenfeld(matrizCoeficientes)
'''votar aqui!!!!'''

#ERRO RELATIVO
#É solicitado do usuário o quão preciso deve ser o resultado, definindo até que ponto ocorreram as interações
#do metodo númerico
if testeConvergencia:
	erro = int(raw_input("DIGITE O EXPOENTE DO ERRO RELATIVO DESEJÁDO:\n"))


def gaussSeidel(matrizA, matrizB, erro):
	vetorX = []
	for r in range(len(matrizA)):
		vetorX.append(0)
	
	
	
	for i in range(len(matrizA)):
		for j in range(len(matrizA):
			if i != j:
				vetorX[i] = 

