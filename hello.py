import tkinter as tk
import main

# Créer la fenêtre principale
fenetre = tk.Tk()
fenetre.title("Gestion des JO")
fenetre.configure(bg='#f4fefe')
fenetre.geometry("1000x500")
fenetre.maxsize(1000,500)
fenetre.minsize(1000,500)

#Petites fonctions initiales qui vont simplifier notre code
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
    effacer_texte()
    cadre_bouton_athlete = tk.Frame(fenetre)
    cadre_bouton_athlete.pack(side="left", fill="x", expand=True)
    cadre_bouton_athlete.configure(bg ='#f4fefe')
    cadre_bouton_visiteur = tk.Frame(fenetre)
    cadre_bouton_visiteur.pack(side="right", fill="x", expand=True)
    cadre_bouton_visiteur.configure(bg = '#f4fefe')
    cadre_bouton_retour = tk.Frame(fenetre, width=100, height=100, bg='green')
    cadre_bouton_retour.place(x=0, y=500, anchor='sw')

    # on créer et place deux boutons initiaux au centre
    creer_bouton(cadre_bouton_athlete, "Athlètes", afficher_interface_athlete, 20, 10, '#5FD4EE','Tw Cen MT',20)
    creer_bouton(cadre_bouton_visiteur, "Visiteurs", afficher_interface_visiteur, 20, 10, '#EE5F5F','Tw Cen MT',20)
    creer_bouton(cadre_bouton_retour, "Quitter", fenetre.destroy, 5, 1, '#b50000' , 'Tw Cen MT',20)

def afficher_interface_athlete():
    # on supprimer les boutons initiaux
    effacer_fenetre()
    effacer_label()
    effacer_texte()

    ###################################### CADRE BOUTON RETOUR ############################################################
    cadre_bouton_retour1 = tk.Frame(fenetre, width=100, height=100, bg='grey')
    cadre_bouton_retour1.place(x=0, y=500, anchor='sw') #anchor sert a superpositionner ce bouton au dessus du cadre gauche
    #On créer le bouton retour
    creer_bouton(cadre_bouton_retour1, "Retour", interface_principale, 5, 1, '#b50000' , 'Tw Cen MT',20)

    ###################################### CADRE GAUCHE ##################################################################
    cadre_gauche = tk.Frame(fenetre, bg='#cbd4d4')
    cadre_gauche.pack(side="left", fill="y") #fill=y pour créer un cadre a gauche de haut en bas et pour fill=x un cadre à gauche en haut
    # on ajouter les boutons au Frame de gauche
    creer_bouton(cadre_gauche, "Afficher tous les athlètes", afficher_athlete, 20, 2, '#9ef0f6','Tw Cen MT',12)
    creer_bouton(cadre_gauche, "Rechercher un athlète", zone_texte_ath, 20, 2, '#6ecaf2','Tw Cen MT',12)
    creer_bouton(cadre_gauche, "Afficher par pays", zone_texte_pays, 20, 2,'#2969eb','Tw Cen MT',12)
    creer_bouton(cadre_gauche, "Afficher par discipline", zone_texte_dis, 20, 2, '#0a55ea','Tw Cen MT',12)
    creer_bouton(cadre_gauche, "Afficher par récompense", zone_texte_rec, 20, 2, '#0b49c3','Tw Cen MT',12)
    
    ###################################### CADRE DU MILIEU ##################################################################
#    cadre_milieu_ath = tk.Frame(fenetre,bg='#ffffff')
#    cadre_milieu_ath.pack(expand=True, fill="both") 
    # On ajoute un canvas dans ce cadre du milieu (utilise ce widjet pour prendre en charge le défilement si le contenu dépasse ses dimensions visibles)
#    global canvas_milieu_ath
#    canvas_milieu_ath = tk.Canvas(cadre_milieu_ath)
#    canvas_milieu_ath.pack(side="left", expand=True, fill="both")
#    # on ajoute une barre de défilement pour le canvas
#    scrollbar = tk.Scrollbar(cadre_milieu_ath, orient="vertical", command=canvas_milieu_ath.yview)
#    scrollbar.pack(side="right", fill="y")
#    canvas_milieu_ath.configure(yscrollcommand=scrollbar.set)
#    # On ajouter un autre cadre dans le Canvas pour contenir les éléments que vous souhaitez afficher
#    global frame_interieur_ath
#    frame_interieur_ath = tk.Frame(canvas_milieu_ath)
#    canvas_milieu_ath.create_window((0, 0), window=frame_interieur_ath, anchor="nw")
#    frame_interieur_ath.bind("<Configure>", canvas_configure_ath)

    ###################################### CADRE DE DROITE ##################################################################
    cadre_droit = tk.Frame(fenetre,bg='#cbd4d4')
    cadre_droit.pack(side="right", fill="y")
    # on jouter les boutons au Frame de droite
    creer_bouton(cadre_droit, "Ajouter un athlète", zone_texte_ajout_ath, 20, 2,'#9ef0f6','Tw Cen MT',12)
    creer_bouton(cadre_droit, "Supprimer un athlète", zone_texte_suppr_ath, 20, 2,'#6ecaf2','Tw Cen MT',12)
    creer_bouton(cadre_droit, "Modifier une récompense", zone_texte_recompense, 20, 2,'#2969eb','Tw Cen MT',12)

    # permet de placer le cadre cadre_bouton_retour1 au premier plan
    cadre_bouton_retour1.lift() 

#def canvas_configure_ath(event=None):                    # cette fonction sera appelé lorsque la taille du widjet changera
#    canvas_milieu_ath.configure(scrollregion=canvas_milieu_ath.bbox("all"))# pour que le canva puisse prendre en charge le défilement pour tous les objets
                                                                                 # (bbox) renvoie les coordonnées de tous les objets dans le canvas


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
    creer_bouton(cadre_gauche, "Rechercher par une identité", zone_texte_visi_nom, 20, 2, '#ff3f3f','Tw Cen MT',11)
    creer_bouton(cadre_gauche, "Rechercher par un numéro", zone_texte_visi_num, 20, 2,'#ff0000','Tw Cen MT',12)

    # Créer un Frame à droite pour les boutons de droite
    cadre_droit = tk.Frame(fenetre,bg='#cbd4d4')
    cadre_droit.pack(side="right", fill="both")
    # Ajouter les boutons au Frame de droite
    creer_bouton(cadre_droit, "Ajouter un visiteur", zone_texte_ajout_visiteur,20,2, '#ff7070','Tw Cen MT',12)
    creer_bouton(cadre_droit, "Supprimer un visiteur", zone_texte_suppr_visiteur,20,2, '#ff3f3f','Tw Cen MT',12)
    creer_bouton(fenetre=cadre_droit, texte="",commande=None, largeur=20, hauteur=2, couleur='#cbd4d4',police='Tw Cen MT',taille=12)
    creer_bouton(cadre_droit, "Afficher la map", afficher_athlete, 20, 2, '#00ff73','Tw Cen MT',12)

    cadre_bouton_retour2.lift() # permet de placer le cadre cadre_bouton_retour1 au premier plan

