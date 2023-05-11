from paquet import Paquet
from random import randint
import time
from affichage import affichage
from generation_deck import generation_deck
from listes import liste_cartes, liste_couleurs, liste_cartes_images, liste_couleurs_images
from tkinter import *
from PIL import Image, ImageTk
from comparaison import comparaison

# Importation des modules

deck = generation_deck()    # Génération du paquet de départ
player1 = Paquet()
player2 = Paquet()
for i in range(len(liste_cartes)*len(liste_couleurs)):
    if len(player1) == len(liste_cartes)*len(liste_couleurs)//2:    # Division du paquet en 2
        player2.ajouter(deck[i])
    else:
        player1.ajouter(deck[i])
jeu1 = Paquet()
jeu2 = Paquet()

nb_tours = 0
Bataille = False
image_dos = Image.open('images/dos-bleu.png')

def tour():     # Fonction lancée à chaque tour

    global nb_tours
    global Bataille

    print(nb_tours)
    if Bataille == True:        # Éxécution des actions spécifiques à la bataille
        jeu1.ajouter(player1.retirer())
        jeu2.ajouter(player2.retirer())
        affichage('??????????', '??????????', player1, player2)
        tour_interface(image_dos, image_dos, jeu1, jeu2)
        Bataille = False
        return

    # Actions classiques

    nb_tours += 1
    jeu1.ajouter(player1.retirer())     # Ajout des 2 cartes
    jeu2.ajouter(player2.retirer())     # à jouer dans le tour
    affichage(jeu1[0], jeu2[0], player1, player2)   # Affichage dans la console
    image_joueur1 = Image.open(f'images/{liste_cartes_images[jeu1[0].index]}-{liste_couleurs_images[jeu1[0].couleur]}.png')     # Initialisation
    image_joueur2 = Image.open(f'images/{liste_cartes_images[jeu2[0].index]}-{liste_couleurs_images[jeu2[0].couleur]}.png')     # des images
    tour_interface(image_joueur1, image_joueur2, jeu1, jeu2)    # Affichage dans l'interface
    Bataille=comparaison(jeu1, jeu2, player1, player2)   # Comparaison des 2 cartes et fin du tour
    assert len(jeu1)+len(jeu2)+len(player1) + len(player2) == len(liste_cartes) * len(liste_couleurs), "Erreur nb cartes"   # Test de sécurité
    time.sleep(0.1) # Temps avant le prochain tour dans jeu_auto


def jeu_auto(): # Éxécution de tour() jusqu'à la fin de jeu
    while len(player1) != 0 and len(player2) != 0:
        tour()
        fenetre.update()
    print("FIN")
    tour_interface()

# ----------------------------------------
def all_children(window):
    _list = window.winfo_children()
    for item in _list:
        if item.winfo_children():
            _list.extend(item.winfo_children())
    return _list
def clear():
    widget_list = all_children(fenetre)
    for item in widget_list:
        item.pack_forget()
#----------------------------------------
# Fonctions permettant de séléctionner tout les éléments de la fenêtre et de les supprimer

