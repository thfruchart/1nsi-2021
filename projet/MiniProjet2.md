# Chiffrement de César : un programme qui craque un message
## Principe
Le principe du chiffrement de César est simple : il consiste à décaler chaque lettre de l'alphabet d'une certaine valeur, appelée la clé de chiffrement.
Par exemple, avec une clé **k=3**, toutes les lettres de l'alphabet sont décalées de trois.

A ===> D  
B ===> E  
C ===> F  
et ainsi de suite...  
en fin d'alphabet, on revient au début :  
X ===> A  
Y ===> B  
Z ===> C  
Ainsi le mot BAC sera chiffré EDF ! 

Pour le déchiffrement, on procède de même en décalant dans l'autre sens.

# 1. Partie TP
* Programmer en Python les fonctions suivantes décrites dans leur chaîne de documentation
* tester chaque fonction sur des exemples pertinents. 

```
def cherche_indice(car, texte):
    """car est un caractère, texte est une chaîne de caractères
    la fonction renvoie -1 si car ne figure pas dans texte
    sinon, elle renvoie le premier indice de car dans texte"""
```


## 2. Partie projet