#Définition des fonctions:
def afficher_athlete():
    effacer_label()
    effacer_texte()
    y_position = 10
    for lignes in main.admin.show_athlete():
        athlete_info = tk.Label(fenetre,text = lignes, bg='#3399FF',font=("Tw Cent MT",13))  # Créer un Label avec les informations de l'athlète
        athlete_info.place(x=200, y=y_position)  # Placer le Label dans la fenêtre
        y_position += 30

def afficher_visiteur():
    effacer_label()
    effacer_texte()
    y_position = 10
    for lignes in main.admin.show_visiteur():
        visiteur_info = tk.Label(text = lignes, bg='#3399FF',font=("Tw Cent MT",13))  # Créer un Label avec les informations du visiteur
        visiteur_info.place(x=200, y=y_position)  # Placer le Label dans la fenêtre
        y_position += 30

################################################################################################################################################
##################################### CREATION DES ENTRY ET FONCTIONS DU BOUTON: << Rechercher un athlète >> ###################################
################################################################################################################################################

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
    fenetre.bind("<Return>", rechercher_athlete) #lorsque la touche "entrée" du clavier est actionné, c'est la fonction rechercher_athlete qui s'exécute

def rechercher_athlete(event=None):
    effacer_label()
    Nom=zone_ath_nom.get()
    NOM=Nom.upper()
    prénom=zone_ath_prenom.get()
    Prénom=prénom.capitalize()
    ENTREE=NOM+" "+Prénom
    #print (ENTREE)
    if NOM!="NOM" and Prénom!="Prénom":
        SORTIE=main.admin.search_athlete(ENTREE)
        if SORTIE=="ERREUR": #on test si cette personne est bien dans notre dico athlete
            erreur_1 = tk.Label(text = "Réessayer cet(te) athlète ne participe pas aux jeux !", bg='#3399FF',font=("Tw Cent MT",13))  # Créer un Label avec le message d'erreur
            erreur_1.place(x=400, y=50)  
        else:
            athlete_info = tk.Label(text = SORTIE, bg='#3399FF',font=("Tw Cent MT",13))  # Créer un Label avec les informations de l'athlète
            athlete_info.place(x=400, y=50)  # Placer le Label dans la fenêtre
    else:
        erreur_2 = tk.Label(text = "Votre saisie est incomplète, réessayer !", bg='#3399FF',font=("Tw Cent MT",13)) #Créer un Label avec du texte d'erreur comme quoi il n'a pas tout renseigner
        erreur_2.place(x=200, y=100)  # Placer le Label dans la fenêtre

################################################################################################################################################
##################################### CREATION DES ENTRY ET FONCTIONS DU BOUTON: << Afficher par pays >> #######################################
################################################################################################################################################

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
    zone_pays.bind("<FocusIn>", retire_justi_pays)#le focus, c-a-d lorsque l'utilisateur commence à taper dans l'entrée
    zone_pays.pack()
    fenetre.bind("<Return>", rechercher_pays) #lorsque la touche "entrée" du clavier est actionné, c'est la fonction rechercher_pays qui s'exécute

def rechercher_pays(event=None):
    effacer_label()
    entree=zone_pays.get()
    ENTREE=entree.upper()
    y_position = 50
    if ENTREE!="PAYS":
        SORTIE=main.admin.search_pays(ENTREE)
        if SORTIE=="ERREUR": #on test si le pays rentré est bien dans les jeux
            erreur_1 = tk.Label(text = "Réessayer ce pays ne participe pas aux jeux !", bg='#3399FF',font=("Tw Cent MT",13))  # Créer un Label avec le message d'erreur
            erreur_1.place(x=400, y=50)   
        else:
            for lignes in SORTIE:
                athlete_infos = tk.Label(text = lignes, bg='#3399FF',font=("Tw Cent MT",13))  # Créer un Label avec les informations de l'athlète
                athlete_infos.place(x=200, y=y_position)  # Place le Label dans la fenêtre
                y_position += 30
    else:
        erreur_2 = tk.Label(text = "Votre saisie est incomplète, réessayer !", bg='#3399FF',font=("Tw Cent MT",13)) #Créer un Label avec du texte d'erreur comme quoi il n'a pas tout renseigner
        erreur_2.place(x=200, y=100)  # Placer le Label dans la fenêtre

################################################################################################################################################
##################################### CREATION DES ENTRY ET FONCTIONS DU BOUTON: << Afficher par récompense >> #######################################
################################################################################################################################################

def retire_justi_rec(event=None):
    if zone_rec.get() == "Médaille":
        zone_rec.delete(0,'end')#les parametres sont les positions des caractères à retirer, ici du débu (0) à la fin ("end")
        zone_rec.config(fg="Black",font=("Tw Cent Mt",13))

def zone_texte_rec():
    effacer_label()
    effacer_texte()
    global zone_rec
    zone_rec = tk.Entry(fg="gray",font=("Tw Cent Mt",13))
    zone_rec.insert(0,"Médaille")
    zone_rec.bind("<FocusIn>", retire_justi_rec)#le focus, c-a-d lorsque l'utilisateur commence à taper dans l'entrée
    zone_rec.pack()
    fenetre.bind("<Return>", rechercher_recompense) #lorsque la touche "entrée" du clavier est actionné, c'est la fonction rechercher_recompense qui s'exécute

