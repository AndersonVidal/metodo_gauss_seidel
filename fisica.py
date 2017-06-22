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

#METODO GAUSS-SEIDEL
#realiza apenas uma interação. Deve ser chamado consecutivamente para realizar
#varias interacoes. ALtera o vetorCorrente!
def gaussSeidel(matrizA, matrizB, vetorX):
	calc = 0
	vetor = vetorX[:]
	#interacao
	for i in range(len(matrizA)):
		calc += matrizB[i]
		for j in range(len(matrizA)):
			if i != j:
				calc += matrizA[i][j] * vetor[j] * (-1)
		vetor[i] = calc
		calc = 0
		
	return vetor

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

#ERRO RELATIVO e APLICAÇÃO DO MÉTODO DE GAUSS-SEIDEL
#é coletado o expoente do erro desejado pelo 

vetorCorrente = []
interacoes = []
subtracao = 0
for r in range(len(matrizCoeficientes)):
		vetorCorrente.append(0)

if testeConvergencia:
	print "DIGITE O MÓDULO DO EXPOENTE DO ERRO RELATIVO DESEJÁDO:"
	print "(Digite um número menor que 0 se deseja um resultado rápido.)"
	print "(Digite 0 para obter o resultado mais preciso possivel!)"
	erro = int(raw_input())
	if erro > 0: erro = pow(10, -erro)
	erroRelativo = 1
	
	subtracao = 0
	while erroRelativo > erro:
		vetorCorrente = gaussSeidel(matrizCoeficientes, vetorTermosIndependentes, vetorCorrente)
		interacoes.append(vetorCorrente[:])
		
		if erro < 0:
			break
		elif erro == 1:
			if interacoes[len(interacoes) -1] == interacoes[len(interacoes) - 2]: break
		elif len(interacoes) > 1:
			for s in range(numMalhas):
				if (interacoes[len(interacoes) - 1][s] - interacoes[len(interacoes) - 2][s]) > subtracao:
					subtracao = interacoes[len(interacoes) - 1][s] - interacoes[len(interacoes) - 2][s]
			erroRelativo = abs(subtracao) / max(interacoes[len(interacoes) -1])
			subtracao = 0
			if interacoes[len(interacoes) -1] == interacoes[len(interacoes) - 2]: break
	
	print "\n\n-----------RESULTADO-----------\n"
	a = 1
	for i in range(len(vetorCorrente)):
		print "i" + str(a)+ " =", vetorCorrente[i], ' A'
		a += 1 
	print "\nNúmero de interações:", len(interacoes)
	a = 0
	for i in interacoes:
		print 'I(' + str(a) + ') =' , i
		a += 1

else:
	print "Matriz não é convergente! Verifique se o sistema de equações esta com os valores corretos!"

