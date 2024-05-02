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

def effacer_texte(): #Obligatoire pour pouvoir rafraichir la zone de texte 
    for child in fenetre.winfo_children():
        if isinstance(child, tk.Entry):
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
    creer_bouton(cadre_bouton_retour, "Quitter", fenetre.destroy, 5, 1, '#b50000' , 'Tw Cen MT',20)

def afficher_interface_athlete():
    # Supprimer les boutons initiaux
    effacer_fenetre()
    effacer_label()
    effacer_texte()
    #Créer un cadre pour le bouton retour
    cadre_bouton_retour1 = tk.Frame(fenetre, width=100, height=100, bg='grey')
    cadre_bouton_retour1.place(x=0, y=500, anchor='sw') #anchor sert a superpositionner ce bouton au dessus du cadre gauche
    #On créer le bouton retour
    creer_bouton(cadre_bouton_retour1, "Retour", interface_principale, 5, 1, '#b50000' , 'Tw Cen MT',20)

    # Créer un Frame à gauche pour les boutons de gauche
    cadre_gauche = tk.Frame(fenetre, bg='#cbd4d4')
    cadre_gauche.pack(side="left", fill="y") #fill=y pour créer un cadre a gauche de haut en bas et pour fill=x un cadre à gauche en haut

    # Ajouter les boutons au Frame de gauche
    creer_bouton(cadre_gauche, "Afficher tous les athlètes", afficher_athlete, 20, 2, '#9ef0f6','Tw Cen MT',12)
    creer_bouton(cadre_gauche, "Rechercher un athlète", zone_texte_ath, 20, 2, '#6ecaf2','Tw Cen MT',12)
    creer_bouton(cadre_gauche, "Afficher par pays", zone_texte_pays, 20, 2,'#2969eb','Tw Cen MT',12)
    creer_bouton(cadre_gauche, "Afficher par discipline", afficher_athlete, 20, 2, '#0a55ea','Tw Cen MT',12)
    
    # Créer un Frame à droite pour les boutons de droite
    cadre_droit = tk.Frame(fenetre,bg='#cbd4d4')
    cadre_droit.pack(side="right", fill="y")

    # Ajouter les boutons au Frame de droite
    creer_bouton(cadre_droit, "Ajouter un athlète", afficher_athlete, 20, 2,'#9ef0f6','Tw Cen MT',12)
    creer_bouton(cadre_droit, "Supprimer un athlète", afficher_athlete, 20, 2,'#6ecaf2','Tw Cen MT',12)
    creer_bouton(cadre_droit, "Ajouter une récompense", afficher_athlete, 20, 2,'#2969eb','Tw Cen MT',12)
    creer_bouton(cadre_droit, "Supprimer une récompense", afficher_athlete, 20, 2,'#0a55ea','Tw Cen MT',12)

    # permet de placer le cadre cadre_bouton_retour1 au premier plan
    cadre_bouton_retour1.lift() 

def afficher_interface_visiteur():
    # Supprimer les boutons initiaux
    effacer_fenetre()
    effacer_label()
    effacer_texte()
    #Créer un cadre pour le bouton retour
    cadre_bouton_retour2 = tk.Frame(fenetre, width=100, height=100, bg='grey')
    cadre_bouton_retour2.place(x=0, y=500, anchor='sw')
    #On créer le bouton retour
    creer_bouton(cadre_bouton_retour2, "Retour", interface_principale, 5, 1, '#b50000' , 'Tw Cen MT',20)

    # Créer un Frame à gauche pour les boutons de gauche
    cadre_gauche = tk.Frame(fenetre,bg='#cbd4d4')
    cadre_gauche.pack(side="left", fill="y")#fill=y pour créer un cadre a gauche de haut en bas et pour fill=x un cadre à gauche en haut

    # Ajouter les boutons au Frame de gauche
    creer_bouton(cadre_gauche, "Afficher tous les visiteurs", afficher_visiteur, 20,2, '#ff7070','Tw Cen MT',12)
    creer_bouton(cadre_gauche, "Rechercher un visiteur par son nom", zone_texte_visi_nom, 20, 2, '#ff3f3f','Tw Cen MT',12)
    creer_bouton(cadre_gauche, "Rechercher un visiteur par son numéro", zone_texte_visi_num, 20, 2,'#ff0000','Tw Cen MT',12)

    # Créer un Frame à droite pour les boutons de droite
    cadre_droit = tk.Frame(fenetre,bg='#cbd4d4')
    cadre_droit.pack(side="right", fill="both")

    # Ajouter les boutons au Frame de droite
    creer_bouton(cadre_droit, "Ajouter un visiteur", afficher_athlete,20,2, 'red','Tw Cen MT',12)
    creer_bouton(cadre_droit, "Supprimer un visiteur", afficher_athlete,20,2, 'red','Tw Cen MT',12)
    creer_bouton(fenetre=cadre_droit, texte="",commande=None, largeur=20, hauteur=2, couleur='#cbd4d4',police='Tw Cen MT',taille=12)
    creer_bouton(cadre_droit, "Afficher la map", afficher_athlete, 20, 2, '#00ff73','Tw Cen MT',12)
    cadre_bouton_retour2.lift() # permet de placer le cadre cadre_bouton_retour1 au premier plan