def rechercher_recompense(event=None):
    effacer_label()
    entree=zone_rec.get()
    Entrée=entree.capitalize()
    y_position = 50
    if Entrée!="Médaille":
        SORTIE=main.admin.search_recompense(Entrée)
        if SORTIE=="ERREUR": #on test si la récompense rentré existe bien
            erreur_1 = tk.Label(text = "Réessayer, cette récompense n'existe pas !", bg='#3399FF',font=("Tw Cent MT",13))  # Créer un Label avec le message d'erreur
            erreur_1.place(x=400, y=50)   
        else:
            for lignes in SORTIE:
                athlete_infos = tk.Label(text = lignes, bg='#3399FF',font=("Tw Cent MT",13))  # Créer un Label avec les informations de l'athlète
                athlete_infos.place(x=200, y=y_position)  # Place le Label dans la fenêtre
                y_position += 30
    else:
        erreur_2 = tk.Label(text = "Votre saisie est incomplète, réessayer !", bg='#3399FF',font=("Tw Cent MT",13)) #Créer un Label avec du texte d'erreur comme quoi il n'a pas tout renseigner
        erreur_2.place(x=200, y=100)  # Placer le Label dans la fenêtre

################################################################################################################################################
##################################### CREATION DES ENTRY ET FONCTIONS DU BOUTON: << Afficher par discipline >> #################################
################################################################################################################################################

def retire_justi_dis(event=None):
    if zone_dis.get() == "DISCIPLINE":
        zone_dis.delete(0,'end')#les parametres sont les positions des caractères à retirer, ici du débu (0) à la fin ("end")
        zone_dis.config(fg="Black",font=("Tw Cent Mt",13))

def zone_texte_dis():
    effacer_label()
    effacer_texte()
    global zone_dis
    zone_dis = tk.Entry(fg="gray",font=("Tw Cent Mt",13))
    zone_dis.insert(0,"DISCIPLINE")
    zone_dis.bind("<FocusIn>", retire_justi_dis)#le focus, c-a-d lorsque l'utilisateur commence à taper dans l'entrée
    zone_dis.pack()
    fenetre.bind("<Return>", rechercher_dis) #lorsque la touche "entrée" du clavier est actionné, c'est la fonction rechercher_dis qui s'exécute

def rechercher_dis(event=None):
    effacer_label()
    entree=zone_dis.get().replace(" ","_")
    ENTREE=entree.upper()
    y_position = 50
    if ENTREE!="DISCIPLINE":
        SORTIE=main.admin.search_dis(ENTREE)
        if SORTIE=="ERREUR": #on test si la discipline rentrée est bien dans les jeux
            erreur_1 = tk.Label(text = "Réessayer cette discipline n'est pas présente aux jeux !", bg='#3399FF',font=("Tw Cent MT",13))  # Créer un Label avec le message d'erreur
            erreur_1.place(x=400, y=50)   
        else:
            for lignes in SORTIE:
                athlete_infos = tk.Label(text = lignes, bg='#3399FF',font=("Tw Cent MT",13))  # Créer un Label avec les informations de l'athlète
                athlete_infos.place(x=200, y=y_position)  # Place le Label dans la fenêtre
                y_position += 30
    else:
        erreur_2 = tk.Label(text = "Votre saisie est incomplète, réessayer !", bg='#3399FF',font=("Tw Cent MT",13)) #Créer un Label avec du texte d'erreur comme quoi il n'a pas tout renseigner
        erreur_2.place(x=200, y=100)  # Placer le Label dans la fenêtre

################################################################################################################################################
##################################### CREATION DES ENTRY ET FONCTIONS DU BOUTON: << Rechercher par identité >> #################################
################################################################################################################################################

def retire_justi_visiteur_nom(event=None):
    if zone_visiteur_nom.get() == "NOM":
        zone_visiteur_nom.delete(0,'end')#les parametres sont les positions des caractères à retirer, ici du débu (0) à la fin ("end")
        zone_visiteur_nom.config(fg="Black",font=("Tw Cent Mt",13))

def remise_justi_visiteur_nom(event=None):
    if zone_visiteur_nom.get() == "":
        zone_visiteur_nom.insert(0,"NOM")
        zone_visiteur_nom.config(fg="gray",font=("Tw Cent Mt",13))

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

def rechercher_visiteur_nom(event=None):
    effacer_label()
    Nom=zone_visiteur_nom.get()
    NOM=Nom.upper()
    prénom=zone_visiteur_prenom.get()
    Prénom=prénom.capitalize()
    ENTREE=NOM+" "+Prénom
    if NOM!="NOM" and Prénom!="Prénom":
        SORTIE=main.admin.search_visiteur_nom(ENTREE)
        if SORTIE=="ERREUR": #on test si cette personne est bien dans notre dico athlete
            erreur_1 = tk.Label(text = "Ce visiteur n'est pas enregistré pour ces jeux !"+"\n", bg='#3399FF',font=("Tw Cent MT",13))  # Créer un Label avec le message d'erreur
            erreur_1.place(x=400, y=60)
            redirection = tk.Label(text = "Pour vous enregistrer et obtenir votre ticket, cliquer sur le bouton << Ajouter un visiteur >>", bg='#3399FF',font=("Tw Cent MT",13))  # Créer un Label avec le message de redirection
            redirection.place(x=170, y=90)
        else:
            visiteur_info = tk.Label(text = SORTIE, bg='#3399FF',font=("Tw Cent MT",14))  # Créer un Label avec les informations de l'athlète
            visiteur_info.place(x=400, y=50)  # Placer le Label dans la fenêtre
    else:
        erreur_2 = tk.Label(text = "Votre saisie est incomplète, réessayer !", bg='#3399FF',font=("Tw Cent MT",13)) #Créer un Label avec du texte d'erreur comme quoi il n'a pas tout renseigner
        erreur_2.place(x=200, y=100)  # Placer le Label dans la fenêtre

################################################################################################################################################
##################################### CREATION DES ENTRY ET FONCTIONS DU BOUTON: << Rechercher par numéro >> ###################################
################################################################################################################################################

def retire_justi_visiteur_num(event=None):
    if zone_visiteur_num.get() == "NUMERO DU BILLET":
        zone_visiteur_num.delete(0,'end')#les parametres sont les positions des caractères à retirer, ici du débu (0) à la fin ("end")
        zone_visiteur_num.config(fg="Black",font=("Tw Cent Mt",13))

def zone_texte_visi_num():
    effacer_label()
    effacer_texte()
    global zone_visiteur_num
    zone_visiteur_num = tk.Entry(fg="gray",font=("Tw Cent Mt",13))
    zone_visiteur_num.insert(0,"NUMERO DU BILLET")
    zone_visiteur_num.bind("<FocusIn>", retire_justi_visiteur_num)#le focus, c-a-d lorsque l'utilisateur commence à taper dans l'entrée
    zone_visiteur_num.pack()
    fenetre.bind("<Return>", rechercher_visiteur_num) #lorsque la touche "entrée" du clavier est actionné, c'est la fonction rechercher_visiteur_num qui s'exécute

