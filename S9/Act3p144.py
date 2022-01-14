def maximum(t):
    maxi_temporaire = t[0]
    for i in range(len(t)) :
        # lecture de la valeur du tableau
        v = t[i]
        # comparaison avec le maximum_temporaire
        if v > maxi_temporaire :
            maxi_temporaire = v
    return maxi_temporaire

def moyenne(t):
    total = 0
    for i in range(len(t)) :
        total += t[i]
    return total/len(t)




def moyenne(t):
    """ t est un tableau non vide
    la fonction renvoie la moyenne des valeurs du tableau"""
    total = 0
    for i in range(len(t)) :
        total += t[i]
    return total/len(t)
