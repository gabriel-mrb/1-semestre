# Crie uma função que faça o print de qualquer matriz passada. Use essa
# função para imprimir a matriz criada no item 1


import random

def nova_matriz(linhas,colunas):
    for i in range(linhas):
        i=[]
        matriz.append(i)

    for i in range(linhas):
        for j in range(colunas):
            # value = input('Informe um valor: ')
            matriz[i].append(random.randint(0,21))
    return matriz  

    
def imprimir_matriz(matriz):
    print('\n\nSua Matriz:\n')
    for i in range(linhas):
        print(matriz[i])


matriz=[]
linhas=int(input('informe o numero de linhas desejadas: '))
colunas=int(input('Informe o numero de colunas desejadas: '))
matriz=nova_matriz(linhas,colunas)
imprimir_matriz(matriz)