def rechercher_visiteur_num(event=None):
    effacer_label()
    ENTREE=zone_visiteur_num.get()
    if ENTREE!="NUMERO DU BILLET":
        SORTIE=main.admin.search_visiteur_num(ENTREE)
        if SORTIE=="ERREUR": #on test si le numéro rentré est bien recenser
            erreur_1 = tk.Label(text = "Ce visiteur n'est pas enregistré pour ces jeux !"+"\n", bg='#3399FF',font=("Tw Cent MT",13))  # Créer un Label avec le message d'erreur
            erreur_1.place(x=400, y=60)
            redirection = tk.Label(text = "Pour vous enregistrer et obtenir votre ticket, cliquer sur le bouton << Ajouter un visiteur >>", bg='#3399FF',font=("Tw Cent MT",13))  # Créer un Label avec le message de redirection
            redirection.place(x=170, y=90) 
        else:
            athlete_infos = tk.Label(text = SORTIE, bg='#3399FF',font=("Tw Cent MT",14))  # Créer un Label avec les informations de l'athlète
            athlete_infos.place(x=200, y=70)  # Place le Label dans la fenêtre
    else:
        erreur_2 = tk.Label(text = "Votre saisie est incomplète, réessayer !", bg='#3399FF',font=("Tw Cent MT",13)) #Créer un Label avec du texte d'erreur comme quoi il n'a pas tout renseigner
        erreur_2.place(x=200, y=100)  # Placer le Label dans la fenêtre

################################################################################################################################################
##################################### CREATION DES ENTRY ET FONCTIONS DU BOUTON: << Ajouter un athlète >> ######################################
################################################################################################################################################

def retire_justi_ajout_ath_nom(event=None):
    if zone_ajout_ath_nom.get() == "NOM":
        zone_ajout_ath_nom.delete(0,'end')#les parametres sont les positions des caractères à retirer, ici du début (0) à la fin ("end")
        zone_ajout_ath_nom.config(fg="Black",font=("Tw Cent Mt",13))

def remise_justi_ajout_ath_nom(event=None):
    if zone_ajout_ath_nom.get() == "":
        zone_ajout_ath_nom.insert(0,"NOM")
        zone_ajout_ath_nom.config(fg="gray",font=("Tw Cent Mt",13))

def retire_justi_ajout_ath_prenom(event=None):
    if zone_ajout_ath_prenom.get() == "Prénom":
        zone_ajout_ath_prenom.delete(0,'end')#les parametres sont les positions des caractères à retirer, ici du débu (0) à la fin ("end")
        zone_ajout_ath_prenom.config(fg="Black",font=("Tw Cent Mt",13))

def remise_justi_ajout_ath_prenom(event=None):
    if zone_ajout_ath_prenom.get() == "":
        zone_ajout_ath_prenom.insert(0,"Prénom")
        zone_ajout_ath_prenom.config(fg="gray",font=("Tw Cent Mt",13))

def retire_justi_ajout_ath_naissance(event=None):
    if zone_ajout_ath_naissance.get() == "Date de naissance: AAAA-MM-JJ":
        zone_ajout_ath_naissance.delete(0,'end')#les parametres sont les positions des caractères à retirer, ici du débu (0) à la fin ("end")
        zone_ajout_ath_naissance.config(fg="Black",font=("Tw Cent Mt",13))

def remise_justi_ajout_ath_naissance(event=None):
    if zone_ajout_ath_naissance.get() == "":
        zone_ajout_ath_naissance.insert(0,"Date de naissance: AAAA-MM-JJ")
        zone_ajout_ath_naissance.config(fg="gray",font=("Tw Cent Mt",13))

def retire_justi_ajout_ath_pays(event=None):
    if zone_ajout_ath_pays.get() == "PAYS":
        zone_ajout_ath_pays.delete(0,'end')#les parametres sont les positions des caractères à retirer, ici du débu (0) à la fin ("end")
        zone_ajout_ath_pays.config(fg="Black",font=("Tw Cent Mt",13))

def remise_justi_ajout_ath_pays(event=None):
    if zone_ajout_ath_pays.get() == "":
        zone_ajout_ath_pays.insert(0,"PAYS")
        zone_ajout_ath_pays.config(fg="gray",font=("Tw Cent Mt",13))

def retire_justi_ajout_ath_dis(event=None):
    if zone_ajout_ath_dis.get() == "DISCIPLINE":
        zone_ajout_ath_dis.delete(0,'end')#les parametres sont les positions des caractères à retirer, ici du débu (0) à la fin ("end")
        zone_ajout_ath_dis.config(fg="Black",font=("Tw Cent Mt",13))

def remise_justi_ajout_ath_dis(event=None):
    if zone_ajout_ath_dis.get() == "":
        zone_ajout_ath_dis.insert(0,"DISCIPLINE")
        zone_ajout_ath_dis.config(fg="gray",font=("Tw Cent Mt",13))

