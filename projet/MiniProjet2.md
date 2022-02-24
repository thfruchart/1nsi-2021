# Chiffrement de César 
## Principe
Le principe du chiffrement de César est simple : il consiste à décaler chaque lettre de l'alphabet d'une certaine valeur, appelée la clé de chiffrement.
Par exemple, avec une clé **k=3**, toutes les lettres de l'alphabet sont décalées de trois.

A ===> D  
B ===> E  
C ===> F  
et ainsi de suite...  

Ainsi le mot BAC sera chiffré EDF ! 


en fin d'alphabet, on revient au début :  
X ===> A  
Y ===> B  
Z ===> C  

Pour le déchiffrement, on procède de même en décalant dans l'autre sens.

# 1. Partie TP : chiffrement
* Programmer en Python les fonctions suivantes décrites dans leur chaîne de documentation
* tester chaque fonction sur des exemples pertinents. 

#### Fonction `cherche_indice`
```Python
def cherche_indice(car, texte):
    """car est un caractère, texte est une chaîne de caractères
    la fonction renvoie -1 si car ne figure pas dans texte
    sinon, elle renvoie le premier indice de car dans texte"""
```
exemples : 
```
>>> cherche_indice('A', 'ABCD')
0
>>> cherche_indice('D', 'ABCD')
3
>>> cherche_indice('X', 'ABCD')
-1
```

#### Fonction `lettre_numero`
```Python
ALPHABET = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'

def lettre_numero(n):
    """renvoie la lettre de l'ALPHABET dont le rang est n
    que n soit compris entre 0 et 25 ou pas ! """
```
exemples : 
```Python
>>> lettre_numero(0)
'A'
>>> lettre_numero(25)
'Z'
>>> lettre_numero(26)
'A'
>>> lettre_numero(28)
'C'
>>> lettre_numero(-2)
'Y'
```

#### Fonction `cesar`
```Python
def cesar(texte, decalage):
    """l'argument texte est écrit en MAJUSCULES (sans accents)
    Renvoie le texte chiffré avec le méthode de César,
    en prenant pour clé l'argument decalage """
```
exemples : 
```Python
>>> cesar('ABC', 1)
'BCD'
>>> cesar('ABC', -1)
'ZAB'
>>> cesar('BONJOUR, COMMENT CA VA ?', 11)
'MZYUZFC, NZXXPYE NL GL ?'
>>> cesar('NL GL MTPY, XPCNT PE EZT ?', -11)
'CA VA BIEN, MERCI ET TOI ?'
```



## 2. Partie projet : un programme qui craque un message
Le chiffrement de César est facile à casser si on connaît la lettre la plus fréquente du message (en français, par exemple, le E).

On pourra commencer par programmer la fonction suivante 
#### Fonction `occurrences`
```Python
def occurrences(txt):
    """txt est un texte écrit en MAJUSCULES
    la fonction renvoie un tableau contenant, pour chaque lettre de l'alphabet,
    le nombre de fois où elle apparaît dans txt"""
```
exemples : 
```Python
>>> occurrences('AAAA BBB CC D ZZZZZ')
[4, 3, 2, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 5]
```

On donne ci-dessous plusieurs messages à déchiffrer. 
Ecrire un programme capable de déchiffrer tous ces messages, en trouvant la clé de chiffrement (décalage) grâce à la recherche de la lettre la plus fréquente dans le texte chiffré. 

