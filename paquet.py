from random import shuffle


class Paquet:
    def __init__(self):
        """Initialisation du paquet"""
        self.liste = []

    def __len__(self):
        """ Méthode de longueur du paquet """
        return len(self.liste)

    def ajouter(self, carte):
        """Méthode d'ajout d'une carte au paquet

        Argument:
            carte (Carte): carte à ajouter
        """
        self.liste = [carte] + self.liste

    def retirer(self):
        """Méthode d'ajout d'une carte au paquet

        Renvoie:
            Carte: utilise la méthode pop() pour retirer et renvoyer la carte
        """
        if len == 0:
            return None
        else:
            return self.liste.pop()

    def __str__(self):
        """Affichage du paquet"""
        return str(self.liste)

    def __getitem__(self, n):
        """Obtention d'une carte à un index donné

        Argument:
            n (entier): index

        Renvoie:
            Carte: Renvoie la carte situé à n index
        """
        return self.liste[n]

    def shuffle(self):
        """Mélange du paquet"""
        shuffle(self.liste)
