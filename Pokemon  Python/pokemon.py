# Projeto: Jogo Pokemon silplificado em Python


import random
import sys

pokemon_floresta = ["Treecko", "Torterra", "Venusaur", "Bayleef", "Ivysaur", "Sceptile","Flygon","Eevee","Garchomp","Greninja"]
pokemon_caverna = ["Meowscarada", "Chein-Pao", "Panda", "Gengar", "HeraCross", "Blaziken","Luxray","Tyranitar","Gardevoir","Lucario"]
pokemon_capturados=[]
chances=3
sair=''
nome=''

print("Olá, Seja bem vindo a Aventura Pokemón.",)
print("Eu sou o Professor Carvalho e estou aqui para lhe auxiliar nessa jornada Pokemon!")
while nome=='':
    nome=input("Por favor, informe o seu nome: ")
    sys.stdout.write("\033[H\033[J")
    sys.stdout.flush()

sys.stdout.write("\033[H\033[J")
sys.stdout.flush()
print(f'Olá {nome}, fico feliz que esteja aqui!...')                     
print(f"Nesta jornada, voce terá a opcao de entrar na caverna ou floresta ambas possuem Pokemons únicos.\nConforme voce captura novos Pokemon, voce poderá checar quais voce ja capturou ao retornar ao menu, mas você terá somente 3 chances de captura, então as use com sabedoria!\nBom jogo!")
print('')
print('Pressione ENTER para continuar')
input()

