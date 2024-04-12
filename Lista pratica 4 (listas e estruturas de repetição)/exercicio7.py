# Faça um programa que calcule e mostre a soma dos 50 primeiros
# números pares

pares=[]


for i in range(0,101):
    if i%2==0:
         pares.append(i)
print(80*"-")
print(f"A soma dos 50 primeiros pares é de: {sum(pares)}")
