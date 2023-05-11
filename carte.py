from listes import liste_cartes,liste_couleurs


class Carte:
    def __init__(self, index, couleur):
        """Initialisation de la classe

        Attributs:
            index (entier): index de la carte dans la liste 'liste_cartes'
            couleur (entier): index de la couleur dans la liste 'liste_couleurs'
        """
        self.index = index
        self.couleur = couleur

    def __eq__(self, carte):
        """Méthode de test d'égalité de cartes

        Arguments:
            carte (Carte): autre carte à comparer

        Renvoie:
            Booléen: résultat de l'égalité
        """
        if self.index == carte.index:
            return True
        else:
            return False

    def __gt__(self, carte):
        """Méthode de test de supériorité

        Arguments:
            carte (Carte): autre carte à comparer

        Renvoie:
            Booléen: résultat de la comparaison
        """
        if self.index < carte.index:
            return True
        else:
            return False

    def __repr__(self):
        """ Affichage de la carte dans la console
        """
        return f"{liste_cartes[self.index]} de {liste_couleurs[self.couleur]}"
