#   Crie uma função que retorne uma matriz de dimensões MxN (valores de
#   entrada – passados pelo usuário) com valores aleatórios entre 1 e 20.


import random

def nova_matriz(l,c):
    for i in range(linhas):
        i=[]
        matriz.append(i)

    for i in range(linhas):
        for j in range(colunas):
            # value = input('Informe um valor: ')
            matriz[i].append(random.randint(0,21))  

    print('\n\nSua Matriz:\n')
    for i in range(linhas):
        print(matriz[i])


matriz=[]
linhas=int(input('informe o numero de linhas desejadas: '))
colunas=int(input('Informe o numero de colunas desejadas: '))
nova_matriz(linhas,colunas)
