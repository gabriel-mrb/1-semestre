# Desafio (extra): implemente um jogo da velha em python

l1=[' ',' ',' ']
l2=[' ',' ',' ']
l3=[' ',' ',' ']
matriz=[l1,l2,l3]


def jogador_1(matriz):
    while True:
        linha=int(input('JOGADOR 1 - Escolha uma linha (1-3): '))
        coluna=int(input('JOGADOR 1 - Escolha uma coluna (1-3): '))
        if matriz[linha-1][coluna-1]=='X' or matriz[linha-1][coluna-1]=='O':
            print('Opcao invalida!') 
            continue
        else:
            matriz[linha-1][coluna-1]='X'
            break
    return matriz

def jogador_2(matriz):
    while True:
        linha=int(input('JOGADOR 2 - Escolha uma linha (1-3): '))
        coluna=int(input('JOGADOR 2 - Escolha uma coluna (1-3): '))
        if matriz[linha-1][coluna-1]=='X' or matriz[linha-1][coluna-1]=='O':
                print('Opcao invalida!') 
                continue
        else:
            matriz[linha-1][coluna-1]='O'
            break
    return matriz

def vitoria(matriz):
    for i in range(3):
        if matriz[i][0]==matriz[i][1]==matriz[i][2] !=' ':
            return True
        elif matriz[0][i]==matriz[1][i]==matriz[2][i] !=' ':
            return True
    if matriz[0][0] == matriz[1][1] == matriz[2][2] != ' ':
        return True
    elif matriz[0][2] == matriz[1][1] == matriz[2][0] != ' ':
        return True
    return False

def empate(matriz):
    for i in range(3):
        if ' ' in matriz[i]:
            return False
        else:
            return True
            

while True:
    for i in range(3):
        print(f' {matriz[i][0]} | {matriz[i][1]} | {matriz[i][2]} ')
        if i==0 or i==1:
            print('-'*11)
    jogador_1(matriz)
    if vitoria(matriz):
        print('JOGADOR 1 VENCEU')
        for i in range(3):
            print(f' {matriz[i][0]} | {matriz[i][1]} | {matriz[i][2]} ')
            if i==0 or i==1:
                print('-'*11)
        break
    if empate(matriz):
        print('O JOGO EMPATOU')
        break
    

    for i in range(3):
        print(f' {matriz[i][0]} | {matriz[i][1]} | {matriz[i][2]} ')
        if i==0 or i==1:
            print('-'*11)
    jogador_2(matriz)
    if vitoria(matriz):
        print('JOGADOR 2 VENCEU')
        for i in range(3):
            print(f' {matriz[i][0]} | {matriz[i][1]} | {matriz[i][2]} ')
            if i==0 or i==1:
                print('-'*11)
        break
    
