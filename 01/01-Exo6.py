# Exercice 6 (à compléter)
n = int(input("Entrer le nombre d'oeufs :"))
print("nombre de boites : ", 1+ (n-1)//6)

#vérification
for n in range(13):
    print (n, " => ",1+ (n-1)//6)
