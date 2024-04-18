import tkinter as tk
import main

# Créer la fenêtre principale
fenetre = tk.Tk()
fenetre.title("Gestion des JO")
fenetre.configure(bg='#f4fefe')
fenetre.geometry("1000x500")
fenetre.maxsize(1000,500)
fenetre.minsize(1000,500)

def effacer_fenetre():
    for child in fenetre.winfo_children():
        if isinstance(child, tk.Frame):
            child.destroy()

def effacer_label():
    for child in fenetre.winfo_children():
        if isinstance(child, tk.Label):
            child.destroy()

def creer_bouton(fenetre, texte, commande, largeur, hauteur, couleur, police, taille):
    bouton = tk.Button(fenetre, text=texte, command=lambda: commande(), width=largeur, height=hauteur, bg=couleur, font=(police, taille))
    bouton.pack() #permet d'afficher le bouton
    return bouton

def interface_principale(): 
    effacer_fenetre()
    effacer_label()
    cadre_bouton_athlete = tk.Frame(fenetre)
    cadre_bouton_athlete.pack(side="left", fill="x", expand=True)
    cadre_bouton_athlete.configure(bg ='#f4fefe')
    cadre_bouton_visiteur = tk.Frame(fenetre)
    cadre_bouton_visiteur.pack(side="right", fill="x", expand=True)
    cadre_bouton_visiteur.configure(bg = '#f4fefe')
    cadre_bouton_retour = tk.Frame(fenetre, width=100, height=100, bg='green')
    cadre_bouton_retour.place(x=0, y=500, anchor='sw')

    # Créer et placer deux boutons initiaux au centre
    creer_bouton(cadre_bouton_athlete, "Athlètes", afficher_interface_athlete, 20, 10, '#5FD4EE','Tw Cen MT',20)
    creer_bouton(cadre_bouton_visiteur, "Visiteurs", afficher_interface_visiteur, 20, 10, '#EE5F5F','Tw Cen MT',20)
    creer_bouton(cadre_bouton_retour, "Quitter", fenetre.destroy, 5, 1, '#EE5F5F' , 'Tw Cen MT',20)

def afficher_interface_athlete():
    effacer_fenetre()
    # Supprimer les boutons initiaux

    cadre_bouton_retour1 = tk.Frame(fenetre, width=100, height=100, bg='grey')
    cadre_bouton_retour1.place(x=0, y=500, anchor='sw') #anchor sert a superpositionner ce bouton au dessus du cadre gauche

    creer_bouton(cadre_bouton_retour1, "Retour", interface_principale, 5, 1, '#EE5F5F' , 'Tw Cen MT',20)

    # Créer un Frame à gauche pour les boutons de gauche
    cadre_gauche = tk.Frame(fenetre)
    cadre_gauche.pack(side="left", fill="y") #fill=y pour créer un cadre a gauche de haut en bas et pour fill=x un cadre à gauche en haut

    # Ajouter trois boutons au Frame de gauche
    creer_bouton(cadre_gauche, "Afficher tous les athlètes", afficher_athlete, 20, 2, '#9ef0f6','Tw Cen MT',12)
    creer_bouton(cadre_gauche, "Afficher par pays", zone_de_texte, 20, 2,'#6ecaf2','Tw Cen MT',12)
    creer_bouton(cadre_gauche, "Afficher par discipline", afficher_athlete, 20, 2, '#2969eb','Tw Cen MT',12)

    # Créer un Frame à droite pour les boutons de droite
    cadre_droit = tk.Frame(fenetre)
    cadre_droit.pack(side="right", fill="y")

    # Ajouter trois boutons au Frame de droite
    creer_bouton(cadre_droit, "caca", afficher_athlete, 20, 2,'#9ef0f6','Tw Cen MT',12)
    creer_bouton(cadre_droit, "pipi", afficher_athlete, 20, 2,'#6ecaf2','Tw Cen MT',12)
    creer_bouton(cadre_droit, "popo", afficher_athlete, 20, 2,'#2969eb','Tw Cen MT',12)
    cadre_bouton_retour1.lift() # permet de placer le cadre cadre_bouton_retour1 au premier plan

