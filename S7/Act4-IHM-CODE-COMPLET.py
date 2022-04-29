import imprimante

"""
Le module "imprimante" définit les fonctions suivantes :
 - reset() : Réinitialise l'imprimante.
 - fixer_temperature_cible(buse, plateau) : Assigne les températures cibles.
 - demarrer_chauffage() : Démarre le chauffage.
 - demarrer_impression() : Démarre l'impression.
 - lire_temperature() : Retourne un 2 uplet contenant les températures courantes de la buse et du plateau.
 - lire_temperature_cible() : Retourne un 2 uplet contenant les températures cibles de la buse et du plateau.
 - chauffage_en_cours() : True si l'imprimante est en train de chauffer, False sinon.
 - impression_en_cours() : True si l'imprimante est en train d'imprimer, False sinon.
"""

# Cette fonction est appelée quand l'utilisateur appuie sur le bouton "Start"
def demarrer_impression():
    if not imprimante.chauffage_en_cours():
        imprimante.demarrer_chauffage()
    print("Chauffage en cours")

# Cette fonction est appelée une fois au démarrage de l'impression
def afficher_message():
    print("Chauffage terminé : démarrage de l'impression")

# Cette fonction est appelée quand l'utilisateur appuie sur le bouton "ABS"
def fixer_temperatures_abs():
    if not imprimante.chauffage_en_cours():
        imprimante.fixer_temperature_cible(230, 100)

# Cette fonction est appelée quand l'utilisateur appuie sur le bouton "PLA"
def fixer_temperatures_pla():
    if not imprimante.chauffage_en_cours():
        imprimante.fixer_temperature_cible(180, 60)

message_affiche = False

# Cette fonction est appelée cycliquement, à la suite de la fonction setup
def loop():
    global message_affiche
    t_b_cible, t_p_cible = imprimante.lire_temperature_cible()
    t_b, t_p = imprimante.lire_temperature()
    if round(t_b, 1) >= t_b_cible and round(t_p, 1) >= t_p_cible and imprimante.chauffage_en_cours() and not imprimante.impression_en_cours():
        imprimante.demarrer_impression()
    if imprimante.impression_en_cours() and not message_affiche:
        afficher_message()
        message_affiche = True
