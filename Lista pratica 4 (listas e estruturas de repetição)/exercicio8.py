# Faça um algoritmo que leia um número positivo e imprima seus
# divisores

divisores=[]
while True:
    numero=int(input("Informe um valor inteiro positivo:"))
    if numero<1:
        print("Valor invalido!")
        continue
    else:
        break

for i in range(1,numero+1):
            if numero%i==0:
                divisores.append(i)
print(80*"-")
print(f"Os divisores de {numero} sao : {divisores}")
print(80*"-")





