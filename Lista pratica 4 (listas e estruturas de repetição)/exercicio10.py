# Dada a lista = [2, 4, 7, 2, 3, 3, 1, 0, 2, 6] imprima o número que se repete
# mais vezes.

lista=[2,4,7,2,3,3,1,0,2,6]
repeticoes=0
numero_frequente=0


for i in lista:
    if lista.count(i)>repeticoes:
        repeticoes=lista.count(i)
        numero_frequente=i
        
print(80*"-")
print(f"O numero com mais repetições na lista é o {numero_frequente}, com {repeticoes} repeticoes.")
print(80*"-")


