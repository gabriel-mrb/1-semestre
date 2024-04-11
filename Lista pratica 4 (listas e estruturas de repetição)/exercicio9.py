# Faça um algoritmo que leia 10 números inteiros, armazene-os em uma
# lista e imprima em ordem crescente

lista=[]
i=0


while i<10:
    valor=int(input(f"Informe o seu {i+1}° valor:"))
    if valor in lista:
        print("Valor repetido")
        continue
    else:
        lista.append(valor)
        i+=1

lista.sort()
print(80*"-")
print(lista)
print(80*"-")