# 01-EXERCICE4

# Saisie des variables
var1 = input("Entrer le texte var1 : ")
var2 = input("Entrer le texte var2 : ")

# échange du contenu de var1 et var2
aux = var1
var1 = var2
var2 = aux

# Affichage
print("var1 : ", var1)
print("var2", var2, sep=" : ")