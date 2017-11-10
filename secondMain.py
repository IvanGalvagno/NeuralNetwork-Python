import numpy as np

#Função de Sigmoid
def nonlin(x, deriv=False):
    if deriv==True:
        return x*(1-x)
    return 1/(1+np.exp(-x))

#Valores de ENTRADA
X = np.array([
    [0,0,1],
    [0,1,1],
    [1,0,1],
    [1,1,1]
])

#Valores de SAIDA
y = np.array([
    [0,1,1,0]
]).T

#SEED valores aleatorios para realizacao do calculo
np.random.seed(1)

#Inicializa Rnadomicamente os pesos
syn0 = 2*np.random.random((3,4)) -1
syn1 = 2*np.random.random((4,1)) -1

for j in range(60000):
    #Feed forward entre as Layers 0, 1 e 2
    l0 = X
    l1 = nonlin(np.dot(l0,syn0))
    l2 = nonlin(np.dot(l1,syn1))

    #Valor de Erro entre o valor gerado com o Erro
    l2_error = y - l2

    if j%10000 == 0:
        print ("Error" , str(np.mean(np.abs(l2_error))))
    
    #Qual a direcao correta / qual o valor da saida
    l2_delta = l2_error*nonlin(l2,deriv=True)

    #Valor de cada  l1 contribui para o erro da l2, baseado nos pesos
    l1_error = l2_delta.dot(syn1.T)

    #Difeca entre os valores ate l1
    l1_delta = l1_error * nonlin(l1,deriv=True)

    syn1 += l1.T.dot(l2_delta)
    syn0 += l0.T.dot(l1_delta)