#Création des zones textes pour demandé les différentes entrées à l'utilisateur
def zone_texte_ajout_ath():
    effacer_label()
    effacer_texte()
    global zone_ajout_ath_nom
    zone_ajout_ath_nom = tk.Entry(fg="gray",font=("Tw Cent Mt",13),width=30) #on augmente le nombre de caractère que la barre peut afficher
    zone_ajout_ath_nom.insert(0,"NOM")
    zone_ajout_ath_nom.bind("<FocusIn>", retire_justi_ajout_ath_nom) #le focus, c-a-d lorsque l'utilisateur commence à taper dans l'entrée
    zone_ajout_ath_nom.bind("<FocusOut>", remise_justi_ajout_ath_nom) #perd le focus, c-a-d lorsque l'utilisateur cesse de taper dans l'entrée ou passe à un autre widget ou quitte la fenêtre
    zone_ajout_ath_nom.pack()
    global zone_ajout_ath_prenom
    zone_ajout_ath_prenom = tk.Entry(fg="gray",font=("Tw Cent Mt",13),width=30)
    zone_ajout_ath_prenom.insert(0,"Prénom")
    zone_ajout_ath_prenom.bind("<FocusIn>", retire_justi_ajout_ath_prenom)
    zone_ajout_ath_prenom.bind("<FocusOut>", remise_justi_ajout_ath_prenom)
    zone_ajout_ath_prenom.pack()
    global zone_ajout_ath_naissance
    zone_ajout_ath_naissance = tk.Entry(fg="gray",font=("Tw Cent Mt",13),width=30)#on augmente le nombre de caractère que la barre peut afficher
    zone_ajout_ath_naissance.insert(0,"Date de naissance: AAAA-MM-JJ")
    zone_ajout_ath_naissance.bind("<FocusIn>", retire_justi_ajout_ath_naissance) 
    zone_ajout_ath_naissance.bind("<FocusOut>", remise_justi_ajout_ath_naissance) 
    zone_ajout_ath_naissance.pack()
    global zone_ajout_ath_pays
    zone_ajout_ath_pays = tk.Entry(fg="gray",font=("Tw Cent Mt",13),width=30)
    zone_ajout_ath_pays.insert(0,"PAYS")
    zone_ajout_ath_pays.bind("<FocusIn>", retire_justi_ajout_ath_pays) 
    zone_ajout_ath_pays.bind("<FocusOut>", remise_justi_ajout_ath_pays) 
    zone_ajout_ath_pays.pack()
    global zone_ajout_ath_dis
    zone_ajout_ath_dis = tk.Entry(fg="gray",font=("Tw Cent Mt",13),width=30)# ici on précise width=30 pour que date de naissance soit totalement afficher
    zone_ajout_ath_dis.insert(0,"DISCIPLINE")
    zone_ajout_ath_dis.bind("<FocusIn>", retire_justi_ajout_ath_dis)
    zone_ajout_ath_dis.bind("<FocusOut>", remise_justi_ajout_ath_dis) 
    zone_ajout_ath_dis.pack()

    fenetre.bind("<Return>", ajout_athlete) #lorsque la touche "entrée" du clavier est actionné, c'est la fonction ajout_athlete qui s'exécute

def ajout_athlete(event=None):
    effacer_label()
    Nom=zone_ajout_ath_nom.get()
    NOM=Nom.upper()
    prénom=zone_ajout_ath_prenom.get()
    Prénom=prénom.capitalize() #pour transformer la chaine de caractère en minuscule et seulement le premier en MAJ
    Naissance=zone_ajout_ath_naissance.get()
    Pays=zone_ajout_ath_pays.get().replace(" ","_") #pour ne pas avoir de problèmes avec les espaces avec la méthode .replace()
    PAYS=Pays.upper() #pour ne pas avoir le problème des majuscules 
    Discipline=zone_ajout_ath_dis.get().replace(" ","_")
    DISCIPLINE=Discipline.upper()
    try:                          # on fait une petite condition selon laquelle si la fonction échoue alors on affiche un message d'erreur
        if NOM!="NOM" and Prénom!="Prénom" and Naissance!="Date de naissance: AAAA-MM-JJ" and PAYS!="PAYS" and DISCIPLINE!="DISCIPLINE":
            main.admin.ad_athlete(NOM,Prénom,Naissance,PAYS,DISCIPLINE)#on exécute l'ajout de l'athlète grâce à la fonction ad_athlete défini dans le main
            texte_affichage="L'athlète "+str(NOM)+" "+str(Prénom)+" né le "+str(Naissance)+" est ajouté aux jeux !"
            affichage = tk.Label(text = texte_affichage, bg='#3399FF',font=("Tw Cent MT",13))  # Créer un Label avec du texte pour signifier que l'athlète est bien ajouter
            affichage.place(x=200, y=90)  # Placer le Label dans la fenêtre
        else:
            erreur_1 = tk.Label(text = "Votre saisie est incomplète, réessayer !", bg='#3399FF',font=("Tw Cent MT",13))
            erreur_1.place(x=200, y=100)  # Placer le Label dans la fenêtre

    except Exception:
        erreur_2 = tk.Label(text = "Votre saisie est incorrecte, respecter la mise en forme des entrées !", bg='#3399FF',font=("Tw Cent MT",13))  # Créer un Label avec du texte pour signifier qu'il faut respecter les entry
        erreur_2.place(x=200, y=100)  # Placer le Label dans la fenêtre

################################################################################################################################################
##################################### CREATION DES ENTRY ET FONCTIONS DU BOUTON: << Ajouter un visiteur >> #####################################
################################################################################################################################################

def retire_justi_ajout_visiteur_nom(event=None):
    if zone_ajout_visiteur_nom.get() == "NOM":
        zone_ajout_visiteur_nom.delete(0,'end')#les parametres sont les positions des caractères à retirer, ici du début (0) à la fin ("end")
        zone_ajout_visiteur_nom.config(fg="Black",font=("Tw Cent Mt",13))

def remise_justi_ajout_visiteur_nom(event=None):
    if zone_ajout_visiteur_nom.get() == "":
        zone_ajout_visiteur_nom.insert(0,"NOM")
        zone_ajout_visiteur_nom.config(fg="gray",font=("Tw Cent Mt",13))

def retire_justi_ajout_visiteur_prenom(event=None):
    if zone_ajout_visiteur_prenom.get() == "Prénom":
        zone_ajout_visiteur_prenom.delete(0,'end')#les parametres sont les positions des caractères à retirer, ici du débu (0) à la fin ("end")
        zone_ajout_visiteur_prenom.config(fg="Black",font=("Tw Cent Mt",13))

def remise_justi_ajout_visiteur_prenom(event=None):
    if zone_ajout_visiteur_prenom.get() == "":
        zone_ajout_visiteur_prenom.insert(0,"Prénom")
        zone_ajout_visiteur_prenom.config(fg="gray",font=("Tw Cent Mt",13))