def tour_interface(img1=image_dos, img2=image_dos, jeu1=None, jeu2=None):   # Affichage de chaque tour dans l'interface
    clear()
    cadre_joueur1 = LabelFrame(fenetre, text='Joueur 1', bg='white')
    cadre_joueur2 = LabelFrame(fenetre, text='Joueur 2', bg='white')
    cadre_carte_joueur1 = Label(cadre_joueur1)
    cadre_carte_joueur2 = Label(cadre_joueur2)
    cadre_infos = Frame(fenetre, pady=40, bg='#018001')

    #----------------------------------------
    if len(player1) == 0 or len(player2) == 0:
        infos = Label(cadre_infos, text="Partie terminée",
                      bg='#018001', font=('Helvetica', 14))
        infos.pack()
        if len(player1) == len(liste_cartes)*len(liste_couleurs):
            infos_gagnant = Label(
                cadre_infos, text="Joueur 1 a gagné", bg='#018001', font=('Helvetica', 14))
            infos_gagnant.pack()
        else:
            infos_gagnant = Label(
                cadre_infos, text="Joueur 2 a gagné", bg='#018001', font=('Helvetica', 14))
            infos_gagnant.pack()
    #----------------------------------------
    # Affichage de fin

    else:
        if Bataille == True:
            img1 = image_dos
            img2 = image_dos


        #------------------------
        img1 = ImageTk.PhotoImage(img1)
        img2 = ImageTk.PhotoImage(img2)
        cadre_carte_joueur1.image = img1
        cadre_carte_joueur1.config(image=img1)
        cadre_carte_joueur1.pack()
        cadre_carte_joueur2.image = img2
        cadre_carte_joueur2.config(image=img2)
        cadre_carte_joueur2.pack()
        #------------------------
        # Affichage des images des cartes

        #------------------------
        bouton_tour = Button(fenetre, text="Jouer", font='Helvetica',bg='white', height=2, width=10, command=tour)
        bouton_tour.pack(side=BOTTOM)
        bouton_jeuauto = Button(fenetre, text="Jeu auto", font='Helvetica',bg='white', height=2, width=10, command=jeu_auto)
        bouton_tour.pack(side=BOTTOM)
        bouton_jeuauto.pack()
        #------------------------
        # Boutons de jeu et jeu auto

        #----------------------------------------
        if jeu1 != None:
            if Bataille == False:
                infos_joueur1 = Label(cadre_joueur1, text=f"{jeu1[0]}", font=('Helvetica', 10, 'bold'), justify=CENTER)
                infos_joueur1.pack()
            nbcartes_joueur1 = Label(cadre_joueur1, text=f"Cartes restantes : {len(player1)}", font=('Helvetica', 10, 'bold'), justify=CENTER)
            nbcartes_joueur1.pack()
        if jeu2 != None:
            if Bataille == False:
                infos_joueur2 = Label(cadre_joueur2, text=f"{jeu2[0]}", font=('Helvetica', 10, 'bold'), justify=CENTER)
                infos_joueur2.pack()
            nbcartes_joueur2 = Label(cadre_joueur2, text=f"Cartes restantes : {len(player2)}", font=('Helvetica', 10, 'bold'), justify=CENTER)
            nbcartes_joueur2.pack()
        #----------------------------------------
        # Affichage nom des cartes et nombre de cartes restantes

        #----------------------------------------
        if jeu1 != None and jeu2 != None and Bataille == False:
            if jeu1[0].index < jeu2[0].index:
                infos = Label(cadre_infos, text="Le joueur 1 gagne ce tour",bg='#018001', font=('Helvetica', 14))
                infos.pack()
            elif jeu1[0].index > jeu2[0].index:
                infos = Label(cadre_infos, text="Le joueur 2 gagne ce tour",bg='#018001', font=('Helvetica', 14))
                infos.pack()
            else:
                texte_bataille = Label(cadre_infos, text="Bataille !", bg='#018001', font=('Helvetica', 40))
                texte_bataille.pack()
        #----------------------------------------
        # Affichage des infos 

        cadre_joueur1.pack(side=LEFT)
        cadre_joueur2.pack(side=RIGHT)

    cadre_infos.pack(side=BOTTOM)

#----------------------------------------
fenetre = Tk()
fenetre.title("Jeu de Bataille")
fenetre.geometry("750x750")
fenetre.minsize(600, 600)
fenetre.maxsize(1000, 1000)
fenetre.iconbitmap("logo.ico")
fenetre.config(background='#018001')
cadre_debut = Frame(fenetre, bg='#018001')
cadre_joueur1 = LabelFrame(fenetre, text='Joueur 1', bg='white')
cadre_joueur2 = LabelFrame(fenetre, text='Joueur 2', bg='white')
cadre_carte_joueur1 = Label(cadre_joueur1)
cadre_carte_joueur2 = Label(cadre_joueur2)
bouton_tour = Button(fenetre, text="Jouer", font='Helvetica',
                     bg='white', height=2, width=10, command=tour)
titre = Label(cadre_debut, text='Jeu de bataille', font=(
    'Franklin_Gothic', 30), bg='#018001', fg='white')
bouton = Button(cadre_debut, text="Jouer", font='Helvetica',
                bg='white', height=2, width=10, command=tour_interface)
titre.pack()
bouton.pack(pady=150)
cadre_debut.pack(expand=YES)
#----------------------------------------
# Initialisation et pernsonnalisation de l'interface

fenetre.mainloop()
