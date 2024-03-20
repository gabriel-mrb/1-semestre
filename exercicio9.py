idade=int(input("Informe sua idade (em anos): "))
tempo_servico=int(input("Informe seu tempo de servico (em anos): "))
if idade>59 and tempo_servico>24:
    print("Voce esta apto a se aposentar.")
elif idade>64 or tempo_servico>29:
    print("Voce esta apto a se aposentar.")
else:
    print("Voce nao esta apto a se aposentar.")