#Création des zones textes pour demandé les différentes entrées à l'utilisateur
def zone_texte_ajout_visiteur():
    effacer_label()
    effacer_texte()
    global zone_ajout_visiteur_nom
    zone_ajout_visiteur_nom = tk.Entry(fg="gray",font=("Tw Cent Mt",13)) 
    zone_ajout_visiteur_nom.insert(0,"NOM")
    zone_ajout_visiteur_nom.bind("<FocusIn>", retire_justi_ajout_visiteur_nom) #le focus, c-a-d lorsque l'utilisateur commence à taper dans l'entrée
    zone_ajout_visiteur_nom.bind("<FocusOut>", remise_justi_ajout_visiteur_nom) #perd le focus, c-a-d lorsque l'utilisateur cesse de taper dans l'entrée ou passe à un autre widget ou quitte la fenêtre
    zone_ajout_visiteur_nom.pack()
    global zone_ajout_visiteur_prenom
    zone_ajout_visiteur_prenom = tk.Entry(fg="gray",font=("Tw Cent Mt",13))
    zone_ajout_visiteur_prenom.insert(0,"Prénom")
    zone_ajout_visiteur_prenom.bind("<FocusIn>", retire_justi_ajout_visiteur_prenom)
    zone_ajout_visiteur_prenom.bind("<FocusOut>", remise_justi_ajout_visiteur_prenom)
    zone_ajout_visiteur_prenom.pack()

    fenetre.bind("<Return>", ajout_visiteur) #lorsque la touche "entrée" du clavier est actionné, c'est la fonction ajout_visiteur qui s'exécute

def ajout_visiteur(event=None):
    effacer_label()
    Nom=zone_ajout_visiteur_nom.get()
    NOM=Nom.upper()
    prénom=zone_ajout_visiteur_prenom.get()
    Prénom=prénom.capitalize() #pour transformer la chaine de caractère en minuscule et seulement le premier en MAJ
    ENTREE=str(NOM)+" "+str(Prénom)
    #print (ENTREE)
    if NOM!="NOM" and Prénom!="Prénom":
        main.admin.ad_visiteur(NOM,Prénom)#on exécute l'ajout de l'athlète grâce à la fonction ad_athlete défini dans le main
        dic_vis=main.admin.ecriture_visiteur()
        texte_affichage_1="Le visiteur "+str(NOM)+" "+str(Prénom)+" est enregistré pour les jeux !"
        affichage_1 = tk.Label(text = texte_affichage_1, bg='#3399FF',font=("Tw Cent MT",13))  # Créer un Label avec du texte pour signifier que le visiteur est bien ajouter
        affichage_1.place(x=200, y=60)  # Placer le Label dans la fenêtre
        texte_affichage_2="Votre numéro de billet personnel est: "+str(dic_vis[ENTREE].numero)
        affichage_2 = tk.Label(text = texte_affichage_2, bg='#3399FF',font=("Tw Cent MT",13))  # Créer un Label avec du texte pour afficher son numéro de billet
        affichage_2.place(x=200, y=90)  # Placer le Label dans la fenêtre
    else:
        erreur = tk.Label(text = "Votre saisie est incomplète, réessayer !", bg='#3399FF',font=("Tw Cent MT",13)) #Créer un Label avec du texte d'erreur comme quoi il n'a pas tout renseigner
        erreur.place(x=200, y=100)  # Placer le Label dans la fenêtre

################################################################################################################################################
##################################### CREATION DES ENTRY ET FONCTIONS DU BOUTON: << Supprimer un visiteur >> #####################################
################################################################################################################################################

def retire_justi_suppr_visiteur_nom(event=None):
    if zone_suppr_visiteur_nom.get() == "NOM":
        zone_suppr_visiteur_nom.delete(0,'end')#les parametres sont les positions des caractères à retirer, ici du début (0) à la fin ("end")
        zone_suppr_visiteur_nom.config(fg="Black",font=("Tw Cent Mt",13))

def remise_justi_suppr_visiteur_nom(event=None):
    if zone_suppr_visiteur_nom.get() == "":
        zone_suppr_visiteur_nom.insert(0,"NOM")
        zone_suppr_visiteur_nom.config(fg="gray",font=("Tw Cent Mt",13))

def retire_justi_suppr_visiteur_prenom(event=None):
    if zone_suppr_visiteur_prenom.get() == "Prénom":
        zone_suppr_visiteur_prenom.delete(0,'end')#les parametres sont les positions des caractères à retirer, ici du débu (0) à la fin ("end")
        zone_suppr_visiteur_prenom.config(fg="Black",font=("Tw Cent Mt",13))

def remise_justi_suppr_visiteur_prenom(event=None):
    if zone_suppr_visiteur_prenom.get() == "":
        zone_suppr_visiteur_prenom.insert(0,"Prénom")
        zone_suppr_visiteur_prenom.config(fg="gray",font=("Tw Cent Mt",13))

#Création des zones textes pour demandé les différentes entrées à l'utilisateur
def zone_texte_suppr_visiteur():
    effacer_label()
    effacer_texte()
    global zone_suppr_visiteur_nom
    zone_suppr_visiteur_nom = tk.Entry(fg="gray",font=("Tw Cent Mt",13)) 
    zone_suppr_visiteur_nom.insert(0,"NOM")
    zone_suppr_visiteur_nom.bind("<FocusIn>", retire_justi_suppr_visiteur_nom) #le focus, c-a-d lorsque l'utilisateur commence à taper dans l'entrée
    zone_suppr_visiteur_nom.bind("<FocusOut>", remise_justi_suppr_visiteur_nom) #perd le focus, c-a-d lorsque l'utilisateur cesse de taper dans l'entrée ou passe à un autre widget ou quitte la fenêtre
    zone_suppr_visiteur_nom.pack()
    global zone_suppr_visiteur_prenom
    zone_suppr_visiteur_prenom = tk.Entry(fg="gray",font=("Tw Cent Mt",13))
    zone_suppr_visiteur_prenom.insert(0,"Prénom")
    zone_suppr_visiteur_prenom.bind("<FocusIn>", retire_justi_suppr_visiteur_prenom)
    zone_suppr_visiteur_prenom.bind("<FocusOut>", remise_justi_suppr_visiteur_prenom)
    zone_suppr_visiteur_prenom.pack()

    fenetre.bind("<Return>", supprimer_visiteur) #lorsque la touche "entrée" du clavier est actionné, c'est la fonction supprimer_visiteur qui s'exécute

