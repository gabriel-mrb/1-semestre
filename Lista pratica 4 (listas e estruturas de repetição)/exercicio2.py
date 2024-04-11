# Fazer um programa para encontrar todos os números pares entre 1 e 100

pares=[]

for i in range(1,101):
    if i%2==0:
        pares.append(i)

print(f"Pares: {pares}")
