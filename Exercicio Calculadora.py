
while True:

    print("1-SOMA")
    print("2-SUBTRACAO")
    print("3-MULTIPLICACAO")
    print("4-DIVISAO")
    print("5-SAIR")


    opcao=int(input("Informe como voce deseja prosseguir: "))
    if opcao>=1 and opcao<=5:
        if opcao==1:
            n1=float(input("Informe o primeiro valor: "))
            n2=float(input("Informe o segundo valor: "))
            print(f"SOMA: {n1} + {n2} = {n1+n2}")    
        elif opcao==2:
            n1=float(input("Informe o primeiro valor: "))
            n2=float(input("Informe o segundo valor: "))
            print(f"SUBTRACAO: {n1} - {n2} = {n1-n2}")  
        elif opcao==3:
            n1=float(input("Informe o primeiro valor: "))
            n2=float(input("Informe o segundo valor: "))
            print(f"MULTIPLICACAO: {n1} * {n2} = {n1*n2}")  
        elif opcao==4:
            n1=float(input("Informe o primeiro valor: "))
            n2=float(input("Informe o segundo valor: "))
            if n2==0:
                print("Operacao invalida!\nTente novamente.")
            else:
                print(f"DIVISAO: {n1} / {n2} = {n1/n2}")   
        elif opcao==5:
            break
    else:
        print("Opcao invalida!\nTente novamente.")
        