#Définition des fonctions:
def afficher_athlete():
    effacer_label()
    effacer_texte()
    y_position = 10
    for lignes in main.admin.show_athlete():
        athlete = tk.Label(text = lignes)  # Créer un Label avec les informations de l'athlète
        athlete.configure(bg='#3399FF')
        athlete.place(x=200, y=y_position)  # Placer le Label dans la fenêtre
        y_position += 30

def afficher_visiteur():
    effacer_label()
    effacer_texte()
    y_position = 10
    for lignes in main.admin.show_visiteur():
        text = tk.Label(text = lignes)  # Créer un Label avec les informations de l'athlète
        text.configure(bg='#3399FF')
        text.place(x=200, y=y_position)  # Placer le Label dans la fenêtre
        y_position += 30

#Configuration de deux petites fonctions qui vont permettre de supprimer la justification des ENTRY lorsque l'on veut clique dessus
#et lorsque l'on y sort elle réapparait
def retire_justi_ath_nom(event=None):
    if zone_ath_nom.get() == "NOM":
        zone_ath_nom.delete(0,'end')#les parametres sont les positions des caractères à retirer, ici du débu (0) à la fin ("end")
        zone_ath_nom.config(fg="Black",font=("Tw Cent Mt",13))

def remise_justi_ath_nom(event=None):
    if zone_ath_nom.get() == "":
        zone_ath_nom.insert(0,"NOM")
        zone_ath_nom.config(fg="gray",font=("Tw Cent Mt",13))

def retire_justi_ath_prenom(event=None):
    if zone_ath_prenom.get() == "Prénom":
        zone_ath_prenom.delete(0,'end')#les parametres sont les positions des caractères à retirer, ici du débu (0) à la fin ("end")
        zone_ath_prenom.config(fg="Black",font=("Tw Cent Mt",13))

def remise_justi_ath_prenom(event=None):
    if zone_ath_prenom.get() == "":
        zone_ath_prenom.insert(0,"Prénom")
        zone_ath_prenom.config(fg="gray",font=("Tw Cent Mt",13))

#Création des zones textes pour demandé les différentes entrées à l'utilisateur
def zone_texte_ath():
    effacer_label()
    effacer_texte()
    global zone_ath_nom
    zone_ath_nom = tk.Entry(fg="gray",font=("Tw Cent Mt",13))
    zone_ath_nom.insert(0,"NOM")
    zone_ath_nom.bind("<FocusIn>", retire_justi_ath_nom) #le focus, c-a-d lorsque l'utilisateur commence à taper dans l'entrée
    zone_ath_nom.bind("<FocusOut>", remise_justi_ath_nom) #perd le focus, c-a-d lorsque l'utilisateur cesse de taper dans l'entrée ou passe à un autre widget ou quitte la fenêtre
    zone_ath_nom.pack()
    global zone_ath_prenom
    zone_ath_prenom = tk.Entry(fg="gray",font=("Tw Cent Mt",13))
    zone_ath_prenom.insert(0,"Prénom")
    zone_ath_prenom.bind("<FocusIn>", retire_justi_ath_prenom)
    zone_ath_prenom.bind("<FocusOut>", remise_justi_ath_prenom)
    zone_ath_prenom.pack()
    fenetre.bind("<Return>", rechercher_athlete) #lorsque la touche "entrée" du clavier est actionné, c'est la fonction recherhcer athlete qui s'exécute

def rechercher_athlete(event=None):
    effacer_label()
    Nom=zone_ath_nom.get()
    Prénom=zone_ath_prenom.get()
    ENTREE=Nom+" "+Prénom
    #print (ENTREE)
    dic_ath=main.admin.ecriture_visiteur()
    if main.admin.search_athlete(ENTREE)=="ERREUR": #on test si cette personne est bien dans notre dico athlete
            text = tk.Label(text = "Réessayer cet(te) athlète ne participe pas aux jeux !")  # Créer un Label avec les informations de l'athlète
            text.configure(bg='#3399FF') #on définit le background du texte
            text.place(x=400, y=50)
            
    else:
        infos=main.admin.search_athlete(ENTREE)
        text = tk.Label(text = infos)  # Créer un Label avec les informations de l'athlète
        text.configure(bg='#3399FF') #on définit le background du texte
        text.place(x=400, y=50)  # Placer le Label dans la fenêtre

#Configuration d'une petite fonction qui vont permettre de supprimer la justification des ENTRY lorsque l'on veut clique dessus
def retire_justi_pays(event=None):
    if zone_pays.get() == "PAYS":
        zone_pays.delete(0,'end')#les parametres sont les positions des caractères à retirer, ici du débu (0) à la fin ("end")
        zone_pays.config(fg="Black",font=("Tw Cent Mt",13))

