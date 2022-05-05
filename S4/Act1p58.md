```python
# question 4
>>> table = lecture_fichier('stations.csv')
# question 5 : le type est liste de liste
# question 6
>>> len(table)-1 # donne le nombre de stations
32
# question 7
>>> table[0] # donne les descripteurs
['id', 'latitude', 'longitude', 'couleur', 'nom', 'description', 'T2', 'T3', 'Super_chargeur', 'distance_km']
# question 8
>>> table[22] # donne la 22ème station
['22', '49.20', '2.21', '#0000FF', 'reveo', 'Rue Des Condamines 11290 ARZENS', '2', '1', 'Non', '129.7']
>>> table[22][1] = '43.20'   # modifie la valeur fausse : 49.2 --> 43.2
# question 9 : il faut modifier chaque ligne de la table en y ajoutant une valeur
```
