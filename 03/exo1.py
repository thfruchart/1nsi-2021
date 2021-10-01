n = int (input("entrer un entier : "))

# on veut afficher les diviseurs de n
for i in range(1, n+1) : # pour chaque entier de 1 à n inclus
    if n%i == 0:  # on calcule le reste de la division
        print(i)  # on affiche uniquement lorsque le reste est nul : i est alors diviseur de n
