# Utilizando a estrutura de repetição for, faça um programa que receba 10
# números e conte quantos deles estão no intervalo [10,20] e quantos
# deles estão fora do intervalo

dentro_intervalo=[]
fora_intervalo=[]

for i in range(0,10):
    numero=float(input(f"Informe o {i+1}° valor:"))
    if numero<10 or numero>20:
        fora_intervalo.append(numero)
    else:
        dentro_intervalo.append(numero)

print(80*"-")
if len(dentro_intervalo)>0:     
    print(f"Voce digitou {len(dentro_intervalo)} numeros que estao dentro do intervalo, sendo eles: {dentro_intervalo}")
else:
    print("Voce nao digitou numeros dentro do intervalo")
print(80*"-")
if len(fora_intervalo)>0:   
    print(f"Voce digitou {len(fora_intervalo)} numeros que estao fora do intervalo, sendo eles {fora_intervalo}")
else:
    print("Voce nao digitou numeros fora do intevalo")
print(80*"-")