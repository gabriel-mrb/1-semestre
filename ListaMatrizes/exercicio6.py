# Gerar e imprimir uma matriz de tamanho 10 x 10, onde seus elementos
# sao da forma:
# A[i][j] = (2*i) + (7*j) 2 se i < j;
# A[i][j] = (3*i^2) 1 se i = j ;
# A[i][j] = (4*i^3) (5*j^2) + 1 se i > j.


def gerar_matriz(matriz):

    for i in range(10):
        for j in range(10):
            if i<j:
                matriz[i].append(2*i + 7*j)                    
            elif i==j:                              
                matriz[i].append(3*i**2)
            else:
                matriz[i].append(4*i**3 * 5*j**2 + 1)
    return matriz


def imprimir_matriz(matriz):
    print('\n\nSua Matriz:\n')
    for i in range(10):
        print(matriz[i])

matriz=[]
for i in range(10):
        i=[]
        matriz.append(i)

        
matriz = gerar_matriz(matriz)
imprimir_matriz(matriz)