while sair!='SIM' and chances>0:  
    opcao_sair=''
    sys.stdout.write("\033[H\033[J")
    sys.stdout.flush()
    print("Menu:")
    print('1.Floresta\n2.Caverna\n3.Seus Pokemon\n4.Sair')
    escolha=input('Informe como voce deseja prosseguir: ')
    sys.stdout.write("\033[H\033[J")
    sys.stdout.flush()

    if escolha=='1':
        print('Voce entrou na floresta...')
        input()
        pokemon=random.choice(pokemon_floresta)
        while opcao_sair!='SIM':
            sys.stdout.write("\033[H\033[J")
            sys.stdout.flush()
            print(f'Voce encontrou um {pokemon}!\n')
            if pokemon not in pokemon_capturados:
                print('Voce nunca capturou este Pokemon')
            else:
                print('Voce ja capturou este Pokemon')
            opcao=input('Deseja captura-lo (sim/nao)?: ').upper()
            if opcao=='SIM':
                while opcao_sair!='SIM':
                    captura=random.randint(0,100)
                    if captura>=50:
                        sys.stdout.write("\033[H\033[J")
                        sys.stdout.flush()
                        print(f'Parabens! Voce capturou um {pokemon}')
                        pokemon_capturados.append(pokemon)
                        input()
                        while True:
                            opcao_sair=input('Voce deseja sair da floresta (sim/nao)?: ').upper()
                            sys.stdout.write("\033[H\033[J")
                            sys.stdout.flush()
                            if opcao_sair=='SIM':
                                print('Voce saiu da floresta.')
                                input()
                                break
                            elif opcao_sair=='NAO':
                                print('Voce se aprofunda na floresta...')
                                pokemon=random.choice(pokemon_floresta)
                                input()
                                sys.stdout.write("\033[H\033[J")
                                sys.stdout.flush()
                                break
                            else:
                                print('Opcao Invalida!\nTente novamente.')
                                input()
                                sys.stdout.write("\033[H\033[J")
                                sys.stdout.flush()
                                continue
                        break
                    else:
                        sys.stdout.write("\033[H\033[J")
                        sys.stdout.flush()
                        chances-=1
                        if chances>0:
                            while True:
                                opcao=input(f'O Pokemon escapou, voce ainda tem {chances} chances restantes,\nDeseja tentar novamente (sim/nao)?: ').upper()
                                sys.stdout.write("\033[H\033[J")
                                sys.stdout.flush()
                                if opcao=='SIM':
                                    break
                                elif opcao=='NAO':
                                    print('Voce saiu da floresta...')
                                    opcao_sair='SIM'
                                    input()
                                    break
                                else:
                                    print('Opcao Invalida!\nTente novamente.')
                                    input()
                                    sys.stdout.write("\033[H\033[J")
                                    sys.stdout.flush()
                                    continue
                            continue
                                
                        else:
                            print(f'O {pokemon} fugiu.')
                            input()
                            sys.stdout.write("\033[H\033[J")
                            sys.stdout.flush()
                            print(f'Parece que voce nao tem mais tentativas ({chances}/3)\nObrigado por jogar!.')
                            input()
                            opcao_sair='SIM'
                continue
                
            elif opcao=='NAO':
                sys.stdout.write("\033[H\033[J")
                sys.stdout.flush()
                print('Voce saiu da floresta...')
                input()
                break
            else:
                sys.stdout.write("\033[H\033[J")
                sys.stdout.flush()
                print('Opcao Invalida\nTente novamente')
                input()
                sys.stdout.write("\033[H\033[J")
                sys.stdout.flush() 
                
                continue
        continue

    elif escolha=='2':
        print('Voce entrou na caverna...')
        input()
        pokemon=random.choice(pokemon_caverna)
        while opcao_sair!='SIM':
            sys.stdout.write("\033[H\033[J")
            sys.stdout.flush()
            print(f'Voce encontrou um {pokemon}!\n')
            if pokemon not in pokemon_capturados:
                print('Voce nunca capturou este Pokemon')
            else:
                print('Voce ja capturou este Pokemon')
            opcao=input('Deseja captura-lo (sim/nao)?: ').upper()
            if opcao=='SIM':
                while opcao_sair!='SIM':
                    captura=random.randint(0,100)
                    if captura>=65:
                        sys.stdout.write("\033[H\033[J")
                        sys.stdout.flush()
                        print(f'Parabens! Voce capturou um {pokemon}')
                        pokemon_capturados.append(pokemon)
                        input()
                        while True:
                            opcao_sair=input('Voce deseja sair da caverna (sim/nao)?: ').upper()
                            sys.stdout.write("\033[H\033[J")
                            sys.stdout.flush()
                            if opcao_sair=='SIM':
                                print('Voce saiu da caverna.')
                                input()
                                break
                            elif opcao_sair=='NAO':
                                print('Voce se aprofunda na caverna...')
                                pokemon=random.choice(pokemon_caverna)
                                input()
                                sys.stdout.write("\033[H\033[J")
                                sys.stdout.flush()
                                break
                            else:
                                print('Opcao Invalida!\nTente novamente.')
                                input()
                                sys.stdout.write("\033[H\033[J")
                                sys.stdout.flush()
                                continue
                        break
                    else:
                        sys.stdout.write("\033[H\033[J")
                        sys.stdout.flush()
                        chances-=1
                        if chances>0:
                            while True:
                                opcao=input(f'O Pokemon escapou, voce ainda tem {chances} chances restantes,\nDeseja tentar novamente (sim/nao)?: ').upper()
                                sys.stdout.write("\033[H\033[J")
                                sys.stdout.flush()
                                if opcao=='SIM':
                                    break
                                elif opcao=='NAO':
                                    print('Voce saiu da caverna...')
                                    opcao_sair='SIM'
                                    input()
                                    break
                                else:
                                    print('Opcao Invalida!\nTente novamente.')
                                    sys.stdout.write("\033[H\033[J")
                                    sys.stdout.flush()
                                    input()
                                    continue
                            continue
                                
                        else:
                            print(f'O {pokemon} fugiu.')
                            input()
                            sys.stdout.write("\033[H\033[J")
                            sys.stdout.flush()
                            print(f'Parece que voce nao tem mais tentativas ({chances}/3)\nObrigado por jogar!.')
                            input()
                            opcao_sair='SIM'
                continue
                
            elif opcao=='NAO':
                sys.stdout.write("\033[H\033[J")
                sys.stdout.flush()
                print('Voce saiu da caverna...')
                input()
                break
            else:
                sys.stdout.write("\033[H\033[J")
                sys.stdout.flush()
                print('Opcao Invalida\nTente novamente')
                input()
                sys.stdout.write("\033[H\033[J")
                sys.stdout.flush() 
                
                continue
        continue

    elif escolha=='3':
        if len(pokemon_capturados)==0:
            print('Voce ainda nao possui nenhum Pokemon.')
            input()
            sys.stdout.write("\033[H\033[J")
            sys.stdout.flush()
        else:
            pokemon_capturados.sort()
            print('Seus Pokemon:')
            for i in pokemon_capturados:
                print(f"- {i}")
        input()

    elif escolha=='4':
        while True:
            sair=input('Voce realmente deseja sair (sim/nao)?: ').upper()
            sys.stdout.write("\033[H\033[J")
            sys.stdout.flush() 
            if sair=='SIM':
                print('Obrigado por jogar!')
                break
            elif sair=='NAO':
                break
            else:
                print('Opcao Invalida!\nTente novamente')
                input()
                sys.stdout.write("\033[H\033[J")
                sys.stdout.flush() 
                continue
    else:
        sys.stdout.write("\033[H\033[J")
        sys.stdout.flush()
        print('Opcao Invalida!\n')
        input()
         
        continue