def supprimer_visiteur(event=None):
    effacer_label()
    Nom=zone_suppr_visiteur_nom.get()
    NOM=Nom.upper()
    prénom=zone_suppr_visiteur_prenom.get()
    Prénom=prénom.capitalize() #pour transformer la chaine de caractère en minuscule et seulement le premier en MAJ
    #print (ENTREE)
    if NOM!="NOM" and Prénom!="Prénom":
        SORTIE=main.admin.del_visiteur(NOM,Prénom)
        if SORTIE=="ERREUR": #on test si le paus rentré est bien dans les jeux
            erreur_1 = tk.Label(text = "Ce visiteur n'est pas enregistré pour ces jeux !"+"\n", bg='#3399FF',font=("Tw Cent MT",13))  # Créer un Label avec le message d'erreur
            erreur_1.place(x=400, y=60)
            redirection = tk.Label(text = "Pour vous enregistrer et obtenir votre ticket, cliquer sur le bouton << Ajouter un visiteur >>", bg='#3399FF',font=("Tw Cent MT",13))  # Créer un Label avec le message de redirection
            redirection.place(x=170, y=90) 
        else:
            texte_affichage="Le visiteur "+str(NOM)+" "+str(Prénom)+" a annulé son billet pour les jeux !"
            affichage = tk.Label(text = texte_affichage, bg='#3399FF',font=("Tw Cent MT",13))  # Créer un Label avec du texte pour signifier que le visiteur est bien ajouter
            affichage.place(x=200, y=60)  # Placer le Label dans la fenêtre
            
    else:
        erreur_2 = tk.Label(text = "Votre saisie est incomplète, réessayer !", bg='#3399FF',font=("Tw Cent MT",13))  # Créer un Label avec du texte d'erreur comme quoi il n'a pas tout renseigner
        erreur_2.place(x=200, y=100)  # Placer le Label dans la fenêtre

################################################################################################################################################
##################################### CREATION DES ENTRY ET FONCTIONS DU BOUTON: << Supprimer un athlète >> #####################################
################################################################################################################################################

def retire_justi_suppr_ath_nom(event=None):
    if zone_suppr_ath_nom.get() == "NOM":
        zone_suppr_ath_nom.delete(0,'end')#les parametres sont les positions des caractères à retirer, ici du début (0) à la fin ("end")
        zone_suppr_ath_nom.config(fg="Black",font=("Tw Cent Mt",13))

def remise_justi_suppr_ath_nom(event=None):
    if zone_suppr_ath_nom.get() == "":
        zone_suppr_ath_nom.insert(0,"NOM")
        zone_suppr_ath_nom.config(fg="gray",font=("Tw Cent Mt",13))

def retire_justi_suppr_ath_prenom(event=None):
    if zone_suppr_ath_prenom.get() == "Prénom":
        zone_suppr_ath_prenom.delete(0,'end')#les parametres sont les positions des caractères à retirer, ici du débu (0) à la fin ("end")
        zone_suppr_ath_prenom.config(fg="Black",font=("Tw Cent Mt",13))

def remise_justi_suppr_ath_prenom(event=None):
    if zone_suppr_ath_prenom.get() == "":
        zone_suppr_ath_prenom.insert(0,"Prénom")
        zone_suppr_ath_prenom.config(fg="gray",font=("Tw Cent Mt",13))

#Création des zones textes pour demandé les différentes entrées à l'utilisateur
def zone_texte_suppr_ath():
    effacer_label()
    effacer_texte()
    global zone_suppr_ath_nom
    zone_suppr_ath_nom = tk.Entry(fg="gray",font=("Tw Cent Mt",13)) 
    zone_suppr_ath_nom.insert(0,"NOM")
    zone_suppr_ath_nom.bind("<FocusIn>", retire_justi_suppr_ath_nom) #le focus, c-a-d lorsque l'utilisateur commence à taper dans l'entrée
    zone_suppr_ath_nom.bind("<FocusOut>", remise_justi_suppr_ath_nom) #perd le focus, c-a-d lorsque l'utilisateur cesse de taper dans l'entrée ou passe à un autre widget ou quitte la fenêtre
    zone_suppr_ath_nom.pack()
    global zone_suppr_ath_prenom
    zone_suppr_ath_prenom = tk.Entry(fg="gray",font=("Tw Cent Mt",13))
    zone_suppr_ath_prenom.insert(0,"Prénom")
    zone_suppr_ath_prenom.bind("<FocusIn>", retire_justi_suppr_ath_prenom)
    zone_suppr_ath_prenom.bind("<FocusOut>", remise_justi_suppr_ath_prenom)
    zone_suppr_ath_prenom.pack()

    fenetre.bind("<Return>", supprimer_athlete) #lorsque la touche "entrée" du clavier est actionné, c'est la fonction supprimer_athlete qui s'exécute

def supprimer_athlete(event=None):
    effacer_label()
    Nom=zone_suppr_ath_nom.get()
    NOM=Nom.upper()
    prénom=zone_suppr_ath_prenom.get()
    Prénom=prénom.capitalize() #pour transformer la chaine de caractère en minuscule et seulement le premier en MAJ
    #print (ENTREE)
    if NOM!="NOM" and Prénom!="Prénom":
        SORTIE=main.admin.del_athlete(NOM,Prénom)
        if SORTIE=="ERREUR": #on test si le paus rentré est bien dans les jeux
            erreur_1 = tk.Label(text = "Cet athlète ne participe pas à ces jeux !"+"\n", bg='#3399FF',font=("Tw Cent MT",13))  # Créer un Label avec le message d'erreur
            erreur_1.place(x=400, y=60)
        else:
            texte_affichage="L'athlète "+str(NOM)+" "+str(Prénom)+" ne participe plus à ces jeux !"
            affichage = tk.Label(text = texte_affichage, bg='#3399FF',font=("Tw Cent MT",13))  # Créer un Label avec du texte pour signifier que le visiteur est bien ajouter
            affichage.place(x=200, y=60)  # Placer le Label dans la fenêtre
    else:
        erreur_2 = tk.Label(text = "Votre saisie est incomplète, réessayer !", bg='#3399FF',font=("Tw Cent MT",13))  # Créer un Label avec du texte d'erreur comme quoi il n'a pas tout renseigner
        erreur_2.place(x=200, y=100)  # Placer le Label dans la fenêtre

################################################################################################################################################
##################################### CREATION DES ENTRY ET FONCTIONS DU BOUTON: << Modifier une récompense >> #####################################
################################################################################################################################################

def retire_justi_rec_nom(event=None):
    if zone_rec_nom.get() == "NOM":
        zone_rec_nom.delete(0,'end')#les parametres sont les positions des caractères à retirer, ici du début (0) à la fin ("end")
        zone_rec_nom.config(fg="Black",font=("Tw Cent Mt",13))

