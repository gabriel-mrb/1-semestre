# Crie uma função que retorne a soma de todos os números pares da
# matriz.


import random

def nova_matriz(l,c):
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


def soma_pares_matriz(linhas,colunas):
    soma=0
    for i in range(linhas):
        for j in range(colunas):
            if matriz[i][j]%2==0:
                soma+=matriz[i][j]
    print(f'A SOMA DOS VALORES PARES DA MATRIZ É: {soma}')

matriz=[]
linhas=int(input('informe o numero de linhas desejadas: '))
colunas=int(input('Informe o numero de colunas desejadas: '))
matriz=nova_matriz(linhas,colunas)
imprimir_matriz(matriz)
soma_pares_matriz(linhas,colunas)
