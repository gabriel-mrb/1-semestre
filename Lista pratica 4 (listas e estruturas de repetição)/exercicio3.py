# Ler um valor inteiro (aceitar somente valores entre 1 e 10) e escrever a
# tabuada de 1 a 10 do valor lido

while True:
    valor=int(input("Informe um valor de 1 a 10: "))
    if valor<1 or valor>10:
        print("Valor Invalido!")
        continue
    else:
        break

for i in range(1,11):
    print(f"{valor} * {i} = {valor*i}")