def remise_justi_rec_nom(event=None):
    if zone_rec_nom.get() == "":
        zone_rec_nom.insert(0,"NOM")
        zone_rec_nom.config(fg="gray",font=("Tw Cent Mt",13))

def retire_justi_rec_prenom(event=None):
    if zone_rec_prenom.get() == "Prénom":
        zone_rec_prenom.delete(0,'end')#les parametres sont les positions des caractères à retirer, ici du débu (0) à la fin ("end")
        zone_rec_prenom.config(fg="Black",font=("Tw Cent Mt",13))

def remise_justi_rec_prenom(event=None):
    if zone_rec_prenom.get() == "":
        zone_rec_prenom.insert(0,"Prénom")
        zone_rec_prenom.config(fg="gray",font=("Tw Cent Mt",13))

def retire_justi_rec_medaille(event=None):
    if zone_rec_medaille.get() == "Médaille (<<Rien>> pour supprimer)":
        zone_rec_medaille.delete(0,'end')#les parametres sont les positions des caractères à retirer, ici du débu (0) à la fin ("end")
        zone_rec_medaille.config(fg="Black",font=("Tw Cent Mt",13))

def remise_justi_rec_medaille(event=None):
    if zone_rec_medaille.get() == "":
        zone_rec_medaille.insert(0,"Médaille (<<Rien>> pour supprimer)")
        zone_rec_medaille.config(fg="gray",font=("Tw Cent Mt",13))

#Création des zones textes pour demandé les différentes entrées à l'utilisateur
def zone_texte_recompense():
    effacer_label()
    effacer_texte()
    global zone_rec_nom
    zone_rec_nom = tk.Entry(fg="gray",font=("Tw Cent Mt",13),width=30)#on augmente le nombre de caractère que la barre peut afficher
    zone_rec_nom.insert(0,"NOM")
    zone_rec_nom.bind("<FocusIn>", retire_justi_rec_nom) #le focus, c-a-d lorsque l'utilisateur commence à taper dans l'entrée
    zone_rec_nom.bind("<FocusOut>", remise_justi_rec_nom) #perd le focus, c-a-d lorsque l'utilisateur cesse de taper dans l'entrée ou passe à un autre widget ou quitte la fenêtre
    zone_rec_nom.pack()
    global zone_rec_prenom
    zone_rec_prenom = tk.Entry(fg="gray",font=("Tw Cent Mt",13),width=30)#on augmente le nombre de caractère que la barre peut afficher
    zone_rec_prenom.insert(0,"Prénom")
    zone_rec_prenom.bind("<FocusIn>", retire_justi_rec_prenom)
    zone_rec_prenom.bind("<FocusOut>", remise_justi_rec_prenom)
    zone_rec_prenom.pack()
    global zone_rec_medaille
    zone_rec_medaille = tk.Entry(fg="gray",font=("Tw Cent Mt",13),width=30)#on augmente le nombre de caractère que la barre peut afficher
    zone_rec_medaille.insert(0,"Médaille (<<Rien>> pour supprimer)")
    zone_rec_medaille.bind("<FocusIn>", retire_justi_rec_medaille)
    zone_rec_medaille.bind("<FocusOut>", remise_justi_rec_medaille)
    zone_rec_medaille.pack()

    fenetre.bind("<Return>", modifier_recompense) #lorsque la touche "entrée" du clavier est actionné, c'est la fonction modifier_recompense qui s'exécute

def modifier_recompense(event=None):
    effacer_label()
    Nom=zone_rec_nom.get()
    NOM=Nom.upper()
    prénom=zone_rec_prenom.get()
    Prénom=prénom.capitalize() #pour transformer la chaine de caractère en minuscule et seulement le premier en MAJ
    médaille=zone_rec_medaille.get()
    Médaille=médaille.capitalize()
    if NOM!="NOM" and Prénom!="Prénom" and Médaille!="Médaille" and (Médaille=="Or" or Médaille=="Argent" or Médaille=="Bronze" or Médaille=="None" or Médaille=="Rien" or Médaille==" "):
        SORTIE=main.admin.update_recompense(NOM,Prénom,Médaille)
        if SORTIE=="ERREUR": #on test si le paus rentré est bien dans les jeux
            erreur_1 = tk.Label(text = "Cet athlète ne participe pas à ces jeux !"+"\n", bg='#3399FF',font=("Tw Cent MT",13))  # Créer un Label avec le message d'erreur
            erreur_1.place(x=400, y=60)
        elif SORTIE=="DEJA LA MEDAILLE":
            erreur_2 = tk.Label(text = "Cet athlète possède déjà cette médaille !"+"\n", bg='#3399FF',font=("Tw Cent MT",13))  # Créer un Label avec le message d'erreur
            erreur_2.place(x=400, y=60)
        elif Médaille=="Or" or Médaille=="Argent":
            texte_affichage_1="L'athlète "+str(NOM)+" "+str(Prénom)+" possède maintenant la médaille d'"+Médaille+" !"
            affichage_1 = tk.Label(text = texte_affichage_1, bg='#3399FF',font=("Tw Cent MT",13))  # Créer un Label avec du texte pour signifier que le visiteur est bien ajouter
            affichage_1.place(x=200, y=60)  # Placer le Label dans la fenêtre
        elif Médaille=="Bronze":
            texte_affichage_2="L'athlète "+str(NOM)+" "+str(Prénom)+" possède maintenant la médaille de Bronze !"
            affichage_2 = tk.Label(text = texte_affichage_2, bg='#3399FF',font=("Tw Cent MT",13))  # Créer un Label avec du texte pour signifier que le visiteur est bien ajouter
            affichage_2.place(x=200, y=60)  # Placer le Label dans la fenêtre
        else:
            texte_affichage="L'athlète "+str(NOM)+" "+str(Prénom)+" ne possède plus de médaille !"
            affichage = tk.Label(text = texte_affichage, bg='#3399FF',font=("Tw Cent MT",13))  # Créer un Label avec du texte pour signifier que le visiteur est bien ajouter
            affichage.place(x=200, y=60)  # Placer le Label dans la fenêtre
    else:
        erreur_3 = tk.Label(text = "Votre saisie est incomplète ou incorrecte, réessayer !", bg='#3399FF',font=("Tw Cent MT",13))  # Créer un Label avec du texte d'erreur comme quoi il n'a pas tout renseigner
        erreur_3.place(x=200, y=100)  # Placer le Label dans la fenêtre

interface_principale()
fenetre.mainloop()
