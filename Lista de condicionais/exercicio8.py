idade=int(input("Informe sua idade (em anos): "))
if idade<16:
    print("Voce nao esta apto a votar.")
elif 15<idade<18 or idade>65:
    print("Voce é um eleitor facultativo.")
else:
    print("Voce é um eleitor obrigatorio.")
