print("Dada a expressao: ax² + bx + c = 0")
while True:
    a=float(input("Informe o valor de a :"))
    if a==0:
        print('Valor invalido')
    else:
        break
b=float(input("Informe o valor de b :"))
c=float(input("Informe o valor de c :"))
delta=b**2-4*a*c
if delta>0:
    print("Delta é maior que zero\nPortanto existem duas raizes distintas")
elif delta==0:
    print("Delta é igual a zero\nPortanto existem duas raizes iguais")
else:
    print("Delta é menor que zero\nPortanto existem duas raizes imaginarias conjugadas")
    