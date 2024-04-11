# Ler 10 números e imprimir quantos são pares e quantos são ímpares

pares=[]
impares=[]

for i in range(0,10):
    numero=float(input(f"Informe o {i+1}° valor: "))
    if numero%2==0:
        pares.append(numero)
    else:
        impares.append(numero)

print(80*"-")
print(f"Voce digitou {len(pares)} numeros pares, sendo eles: {pares}")
print(f"Voce digitou {len(impares)} numeros impares, sendo eles: {impares}")