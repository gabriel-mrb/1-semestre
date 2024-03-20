
print("1-PUCPR\n2-UNICAMP")
codigo=input("Informe o codigo da instituicao (1/2): ")
n1=float(input("Informe a nota 1 do aluno: "))
n2=float(input("Informe a nota 2 do aluno: "))
media=(n1+n2)/2

if codigo==1:
    if media>=7:
        print(f"MEDIA: {media:.2f}")
        print("Aluno aprovado.")
    elif media<4:
        print(f"MEDIA: {media:.2f}")
        print("Aluno reproovado.")
    else:
        print(f"MEDIA: {media:.2f}")
        print("Aluno em exame")

else:
    if media>=5:
        print(f"MEDIA: {media:.2f}")
        print("Aluno aprovado.")
    else:
        print(f"MEDIA: {media:.2f}")
        print("Aluno em exame")