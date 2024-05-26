# Crie uma função que retorne o maior valor de uma linha escolhida pelo
# usuário (parâmetro). Lembre-se de fazer a validação se a coluna
# escolhida existe


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


def maior_valor_linha(linha_maior_valor,linhas,colunas):
    valor_maior=0
    for i in range(colunas):
        if matriz[linha_maior_valor][i]>=valor_maior:
                valor_maior=matriz[linha_maior_valor][i]
    print(f'O maior valor na linha {linha_maior_valor+1} é: {valor_maior}')

matriz=[]
linhas=int(input('informe o numero de linhas desejadas: '))
colunas=int(input('Informe o numero de colunas desejadas: '))
matriz=nova_matriz(linhas,colunas)
imprimir_matriz(matriz)

while True:
    linha_maior_valor = int(input(f'Informe uma linha entre 1 - {linhas}: '))
    if 0>=linha_maior_valor or linha_maior_valor>linhas:
        print('Valor invalido!')
        continue
    else:
        linha_maior_valor-=1
        break
maior_valor_linha(linha_maior_valor , linhas , colunas)