def afficher_interface_visiteur():
    effacer_fenetre()
    # Supprimer les boutons initiaux
    cadre_bouton_retour2 = tk.Frame(fenetre, width=100, height=100, bg='grey')
    cadre_bouton_retour2.place(x=0, y=500, anchor='sw')

    creer_bouton(cadre_bouton_retour2, "Retour", interface_principale, 5, 1, '#EE5F5F' , 'Tw Cen MT',20)

    # Créer un Frame à gauche pour les boutons de gauche
    cadre_gauche = tk.Frame(fenetre)
    cadre_gauche.pack(side="left", fill="y")


    # Ajouter trois boutons au Frame de gauche
    creer_bouton(cadre_gauche, "Afficher tous les visiteurs", afficher_visiteur, 20,2, 'red','Tw Cen MT',12)

    # Créer un Frame à droite pour les boutons de droite
    cadre_droit = tk.Frame(fenetre)
    cadre_droit.pack(side="right", fill="both")

    # Ajouter trois boutons au Frame de droite

    creer_bouton(cadre_droit, "caca", afficher_athlete,20,2, 'red','Tw Cen MT',12)
    cadre_bouton_retour2.lift() # permet de placer le cadre cadre_bouton_retour1 au premier plan

def afficher_athlete():
    effacer_label()
    y_position = 10
    for element in main.admin.show_athlete():
        athlete = tk.Label(text = element)  # Créer un Label avec les informations de l'athlète
        athlete.configure(bg='#3399FF')
        athlete.place(x=200, y=y_position)  # Placer le Label dans la fenêtre
        y_position += 30

def afficher_visiteur():
    effacer_label()
    y_position = 10
    for element in main.admin.show_visiteur():
        text = tk.Label(text = element)  # Créer un Label avec les informations de l'athlète
        text.configure(bg='#3399FF')
        text.place(x=200, y=y_position)  # Placer le Label dans la fenêtre
        y_position += 30

#Création d'une zone texte pour demandé une entrée à l'utilisateur et l'a récupéré
def zone_texte():
    effacer_label()
    global zone
    zone = tk.Entry()
    zone.pack()

def recup_entree(event = None):
    texte = tk.Label(fenetre, text = zone.get())
    texte.place(x=200, y=200)
    
fenetre.bind("<Return>", recup_entree)


def rechercher_athlete(ENTRE):
    effacer_label()
    dic_ath=main.admin.ecriture_visiteur()
    while True:
            cle=input("Saissisez:NOM Prénom  ") #on demande le nom et prenom du visiteur à afficher
            if cle not in dic_ath.keys(): #on test si cette personne existe dans notre dico visiteur
                print("Réessayer, cette personne n'est pas renseignée !")
            else:
                infos=dic_ath[cle].afficher()
                print(infos)
                break

def rechercher_pays():
    effacer_label()
    y_position = 10
    for element in main.admin.search_pays():
        text = tk.Label(text = element)  # Créer un Label avec les informations de l'athlète
        text.configure(bg='#3399FF')
        text.place(x=200, y=y_position)  # Placer le Label dans la fenêtre
        y_position += 30

def rechercher_dis():
    effacer_label()
    y_position = 10
    for element in main.admin.search_dis():
        text = tk.Label(text = element)  # Créer un Label avec les informations de l'athlète
        text.configure(bg='#3399FF')
        text.place(x=200, y=y_position)  # Placer le Label dans la fenêtre
        y_position += 30



def rechercher_visiteur():
    effacer_label()
    y_position = 10
    for element in main.admin.search_visiteur():
        text = tk.Label(text = element)  # Créer un Label avec les informations de l'athlète
        text.configure(bg='#3399FF')
        text.place(x=200, y=y_position)  # Placer le Label dans la fenêtre
        y_position += 30

interface_principale()
fenetre.mainloop()