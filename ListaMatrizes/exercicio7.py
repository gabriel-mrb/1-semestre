# Faça um programa de cadastro de pessoas. Cada pessoa deve ser uma
# lista com as informações:
# [“Nome”, “CPF”, idade (int), renda_mensal (float]
# O programa deve sempre perguntar se quer cadastrar mais uma
# pessoa ou sair. Ao final, as pessoas devem estar cadastradas na mesma
# matriz e as informações devem ser printadas em tela uma embaixo da
# outra. Ainda, deve-se calcular a média de idade e a média de renda
# mensal (imprimir informações).

matriz=[]

def cadastrar_pessoa(matriz):
    lista=[]
    matriz.append(lista)
    lista.append(input('\nInforme seu nome: '))
    lista.append(input('Informe seu CPF: '))
    lista.append(int(input('Informe sua idade: ')))
    lista.append(float(input('Informe sua renda mensal: ')))
    return matriz

def verificar_cadastros(matriz):
    print('Seus Cadastros:')
    for i in range(len(matriz)):
        print(matriz[i])
    
def somas(matriz):
    idade=0
    for i in range(len(matriz)):
        idade+=matriz[i][2]
    return idade/len(matriz)

def renda(matriz):
    renda=0
    for i in range(len(matriz)):
        renda +=matriz[i][3]
    return renda/len(matriz)

while True:
    
    print('1-CADASTRAR PESSOA\n2-VER CADASTROS\n3-SAIR')
    opcao=int(input('Informe como voce deseja prosseguir: '))
    match opcao:
        case 1:
            matriz=cadastrar_pessoa(matriz)

        case 2:
            verificar_cadastros(matriz)
            print(f'\nIDADE MEDIA: {somas(matriz)}')
            print(f'RENDA MEDIA: {renda(matriz)}\n')

        case 3:
            break