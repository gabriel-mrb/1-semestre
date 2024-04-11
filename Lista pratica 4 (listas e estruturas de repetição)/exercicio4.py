# Leia várias idades e calcule a média entre as idades (usar uma variável para idade)

lista_idade=[]
while True:
    idade=int(input("Informe a sua idade: "))
    if idade<1:
        print("Valor Invalido!")
        continue
    else:
        lista_idade.append(idade)
        print("Valor cadastrado com sucesso!")
    if input("Deseja adicionar mais valores (sim/não): ").upper()=="SIM":
        continue
    else:
        break

media=sum(lista_idade) / len(lista_idade)
print(80*"-")
print(f"A média das idades registradas é de: {media:.2f} anos.")
