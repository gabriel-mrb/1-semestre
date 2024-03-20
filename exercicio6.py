
p=[]
i=[]

while True:
    n=float(input("Digite um numero: "))
    print("Digite 0 para encerrar.")
    if n==0:
        break
    else:
        if n%2==0:
            p.append(n)
        else:
            i.append(n)

print("Pares: ",end="")
print(p,end="")
    

print("\nImpares: ",end="")
print(i,end="")


#FAZER FLUXOGRAMA

