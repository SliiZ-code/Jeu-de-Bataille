from carte import Carte
from paquet import Paquet
from listes import liste_cartes, liste_couleurs


def generation_deck():
    """Génération du paquet de départ
        en fonction des cartes et 
        couleurs choisies
    """
    deck = Paquet()
    for i in range(0, len(liste_couleurs)):
        for a in range(0, len(liste_cartes)):
            deck.ajouter(Carte(a, i))
    deck.shuffle()
    return deck
