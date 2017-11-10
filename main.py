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
    [1,0,0],
    [1,1,1]
])

#Valores de SAIDA
y = np.array([
    [0,0,1,1]
]).T

#SEED valores aleatorios para realizacao do calculo
np.random.seed(1)

#Inicialização dos Pesos randomicamente
Syn0 = 2*np.random.random((3,1)) -1

for iter in range(1000):
    #Forward Propagation
    l0 = X   #Layer 0
    l1 = nonlin(np.dot(l0,Syn0)) #Hidden Layer

    #Erro
    l1_error = y - l1

    l1_delta = l1_error * nonlin(l1,True)

    #Atualizacao dos Pesos W
    Syn0 += np.dot(l0.T, l1_delta)

print('Saida após o treinamento: ')
print(l1)