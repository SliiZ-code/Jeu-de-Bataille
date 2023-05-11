from random import randint


def comparaison(jeu1, jeu2, player1, player2):
    """Comparaison entre les deux cartes en jeu 
       et ramassage des cartes par le gagnant

    Arguments:
        jeu1 (Paquet): Carte en jeu du joueur 1
        jeu2 (Paquet): Carte en jeu du joueur 2
        player1 (Paquet): Main du joueur 1
        player2 (Paquet): Main du joueur 2
    """
    Bataille=False

    # ------------------------
    if jeu1[0] > jeu2[0]:
        for i in range(len(jeu1)):
            if randint(0, 1) == 0:
                player1.ajouter(jeu1.retirer())
                player1.ajouter(jeu2.retirer())
            else:
                player1.ajouter(jeu2.retirer())
                player1.ajouter(jeu1.retirer())

    elif jeu2[0] > jeu1[0]:
        for i in range(len(jeu1)):
            if randint(0, 1) == 0:
                player2.ajouter(jeu1.retirer())
                player2.ajouter(jeu2.retirer())
            else:
                player2.ajouter(jeu2.retirer())
                player2.ajouter(jeu1.retirer())
    # ------------------------
    # Ramassage de toutes les cartes par le gagnant

    # ------------------------
    elif len(player1) < 2:
        while len(player1) != 0:
            player2.ajouter(player1.retirer())
    elif len(player2) < 2:
        while len(player2) != 0:
            player1.ajouter(player2.retirer())
    # ------------------------
    # Cas où un jouer n'aurait plus assez de cartes pour jouer une bataille

    else:
        Bataille = True
        print("BATAILLE")
    return Bataille