def zone_texte_pays():
    effacer_label()
    effacer_texte()
    global zone_pays
    zone_pays = tk.Entry(fg="gray",font=("Tw Cent Mt",13))
    zone_pays.insert(0,"PAYS")
    zone_pays.bind("<FocusIn>", retire_justi_pays)
    zone_pays.pack()
    fenetre.bind("<Return>", rechercher_pays) #lorsque la touche "entrée" du clavier est actionné, c'est la fonction rechercher pays qui s'exécute

def rechercher_pays(event=None):
    effacer_label()
    ENTREE=zone_pays.get()
    #print (ENTREE)
    y_position = 50
    if main.admin.search_pays(ENTREE)=="ERREUR": #on test si le paus rentré est bien dans les jeux
            text = tk.Label(text = "Réessayer ce pays ne participe pas aux jeux !")  # Créer un Label avec les informations de l'athlète
            text.configure(bg='#3399FF') #on définit le background du texte
            text.place(x=400, y=50)   
    else:
        infos=main.admin.search_pays(ENTREE)
        #print (infos)
        for lignes in infos:
            text = tk.Label(text = lignes)  # Créer un Label avec les informations de l'athlète
            text.configure(bg='#3399FF') #on définit le background du texte
            text.place(x=200, y=y_position)  # Place le Label dans la fenêtre
            y_position += 30

#Configuration de deux petites fonctions qui vont permettre de supprimer la justification des ENTRY lorsque l'on veut clique dessus
#et lorsque l'on y sort elle réapparait
def retire_justi_visiteur_nom(event=None):
    if zone_visiteur_nom.get() == "NOM":
        zone_visiteur_nom.delete(0,'end')#les parametres sont les positions des caractères à retirer, ici du débu (0) à la fin ("end")
        zone_visiteur_nom.config(fg="Black",font=("Tw Cent Mt",13))

def remise_justi_visiteur_nom(event=None):
    if zone_visiteur_nom.get() == "":
        zone_ath_nom.insert(0,"NOM")
        zone_ath_nom.config(fg="gray",font=("Tw Cent Mt",13))

def retire_justi_visiteur_prenom(event=None):
    if zone_visiteur_prenom.get() == "Prénom":
        zone_visiteur_prenom.delete(0,'end')#les parametres sont les positions des caractères à retirer, ici du débu (0) à la fin ("end")
        zone_visiteur_prenom.config(fg="Black",font=("Tw Cent Mt",13))

def remise_justi_visiteur_prenom(event=None):
    if zone_visiteur_prenom.get() == "":
        zone_visiteur_prenom.insert(0,"Prénom")
        zone_visiteur_prenom.config(fg="gray",font=("Tw Cent Mt",13))

def zone_texte_visi_nom():
    effacer_label()
    effacer_texte()
    global zone_visiteur_nom
    zone_visiteur_nom = tk.Entry(fg="gray",font=("Tw Cent Mt",13))
    zone_visiteur_nom.insert(0,"NOM")
    zone_visiteur_nom.bind("<FocusIn>", retire_justi_visiteur_nom) #le focus, c-a-d lorsque l'utilisateur commence à taper dans l'entrée
    zone_visiteur_nom.bind("<FocusOut>", remise_justi_visiteur_nom) #perd le focus, c-a-d lorsque l'utilisateur cesse de taper dans l'entrée ou passe à un autre widget ou quitte la fenêtre
    zone_visiteur_nom.pack()
    global zone_visiteur_prenom
    zone_visiteur_prenom = tk.Entry(fg="gray",font=("Tw Cent Mt",13))
    zone_visiteur_prenom.insert(0,"Prénom")
    zone_visiteur_prenom.bind("<FocusIn>", retire_justi_visiteur_prenom)
    zone_visiteur_prenom.bind("<FocusOut>", remise_justi_visiteur_prenom)
    zone_visiteur_prenom.pack()
    fenetre.bind("<Return>", rechercher_visiteur_nom) #lorsque la touche "entrée" du clavier est actionné, c'est la fonction rechercher_visiteur_nom qui s'exécute

def rechercher_visiteur_nom():
    effacer_label()
    y_position = 10
    for element in main.admin.search_visiteur():
        text = tk.Label(text = element)  # Créer un Label avec les informations du visiteur
        text.configure(bg='#3399FF')
        text.place(x=200, y=y_position)  # Placer le Label dans la fenêtre
        y_position += 30

def zone_texte_visi_num():
    effacer_label()
    effacer_texte()
    global zone_visiteur_num
    zone_visiteur_num = tk.Entry()
    zone_visiteur_num.pack()
    fenetre.bind("<Return>", rechercher_visiteur_num) #lorsque la touche "entrée" du clavier est actionné, c'est la fonction rechercher_visiteur_num qui s'exécute

def rechercher_visiteur_num():
    effacer_label()
    y_position = 10
    for element in main.admin.search_visiteur():
        text = tk.Label(text = element)  # Créer un Label avec les informations du visiteur
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

interface_principale()
fenetre.mainloop()