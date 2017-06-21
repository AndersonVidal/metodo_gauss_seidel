#coding: utf-8

#IMPRIME NA FORMA MATRIZ
def imprimeMatriz(matrizA, matrizB):
	print ''
	v = 0
	for linha in matrizA:
		print '|',
		c = 0
		for l in linha:
			print '(' + str(l)+ ')' + 'i'+ str(c),
			c += 1
		print '|',
		print '=', '|', matrizB[v], '|'
		v += 1

def obterSistemaTrabalho(matrizA, matrizB):
	for i in range(len(matrizA)):
		diagonal = matrizA[i][i]
		for j in range(len(matrizA[i])):
			matrizA[i][j] = matrizA[i][j] / diagonal
		matrizB[i] = matrizB[i] / diagonal

def testeSassenfeld(matriz, vetorTermosIndependentes):
	maior = 0
	element = 1
	soma = 0

	#percorre a matriz
	for i in range(len(matriz)):
		for j in range(len(matriz)):
			soma += matriz[i][j]*element
			print "soma", soma-1
		if(maior != 0):
			element = maior

		if(soma > maior):
			maior = soma
		soma = 0
		print "maior ", maior

#COLETA NUMERO DE LINHAS
numMalhas = int(raw_input('Digite o número de malhas do circuito:\n'))

#INICIALIZAÇÃO DA MATRIZ E DO VETOR DE TERMOS INDEPENDENTES
matrizCoeficientes = []
vetorTermosIndependentes = []

print "\nDigite os coeficientes do sistema, seguindo a ordem",
print "das variáveis! (Ex.: i1, i2, i3,..., b1)\n"

#COLETA DE DADOS DO USUÁRIO
for i in range(numMalhas):
	entrada = map(float, raw_input(' linha ' + str(i + 1) + ':').split(" "))
	matrizCoeficientes.append(entrada[:(len(entrada) - 1)])
	vetorTermosIndependentes.append(entrada[(len(entrada) - 1)])

imprimeMatriz(matrizCoeficientes, vetorTermosIndependentes) # teste

#VERIFICANDO CRITERIOS DE CONVERGÊNCIA

obterSistemaTrabalho(matrizCoeficientes, vetorTermosIndependentes)
imprimeMatriz(matrizCoeficientes, vetorTermosIndependentes) #teste
testeSassenfeld(matrizCoeficientes, vetorTermosIndependentes)

#Critério matriz diagonal dominante
