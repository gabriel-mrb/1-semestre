# Crie uma função que retorne a soma de uma coluna escolhida pelo
# usuário (a coluna escolhida deve ser passada por parâmetro). Lembre-se de fazer a validação se a coluna escolhida existe.


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


def soma_coluna_matriz(num_coluna,linhas):
    soma_coluna=0
    for i in range(linhas):
        soma_coluna+=matriz[i][num_coluna-1]
    print(f'A SOMA DOS VALORES NA COLUNA {num_coluna-1} DA MATRIZ É: {soma_coluna}')

matriz=[]
linhas=int(input('informe o numero de linhas desejadas: '))
colunas=int(input('Informe o numero de colunas desejadas: '))
matriz=nova_matriz(linhas,colunas)
imprimir_matriz(matriz)

while True:
    soma_col = int(input(f'Para realizar a soma de uma coluna, informe um valor entre 1 - {colunas}: '))
    if soma_col<1 or soma_col>colunas:
        print('Valor Invalido!')
        continue
    else:
        soma_coluna_matriz(soma_col,linhas)
        break
