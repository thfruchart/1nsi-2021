```>>> dico = {}
>>> dico['bit'] = "élément d'information valant 0 ou 1"
>>> dico
{'bit': 'binary digit = chiffre binaire'}
>>> dico['processeur'] = "unité de calcul de l'ordinateur"
>>> dico 
{'bit': 'binary digit = chiffre binaire',
 'processeur': "unité de calcul de l'ordinateur"}
>>> dico[0]
Traceback (most recent call last):
  File "<interactive input>", line 1, in <module>
KeyError: 0
>>> dico['bit']
"élément d'information valant 0 ou 1"
>>> dico['processeur']
"unité de calcul de l'ordinateur"
>>> len(dico)
2
>>> dico['RAM']='mémoire vive'
>>> len(dico)
3
>>> dico
{'RAM': 'mémoire vive',
 'bit': 'binary digit = chiffre binaire',
 'processeur': "unité de calcul de l'ordinateur"}```
