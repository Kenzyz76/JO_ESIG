import tkinter as tk
import tkinter.font as tkFont
import customtkinter as ctk
from PIL import ImageTk, Image  
import main

# Créer la fenêtre principale
fenetre = tk.Tk()
fenetre.title("Gestion des JO")
fenetre.configure(bg='#f4fefe')
fenetre.iconbitmap("img/logo_jo.ico")
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

def effacer_milieu_ath():
    for child in cadre_scrollbar_ath.winfo_children():
        if isinstance(child, tk.Label):
            child.destroy()
    for child in cadre_scrollbar_ath.winfo_children():
        if isinstance(child, tk.Entry):
            child.destroy()
    cadre_scrollbar_ath._parent_canvas.yview_moveto(0.0) #permet de faire remonter la scrollbar tout en haut

def effacer_infos_milieu_ath():
    for child in cadre_scrollbar_ath.winfo_children():
        if isinstance(child, tk.Label):
            child.destroy()

def effacer_milieu_vis():
    for child in cadre_scrollbar_vis.winfo_children():
        if isinstance(child, tk.Label):
            child.destroy()
    for child in cadre_scrollbar_vis.winfo_children():
        if isinstance(child, tk.Entry):
            child.destroy()
    for child in cadre_scrollbar_vis.winfo_children():
        if isinstance(child, tk.Canvas):
            child.destroy()
    cadre_scrollbar_vis._parent_canvas.yview_moveto(0.0) #permet de faire remonter la scrollbar tout en haut

def effacer_infos_milieu_vis():
    for child in cadre_scrollbar_vis.winfo_children():
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

def rien(event=None):
    pass

def interface_accueil():
    img_accueil = Image.open("img/AccueilJO.jpeg")#on ouvre l'image avec pill pour pas de problème d'objet
    img_accueil = ImageTk.PhotoImage(img_accueil)#on ouvre l'image avec tkinter
    affichage_accueil = tk.Label(fenetre, image=img_accueil, bg="#e7e6e6")
    affichage_accueil.image = img_accueil
    affichage_accueil.pack()
    fenetre.bind("<Return>", interface_principale) #lorsque la touche "entrée" du clavier est actionné, c'est la fonction rechercher_athlete qui s'exécute

def interface_principale(event=None): 
    effacer_fenetre()
    effacer_label()
    effacer_texte()

    img_menu = Image.open("img/MENU.jpeg")#on ouvre l'image avec pill pour pas de problème d'objet
    img_menu = ImageTk.PhotoImage(img_menu)#on ouvre l'image avec tkinter
    affichage_menu = tk.Label(fenetre, image=img_menu)
    affichage_menu.image = img_menu
    affichage_menu.place(x=0,y=0)

    FONT_MENU=tkFont.Font(family="Tw Cen MT",size=25, underline=True)
    affichage_MENU = tk.Label(fenetre,text ="MENU",font=FONT_MENU,bg="#f4fefe")  # Créer un Label avec le nom de l'athlète
    affichage_MENU.pack()  # Placer le Label dans la fenêtre

    cadre_bouton_athlete = tk.Frame(fenetre)
    cadre_bouton_athlete.pack(side="left", fill="x", expand=True)
    cadre_bouton_athlete.configure(bg ='#f4fefe')
    cadre_bouton_visiteur = tk.Frame(fenetre)
    cadre_bouton_visiteur.pack(side="right", fill="x", expand=True)
    cadre_bouton_visiteur.configure(bg = '#f4fefe')
    cadre_bouton_retour = tk.Frame(fenetre, width=100, height=100)
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
                      
    ###################################### CADRE DE DROITE ##################################################################
    cadre_droit = tk.Frame(fenetre,bg='#cbd4d4')
    cadre_droit.pack(side="right", fill="y")
    # on jouter les boutons au Frame de droite
    creer_bouton(cadre_droit, "Ajouter un athlète", zone_texte_ajout_ath, 20, 2,'#9ef0f6','Tw Cen MT',12)
    creer_bouton(cadre_droit, "Supprimer un athlète", zone_texte_suppr_ath, 20, 2,'#6ecaf2','Tw Cen MT',12)
    creer_bouton(cadre_droit, "Modifier une récompense", zone_texte_recompense, 20, 2,'#2969eb','Tw Cen MT',12)

    ###################################### CADRE DU MILIEU ##################################################################
    global cadre_milieu_ath
    cadre_milieu_ath = tk.Frame(fenetre)
    cadre_milieu_ath.pack(expand=True, side="top", fill="both")
    global cadre_scrollbar_ath
    cadre_scrollbar_ath = ctk.CTkScrollableFrame(cadre_milieu_ath, fg_color="#e7e6e6")
    cadre_scrollbar_ath.pack(expand=True, fill="both")

    cadre_bouton_retour1.lift() # permet de placer le cadre cadre_bouton_retour1 au premier plan

def afficher_interface_visiteur():
    # On supprime les boutons initiaux
    effacer_fenetre()
    effacer_label()
    effacer_texte()

    ###################################### CADRE BOUTON RETOUR ############################################################
    cadre_bouton_retour2 = tk.Frame(fenetre, width=100, height=100, bg='grey')
    cadre_bouton_retour2.place(x=0, y=500, anchor='sw')
    #On créer le bouton retour
    creer_bouton(cadre_bouton_retour2, "Retour", interface_principale, 5, 1, '#b50000' , 'Tw Cen MT',20)

    ###################################### CADRE GAUCHE ##################################################################
    cadre_gauche = tk.Frame(fenetre,bg='#cbd4d4')
    cadre_gauche.pack(side="left", fill="y")#fill=y pour créer un cadre a gauche de haut en bas et pour fill=x un cadre à gauche en haut
    # Ajouter les boutons au Frame de gauche
    creer_bouton(cadre_gauche, "Afficher tous les visiteurs", afficher_visiteur, 20,2, '#ff7070','Tw Cen MT',12)
    creer_bouton(cadre_gauche, "Rechercher par une identité", zone_texte_visi_nom, 20, 2, '#ff3f3f','Tw Cen MT',11)
    creer_bouton(cadre_gauche, "Rechercher par un numéro", zone_texte_visi_num, 20, 2,'#ff0000','Tw Cen MT',12)

    ###################################### CADRE DE DROITE ##################################################################
    cadre_droit = tk.Frame(fenetre,bg='#cbd4d4')
    cadre_droit.pack(side="right", fill="both")
    # Ajouter les boutons au Frame de droite
    creer_bouton(cadre_droit, "Ajouter un visiteur", zone_texte_ajout_visiteur,20,2, '#ff7070','Tw Cen MT',12)
    creer_bouton(cadre_droit, "Supprimer un visiteur", zone_texte_suppr_visiteur,20,2, '#ff3f3f','Tw Cen MT',12)
    bouton_visiteur_droit_3=creer_bouton(fenetre=cadre_droit, texte="",commande=rien, largeur=20, hauteur=2, couleur='#cbd4d4',police='Tw Cen MT',taille=12)
    bouton_visiteur_droit_3.config(border=0,activebackground="#cbd4d4")
    creer_bouton(cadre_droit, "Afficher la map", afficher_plan, 20, 2, '#00ff73','Tw Cen MT',12)

    ###################################### CADRE DU MILIEU ##################################################################
    global cadre_milieu_vis
    cadre_milieu_vis = tk.Frame(fenetre)
    cadre_milieu_vis.pack(expand=True, side="top", fill="both")
    global cadre_scrollbar_vis
    cadre_scrollbar_vis = ctk.CTkScrollableFrame(cadre_milieu_vis, fg_color="#e7e6e6")
    cadre_scrollbar_vis.pack(expand=True, fill="both")

    cadre_bouton_retour2.lift() # permet de placer le cadre cadre_bouton_retour1 au premier plan

#Définition des fonctions:
def afficher_plan(event=None):
    effacer_label()
    effacer_milieu_vis()
    effacer_texte()
    cadre_scrollbar_vis.configure(label_text="Afficher map")
    canvas_image = tk.Canvas(cadre_scrollbar_vis, width=600, height=600)
    original_img = Image.open("img/plan_des_jo.jpg")
    resized_img = original_img.resize((600, 500))
    img_carte = ImageTk.PhotoImage(resized_img)
    canvas_image.create_image(0,0,anchor="nw",image=img_carte)
    canvas_image.image = img_carte
    canvas_image.pack()

def afficher_athlete():
    effacer_label()
    effacer_milieu_ath()
    effacer_texte()
    img="img.jpeg"
    cadre_scrollbar_ath.configure(label_text="Afficher tous les athlètes")
    for athlete_infos in main.admin.ecriture_athlete().values():
        NOM=athlete_infos.nom
        Prénom=athlete_infos.prenom
        #DATE=athlete_infos.nais
        PAYS=athlete_infos.pays
        DISCIPLINE=athlete_infos.dis
        REC=athlete_infos.rec

        affichage_NOM = tk.Label(cadre_scrollbar_ath,text = NOM,font=("Tw Cent MT",13),bg="#e7e6e6")  # Créer un Label avec le nom de l'athlète
        affichage_NOM.pack()  # Placer le Label dans la fenêtre
        affichage_Prénom = tk.Label(cadre_scrollbar_ath,text = Prénom,font=("Tw Cent MT",13),bg="#e7e6e6")  # Créer un Label avec le prénom de l'athlète
        affichage_Prénom.pack()  # Placer le Label dans la fenêtre

        img_drapeau = Image.open("img/"+PAYS+".jpeg")#on ouvre l'image avec pill pour pas de problème d'objet
        img_drapeau = ImageTk.PhotoImage(img_drapeau)#on ouvre l'image avec tkinter
        affichage_Pays = tk.Label(cadre_scrollbar_ath, image=img_drapeau, bg="#e7e6e6")
        affichage_Pays.image = img_drapeau
        affichage_Pays.pack()

        affichage_DISCIPLINE = tk.Label(cadre_scrollbar_ath,text = DISCIPLINE,font=("Tw Cent MT",13),bg="#e7e6e6")  # Créer un Label avec la discipline de l'athlète
        affichage_DISCIPLINE.pack()  # Placer le Label dans la fenêtre
        affichage_REC = tk.Label(cadre_scrollbar_ath,text = REC,font=("Tw Cent MT",13),bg="#e7e6e6")  # Créer un Label avec la récompense de l'athlète
        affichage_REC.pack()  # Placer le Label dans la fenêtre
        
        try:
            img_portrait = Image.open("img/"+NOM+"_"+Prénom+".jpeg")#on ouvre l'image avec pill pour pas de problème d'objet
            img_portrait = ImageTk.PhotoImage(img_portrait)#on ouvre l'image avec tkinter
        except FileNotFoundError:
            img_portrait = ImageTk.PhotoImage(Image.open("img/anonymous.jpeg"))

        affichage_portrait = tk.Label(cadre_scrollbar_ath, image=img_portrait, bg="#e7e6e6")
        affichage_portrait.image = img_portrait
        affichage_portrait.pack()

        underscore="_______________________________________________________________"
        affichage_underscore = tk.Label(cadre_scrollbar_ath,text = underscore,font=("Tw Cent MT",13),bg="#e7e6e6")
        affichage_underscore.pack()  # Placer le Label dans la fenêtre"""

def afficher_visiteur():
    effacer_label()
    effacer_milieu_vis()
    effacer_texte()
    cadre_scrollbar_vis.configure(label_text="Afficher tous les visiteurs")
    for visiteur_infos in main.admin.ecriture_visiteur().values():
        NOM=visiteur_infos.nom
        Prénom=visiteur_infos.prenom
        NUMERO=visiteur_infos.numero
        affichage_NOM = tk.Label(cadre_scrollbar_vis,text ="NOM: "+NOM,font=("Tw Cent MT",13),bg="#e7e6e6")  # Créer un Label avec le nom du visiteur
        affichage_NOM.pack()  # Placer le Label dans la fenêtre
        affichage_Prénom = tk.Label(cadre_scrollbar_vis,text ="Prénom: " +Prénom,font=("Tw Cent MT",13),bg="#e7e6e6")  # Créer un Label avec le prénom du visiteur
        affichage_Prénom.pack()  # Placer le Label dans la fenêtre
        affichage_NUMERO = tk.Label(cadre_scrollbar_vis,text ="Numéro du billet: "+NUMERO,font=("Tw Cent MT",13),bg="#e7e6e6")  # Créer un Label avec le numéro de billet du visiteur
        affichage_NUMERO.pack()  # Placer le Label dans la fenêtre

        underscore="_______________________________________________________________"
        affichage_underscore = tk.Label(cadre_scrollbar_vis,text = underscore,font=("Tw Cent MT",13),bg="#e7e6e6")
        affichage_underscore.pack()  # Placer le Label dans la fenêtre"""

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
    effacer_milieu_ath()
    effacer_texte()
    cadre_scrollbar_ath.configure(label_text="Rechercher un athlète")
    global zone_ath_nom
    zone_ath_nom = tk.Entry(cadre_scrollbar_ath,fg="gray",font=("Tw Cent Mt",13))
    zone_ath_nom.insert(0,"NOM")
    zone_ath_nom.bind("<FocusIn>", retire_justi_ath_nom) #le focus, c-a-d lorsque l'utilisateur commence à taper dans l'entrée
    zone_ath_nom.bind("<FocusOut>", remise_justi_ath_nom) #perd le focus, c-a-d lorsque l'utilisateur cesse de taper dans l'entrée ou passe à un autre widget ou quitte la fenêtre
    zone_ath_nom.pack()
    global zone_ath_prenom
    zone_ath_prenom = tk.Entry(cadre_scrollbar_ath,fg="gray",font=("Tw Cent Mt",13))
    zone_ath_prenom.insert(0,"Prénom")
    zone_ath_prenom.bind("<FocusIn>", retire_justi_ath_prenom)
    zone_ath_prenom.bind("<FocusOut>", remise_justi_ath_prenom)
    zone_ath_prenom.pack()
    fenetre.bind("<Return>", rechercher_athlete) #lorsque la touche "entrée" du clavier est actionné, c'est la fonction rechercher_athlete qui s'exécute

def rechercher_athlete(event=None):
    effacer_label()
    effacer_infos_milieu_ath()
    Nom=zone_ath_nom.get()
    NOM=Nom.upper()
    prénom=zone_ath_prenom.get()
    Prénom=prénom.capitalize()
    ENTREE=NOM+" "+Prénom
    if NOM!="NOM" and NOM!="" and Prénom!="Prénom"and Prénom!="" :
        SORTIE=main.admin.search_athlete(ENTREE)
        if SORTIE=="ERREUR": #on test si cette personne est bien dans notre dico athlete
            erreur_1 = tk.Label(cadre_scrollbar_ath,text = "Réessayer cet(te) athlète ne participe pas aux jeux !", bg='#ff3939',font=("Tw Cent MT",13))  # Créer un Label avec le message d'erreur
            erreur_1.pack(pady=25) 
        else:
            PAYS=SORTIE[2]
            #NAISSANCE=SORTIE[3]
            DISCIPLINE=SORTIE[4]
            REC=SORTIE[5]
            if REC==None:
                REC="Pas de médaille"
            affichage_NOM = tk.Label(cadre_scrollbar_ath,text = "NOM: "+NOM,font=("Tw Cent MT",13),bg="#e7e6e6")  # Créer un Label avec le nom de l'athlète
            affichage_NOM.pack()  # Placer le Label dans la fenêtre
            affichage_Prénom = tk.Label(cadre_scrollbar_ath,text = "Prénom: "+Prénom,font=("Tw Cent MT",13),bg="#e7e6e6")  # Créer un Label avec le prénom de l'athlète
            affichage_Prénom.pack()  # Placer le Label dans la fenêtre

            img_drapeau = tk.PhotoImage(file="img/"+PAYS+".jpeg") #on ouvre l'image
            affichage_Pays = tk.Label(cadre_scrollbar_ath, image=img_drapeau,bg="#e7e6e6")
            affichage_Pays.image = img_drapeau  # Gardez une référence à l'objet PhotoImage pour éviter qu'il ne soit supprimé
            affichage_Pays.pack()

            affichage_DISCIPLINE = tk.Label(cadre_scrollbar_ath,text = "DISCIPLINE: "+DISCIPLINE,font=("Tw Cent MT",13),bg="#e7e6e6")  # Créer un Label avec la discipline de l'athlète
            affichage_DISCIPLINE.pack()  # Placer le Label dans la fenêtre
            affichage_REC = tk.Label(cadre_scrollbar_ath,text = "Médaille : "+REC,font=("Tw Cent MT",13),bg="#e7e6e6")  # Créer un Label avec la récompense de l'athlète
            affichage_REC.pack()  # Placer le Label dans la fenêtre
            try:
                    img_portrait = Image.open("img/"+NOM+"_"+Prénom+".jpeg")#on ouvre l'image avec pill pour pas de problème d'objet
                    img_portrait = ImageTk.PhotoImage(img_portrait)#on ouvre l'image avec tkinter
            except FileNotFoundError:
                    img_portrait = ImageTk.PhotoImage(Image.open("img/anonymous.jpeg"))

            affichage_portrait = tk.Label(cadre_scrollbar_ath, image=img_portrait,bg="#e7e6e6")
            affichage_portrait.image = img_portrait  # Gardez une référence à l'objet PhotoImage pour éviter qu'il ne soit supprimé
            affichage_portrait.pack()

    else:
        erreur_2 = tk.Label(cadre_scrollbar_ath,text = "Votre saisie est incomplète, réessayer !", bg='#ff3939',font=("Tw Cent MT",13)) #Créer un Label avec du texte d'erreur comme quoi il n'a pas tout renseigner
        erreur_2.pack(pady=25) # Placer le Label dans la fenêtre

################################################################################################################################################
##################################### CREATION DES ENTRY ET FONCTIONS DU BOUTON: << Afficher par pays >> #######################################
################################################################################################################################################

def retire_justi_pays(event=None):
    if zone_pays.get() == "PAYS":
        zone_pays.delete(0,'end')#les parametres sont les positions des caractères à retirer, ici du débu (0) à la fin ("end")
        zone_pays.config(fg="Black",font=("Tw Cent Mt",13))

def zone_texte_pays():
    effacer_label()
    effacer_milieu_ath()
    effacer_texte()
    cadre_scrollbar_ath.configure(label_text="Afficher par pays")
    global zone_pays
    zone_pays = tk.Entry(cadre_scrollbar_ath,fg="gray",font=("Tw Cent Mt",13))
    zone_pays.insert(0,"PAYS")
    zone_pays.bind("<FocusIn>", retire_justi_pays)#le focus, c-a-d lorsque l'utilisateur commence à taper dans l'entrée
    zone_pays.pack()
    fenetre.bind("<Return>", rechercher_pays) #lorsque la touche "entrée" du clavier est actionné, c'est la fonction rechercher_pays qui s'exécute

def rechercher_pays(event=None):
    effacer_label()
    effacer_infos_milieu_ath()
    entree=zone_pays.get()
    ENTREE=entree.upper()
    if ENTREE!="PAYS" and ENTREE!="":
        SORTIE=main.admin.search_pays(ENTREE)
        if SORTIE=="ERREUR": #on test si le pays rentré est bien dans les jeux
            erreur_1 = tk.Label(cadre_scrollbar_ath,text = "Réessayer ce pays ne participe pas aux jeux !", bg='#ff3939',font=("Tw Cent MT",13))  # Créer un Label avec le message d'erreur
            erreur_1.pack(pady=25)   
        else:
            for lignes in SORTIE:
                NOM=lignes[0]
                Prénom=lignes[1]
                PAYS=lignes[2]
                #DATE=athlete_infos.nais
                DISCIPLINE=lignes[4]
                REC=lignes[5]

                affichage_NOM = tk.Label(cadre_scrollbar_ath,text = NOM,font=("Tw Cent MT",13),bg="#e7e6e6")  # Créer un Label avec le nom de l'athlète
                affichage_NOM.pack()  # Placer le Label dans la fenêtre
                affichage_Prénom = tk.Label(cadre_scrollbar_ath,text = Prénom,font=("Tw Cent MT",13),bg="#e7e6e6")  # Créer un Label avec le prénom de l'athlète
                affichage_Prénom.pack()  # Placer le Label dans la fenêtre

                img_drapeau = Image.open("img/"+PAYS+".jpeg")#on ouvre l'image avec pill pour pas de problème d'objet
                img_drapeau = ImageTk.PhotoImage(img_drapeau)#on ouvre l'image avec tkinter
                affichage_Pays = tk.Label(cadre_scrollbar_ath, image=img_drapeau, bg="#e7e6e6")
                affichage_Pays.image = img_drapeau
                affichage_Pays.pack()

                affichage_DISCIPLINE = tk.Label(cadre_scrollbar_ath,text = DISCIPLINE,font=("Tw Cent MT",13),bg="#e7e6e6")  # Créer un Label avec la discipline de l'athlète
                affichage_DISCIPLINE.pack()  # Placer le Label dans la fenêtre
                affichage_REC = tk.Label(cadre_scrollbar_ath,text = REC,font=("Tw Cent MT",13),bg="#e7e6e6")  # Créer un Label avec la récompense de l'athlète
                affichage_REC.pack()  # Placer le Label dans la fenêtre
                
                try:
                    img_portrait = Image.open("img/"+NOM+"_"+Prénom+".jpeg")#on ouvre l'image avec pill pour pas de problème d'objet
                    img_portrait = ImageTk.PhotoImage(img_portrait)#on ouvre l'image avec tkinter
                except FileNotFoundError:
                    img_portrait = ImageTk.PhotoImage(Image.open("img/anonymous.jpeg"))

                affichage_portrait = tk.Label(cadre_scrollbar_ath, image=img_portrait, bg="#e7e6e6")
                affichage_portrait.image = img_portrait
                affichage_portrait.pack()

                underscore="_______________________________________________________________"
                affichage_underscore = tk.Label(cadre_scrollbar_ath,text = underscore,font=("Tw Cent MT",13),bg="#e7e6e6")
                affichage_underscore.pack()  # Placer le Label dans la fenêtre"""

    else:
        erreur_2 = tk.Label(cadre_scrollbar_ath,text = "Votre saisie est incomplète, réessayer !", bg='#ff3939',font=("Tw Cent MT",13)) #Créer un Label avec du texte d'erreur comme quoi il n'a pas tout renseigner
        erreur_2.pack(pady=25)  # Placer le Label dans la fenêtre

################################################################################################################################################
##################################### CREATION DES ENTRY ET FONCTIONS DU BOUTON: << Afficher par récompense >> #######################################
################################################################################################################################################

def retire_justi_rec(event=None):
    if zone_rec.get() == "Médaille":
        zone_rec.delete(0,'end')#les parametres sont les positions des caractères à retirer, ici du débu (0) à la fin ("end")
        zone_rec.config(fg="Black",font=("Tw Cent Mt",13))

def zone_texte_rec():
    effacer_label()
    effacer_milieu_ath()
    effacer_texte()
    global zone_rec
    cadre_scrollbar_ath.configure(label_text="Afficher par récompense")
    zone_rec = tk.Entry(cadre_scrollbar_ath,fg="gray",font=("Tw Cent Mt",13))
    zone_rec.insert(0,"Médaille")
    zone_rec.bind("<FocusIn>", retire_justi_rec)#le focus, c-a-d lorsque l'utilisateur commence à taper dans l'entrée
    zone_rec.pack()
    fenetre.bind("<Return>", rechercher_recompense) #lorsque la touche "entrée" du clavier est actionné, c'est la fonction rechercher_recompense qui s'exécute

def rechercher_recompense(event=None):
    effacer_label()
    effacer_infos_milieu_ath()
    entree=zone_rec.get()
    Entrée=entree.capitalize()
    if Entrée!="Médaille" and Entrée!="":
        SORTIE=main.admin.search_recompense(Entrée)
        if SORTIE=="ERREUR": #on test si la récompense rentré existe bien
            erreur_1 = tk.Label(cadre_scrollbar_ath,text = "Réessayer, cette récompense n'existe pas !", bg='#ff3939',font=("Tw Cent MT",13))  # Créer un Label avec le message d'erreur
            erreur_1.pack(pady=25)    
        else:
            for lignes in SORTIE:
                NOM=lignes[0]
                Prénom=lignes[1]
                PAYS=lignes[2]
                #DATE=athlete_infos.nais
                DISCIPLINE=lignes[4]
                REC=lignes[5]

                affichage_NOM = tk.Label(cadre_scrollbar_ath,text = NOM,font=("Tw Cent MT",13),bg="#e7e6e6")  # Créer un Label avec le nom de l'athlète
                affichage_NOM.pack()  # Placer le Label dans la fenêtre
                affichage_Prénom = tk.Label(cadre_scrollbar_ath,text = Prénom,font=("Tw Cent MT",13),bg="#e7e6e6")  # Créer un Label avec le prénom de l'athlète
                affichage_Prénom.pack()  # Placer le Label dans la fenêtre

                img_drapeau = Image.open("img/"+PAYS+".jpeg")#on ouvre l'image avec pill pour pas de problème d'objet
                img_drapeau = ImageTk.PhotoImage(img_drapeau)#on ouvre l'image avec tkinter
                affichage_Pays = tk.Label(cadre_scrollbar_ath, image=img_drapeau, bg="#e7e6e6")
                affichage_Pays.image = img_drapeau
                affichage_Pays.pack()

                affichage_DISCIPLINE = tk.Label(cadre_scrollbar_ath,text = DISCIPLINE,font=("Tw Cent MT",13),bg="#e7e6e6")  # Créer un Label avec la discipline de l'athlète
                affichage_DISCIPLINE.pack()  # Placer le Label dans la fenêtre
                affichage_REC = tk.Label(cadre_scrollbar_ath,text = REC,font=("Tw Cent MT",13),bg="#e7e6e6")  # Créer un Label avec la récompense de l'athlète
                affichage_REC.pack()  # Placer le Label dans la fenêtre
                
                try:
                    img_portrait = Image.open("img/"+NOM+"_"+Prénom+".jpeg")#on ouvre l'image avec pill pour pas de problème d'objet
                    img_portrait = ImageTk.PhotoImage(img_portrait)#on ouvre l'image avec tkinter
                except FileNotFoundError:
                    img_portrait = ImageTk.PhotoImage(Image.open("img/anonymous.jpeg"))

                affichage_portrait = tk.Label(cadre_scrollbar_ath, image=img_portrait, bg="#e7e6e6")
                affichage_portrait.image = img_portrait
                affichage_portrait.pack()

                underscore="_______________________________________________________________"
                affichage_underscore = tk.Label(cadre_scrollbar_ath,text = underscore,font=("Tw Cent MT",13),bg="#e7e6e6")
                affichage_underscore.pack()  # Placer le Label dans la fenêtre"""

    else:
        erreur_2 = tk.Label(cadre_scrollbar_ath,text = "Votre saisie est incomplète, réessayer !", bg='#ff3939',font=("Tw Cent MT",13)) #Créer un Label avec du texte d'erreur comme quoi il n'a pas tout renseigner
        erreur_2.pack(pady=25)  # Placer le Label dans la fenêtre

################################################################################################################################################
##################################### CREATION DES ENTRY ET FONCTIONS DU BOUTON: << Afficher par discipline >> #################################
################################################################################################################################################

def retire_justi_dis(event=None):
    if zone_dis.get() == "DISCIPLINE":
        zone_dis.delete(0,'end')#les parametres sont les positions des caractères à retirer, ici du débu (0) à la fin ("end")
        zone_dis.config(fg="Black",font=("Tw Cent Mt",13))

def zone_texte_dis():
    effacer_label()
    effacer_milieu_ath()
    effacer_texte()
    cadre_scrollbar_ath.configure(label_text="Afficher par discipline")
    global zone_dis
    zone_dis = tk.Entry(cadre_scrollbar_ath,fg="gray",font=("Tw Cent Mt",13))
    zone_dis.insert(0,"DISCIPLINE")
    zone_dis.bind("<FocusIn>", retire_justi_dis)#le focus, c-a-d lorsque l'utilisateur commence à taper dans l'entrée
    zone_dis.pack()
    fenetre.bind("<Return>", rechercher_dis) #lorsque la touche "entrée" du clavier est actionné, c'est la fonction rechercher_dis qui s'exécute

def rechercher_dis(event=None):
    effacer_label()
    effacer_infos_milieu_ath()
    entree=zone_dis.get().replace(" ","_")
    ENTREE=entree.upper()
    if ENTREE!="DISCIPLINE" and ENTREE!="":
        SORTIE=main.admin.search_dis(ENTREE)
        if SORTIE=="ERREUR": #on test si la discipline rentrée est bien dans les jeux
            erreur_1 = tk.Label(cadre_scrollbar_ath,text = "Réessayer cette discipline n'est pas présente aux jeux !", bg='#ff3939',font=("Tw Cent MT",13))  # Créer un Label avec le message d'erreur
            erreur_1.pack(pady=25)   
        else:
            for lignes in SORTIE:
                NOM=lignes[0]
                Prénom=lignes[1]
                PAYS=lignes[2]
                #DATE=athlete_infos.nais
                DISCIPLINE=lignes[4]
                REC=lignes[5]

                affichage_NOM = tk.Label(cadre_scrollbar_ath,text = NOM,font=("Tw Cent MT",13),bg="#e7e6e6")  # Créer un Label avec le nom de l'athlète
                affichage_NOM.pack()  # Placer le Label dans la fenêtre
                affichage_Prénom = tk.Label(cadre_scrollbar_ath,text = Prénom,font=("Tw Cent MT",13),bg="#e7e6e6")  # Créer un Label avec le prénom de l'athlète
                affichage_Prénom.pack()  # Placer le Label dans la fenêtre

                img_drapeau = Image.open("img/"+PAYS+".jpeg")#on ouvre l'image avec pill pour pas de problème d'objet
                img_drapeau = ImageTk.PhotoImage(img_drapeau)#on ouvre l'image avec tkinter
                affichage_Pays = tk.Label(cadre_scrollbar_ath, image=img_drapeau, bg="#e7e6e6")
                affichage_Pays.image = img_drapeau
                affichage_Pays.pack()

                affichage_DISCIPLINE = tk.Label(cadre_scrollbar_ath,text = DISCIPLINE,font=("Tw Cent MT",13),bg="#e7e6e6")  # Créer un Label avec la discipline de l'athlète
                affichage_DISCIPLINE.pack()  # Placer le Label dans la fenêtre
                affichage_REC = tk.Label(cadre_scrollbar_ath,text = REC,font=("Tw Cent MT",13),bg="#e7e6e6")  # Créer un Label avec la récompense de l'athlète
                affichage_REC.pack()  # Placer le Label dans la fenêtre
                
                try:
                    img_portrait = Image.open("img/"+NOM+"_"+Prénom+".jpeg")#on ouvre l'image avec pill pour pas de problème d'objet
                    img_portrait = ImageTk.PhotoImage(img_portrait)#on ouvre l'image avec tkinter
                except FileNotFoundError:
                    img_portrait = ImageTk.PhotoImage(Image.open("img/anonymous.jpeg"))

                affichage_portrait = tk.Label(cadre_scrollbar_ath, image=img_portrait, bg="#e7e6e6")
                affichage_portrait.image = img_portrait
                affichage_portrait.pack()

                underscore="_______________________________________________________________"
                affichage_underscore = tk.Label(cadre_scrollbar_ath,text = underscore,font=("Tw Cent MT",13),bg="#e7e6e6")
                affichage_underscore.pack()  # Placer le Label dans la fenêtre"""
    else:
        erreur_2 = tk.Label(cadre_scrollbar_ath,text = "Votre saisie est incomplète, réessayer !", bg='#ff3939',font=("Tw Cent MT",13)) #Créer un Label avec du texte d'erreur comme quoi il n'a pas tout renseigner
        erreur_2.pack(pady=25)  # Placer le Label dans la fenêtre

################################################################################################################################################
##################################### CREATION DES ENTRY ET FONCTIONS DU BOUTON: << Rechercher par une identité >> #################################
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
    effacer_milieu_vis()
    effacer_texte()
    cadre_scrollbar_vis.configure(label_text="Rechercher par une identité")
    global zone_visiteur_nom
    zone_visiteur_nom = tk.Entry(cadre_scrollbar_vis,fg="gray",font=("Tw Cent Mt",13))
    zone_visiteur_nom.insert(0,"NOM")
    zone_visiteur_nom.bind("<FocusIn>", retire_justi_visiteur_nom) #le focus, c-a-d lorsque l'utilisateur commence à taper dans l'entrée
    zone_visiteur_nom.bind("<FocusOut>", remise_justi_visiteur_nom) #perd le focus, c-a-d lorsque l'utilisateur cesse de taper dans l'entrée ou passe à un autre widget ou quitte la fenêtre
    zone_visiteur_nom.pack()
    global zone_visiteur_prenom
    zone_visiteur_prenom = tk.Entry(cadre_scrollbar_vis,fg="gray",font=("Tw Cent Mt",13))
    zone_visiteur_prenom.insert(0,"Prénom")
    zone_visiteur_prenom.bind("<FocusIn>", retire_justi_visiteur_prenom)
    zone_visiteur_prenom.bind("<FocusOut>", remise_justi_visiteur_prenom)
    zone_visiteur_prenom.pack()
    fenetre.bind("<Return>", rechercher_visiteur_nom) #lorsque la touche "entrée" du clavier est actionné, c'est la fonction rechercher_visiteur_nom qui s'exécute

def rechercher_visiteur_nom(event=None):
    effacer_label()
    effacer_infos_milieu_vis()
    Nom=zone_visiteur_nom.get()
    NOM=Nom.upper()
    prénom=zone_visiteur_prenom.get()
    Prénom=prénom.capitalize()
    ENTREE=NOM+" "+Prénom
    if NOM!="NOM" and NOM!="" and Prénom!="Prénom"and Prénom!="" :
        SORTIE=main.admin.search_visiteur_nom(ENTREE)
        if SORTIE=="ERREUR": #on test si cette personne est bien dans notre dico athlete
            erreur_1 = tk.Label(cadre_scrollbar_vis,text = "Ce visiteur n'est pas enregistré pour ces jeux !", bg='#ff3939',font=("Tw Cent MT",13))  # Créer un Label avec le message d'erreur
            erreur_1.pack(pady=25)
            redirection_1 = tk.Label(cadre_scrollbar_vis,text = "Pour vous enregistrer et obtenir votre ticket", bg='#ff3939',font=("Tw Cent MT",13))  # Créer un Label avec le message de redirection
            redirection_1.pack()
            redirection_2 = tk.Label(cadre_scrollbar_vis,text = "cliquer sur le bouton << Ajouter un visiteur >>", bg='#ff3939',font=("Tw Cent MT",13))  # Créer un Label avec le message de redirection
            redirection_2.pack()
        else:
            NUMERO=SORTIE[2]
            affichage_NOM = tk.Label(cadre_scrollbar_vis,text ="\n"+"NOM: "+NOM,font=("Tw Cent MT",13),bg="#e7e6e6")  # Créer un Label avec le nom du visiteur
            affichage_NOM.pack()  # Placer le Label dans la fenêtre
            affichage_Prénom = tk.Label(cadre_scrollbar_vis,text ="Prénom: " +Prénom,font=("Tw Cent MT",13),bg="#e7e6e6")  # Créer un Label avec le prénom du visiteur
            affichage_Prénom.pack()  # Placer le Label dans la fenêtre
            affichage_NUMERO = tk.Label(cadre_scrollbar_vis,text ="Numéro du billet: "+NUMERO,font=("Tw Cent MT",13),bg="#e7e6e6")  # Créer un Label avec le numéro de billet du visiteur
            affichage_NUMERO.pack()  # Placer le Label dans la fenêtre
    else:
        erreur_2 = tk.Label(cadre_scrollbar_vis,text = "Votre saisie est incomplète, réessayer !", bg='#ff3939',font=("Tw Cent MT",13)) #Créer un Label avec du texte d'erreur comme quoi il n'a pas tout renseigner
        erreur_2.pack(pady=25)  # Placer le Label dans la fenêtre

################################################################################################################################################
##################################### CREATION DES ENTRY ET FONCTIONS DU BOUTON: << Rechercher par numéro >> ###################################
################################################################################################################################################

def retire_justi_visiteur_num(event=None):
    if zone_visiteur_num.get() == "NUMERO DU BILLET":
        zone_visiteur_num.delete(0,'end')#les parametres sont les positions des caractères à retirer, ici du débu (0) à la fin ("end")
        zone_visiteur_num.config(fg="Black",font=("Tw Cent Mt",13))

def zone_texte_visi_num():
    effacer_label()
    effacer_milieu_vis()
    effacer_texte()
    cadre_scrollbar_vis.configure(label_text="Rechercher par numéro")
    global zone_visiteur_num
    zone_visiteur_num = tk.Entry(cadre_scrollbar_vis,fg="gray",font=("Tw Cent Mt",13))
    zone_visiteur_num.insert(0,"NUMERO DU BILLET")
    zone_visiteur_num.bind("<FocusIn>", retire_justi_visiteur_num)#le focus, c-a-d lorsque l'utilisateur commence à taper dans l'entrée
    zone_visiteur_num.pack()
    fenetre.bind("<Return>", rechercher_visiteur_num) #lorsque la touche "entrée" du clavier est actionné, c'est la fonction rechercher_visiteur_num qui s'exécute

def rechercher_visiteur_num(event=None):
    effacer_label()
    effacer_infos_milieu_vis()
    NUMERO=zone_visiteur_num.get()
    if NUMERO!="NUMERO DU BILLET" and NUMERO!="":
        SORTIE=main.admin.search_visiteur_num(NUMERO)
        if SORTIE=="ERREUR": #on test si le numéro rentré est bien recenser
            erreur_1 = tk.Label(cadre_scrollbar_vis,text = "Ce visiteur n'est pas enregistré pour ces jeux", bg='#ff3939',font=("Tw Cent MT",13))  # Créer un Label avec le message d'erreur
            erreur_1.pack(pady=25)
            redirection_1 = tk.Label(cadre_scrollbar_vis,text = "Pour vous enregistrer et obtenir votre ticket", bg='#ff3939',font=("Tw Cent MT",13))  # Créer un Label avec le message de redirection
            redirection_1.pack()
            redirection_2 = tk.Label(cadre_scrollbar_vis,text = "cliquer sur le bouton << Ajouter un visiteur >>", bg='#ff3939',font=("Tw Cent MT",13))  # Créer un Label avec le message de redirection
            redirection_2.pack()
        else:
            NOM=SORTIE[0]
            Prénom=SORTIE[1]
            affichage_NOM = tk.Label(cadre_scrollbar_vis,text ="\n"+"NOM: "+NOM,font=("Tw Cent MT",13),bg="#e7e6e6")  # Créer un Label avec le nom du visiteur
            affichage_NOM.pack()  # Placer le Label dans la fenêtre
            affichage_Prénom = tk.Label(cadre_scrollbar_vis,text ="Prénom: " +Prénom,font=("Tw Cent MT",13),bg="#e7e6e6")  # Créer un Label avec le prénom du visiteur
            affichage_Prénom.pack()  # Placer le Label dans la fenêtre
            affichage_NUMERO = tk.Label(cadre_scrollbar_vis,text ="Numéro du billet: "+NUMERO,font=("Tw Cent MT",13),bg="#e7e6e6")  # Créer un Label avec le numéro de billet du visiteur
            affichage_NUMERO.pack()  # Placer le Label dans la fenêtre
    else:
        erreur_2 = tk.Label(cadre_scrollbar_vis,text = "Votre saisie est incomplète, réessayer !", bg='#ff3939',font=("Tw Cent MT",13)) #Créer un Label avec du texte d'erreur comme quoi il n'a pas tout renseigner
        erreur_2.pack(pady=25)  # Placer le Label dans la fenêtre

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
    effacer_milieu_ath()
    effacer_texte()
    cadre_scrollbar_ath.configure(label_text="Ajouter un athlète")
    global zone_ajout_ath_nom
    zone_ajout_ath_nom = tk.Entry(cadre_scrollbar_ath,fg="gray",font=("Tw Cent Mt",13),width=30) #on augmente le nombre de caractère que la barre peut afficher
    zone_ajout_ath_nom.insert(0,"NOM")
    zone_ajout_ath_nom.bind("<FocusIn>", retire_justi_ajout_ath_nom) #le focus, c-a-d lorsque l'utilisateur commence à taper dans l'entrée
    zone_ajout_ath_nom.bind("<FocusOut>", remise_justi_ajout_ath_nom) #perd le focus, c-a-d lorsque l'utilisateur cesse de taper dans l'entrée ou passe à un autre widget ou quitte la fenêtre
    zone_ajout_ath_nom.pack()
    global zone_ajout_ath_prenom
    zone_ajout_ath_prenom = tk.Entry(cadre_scrollbar_ath,fg="gray",font=("Tw Cent Mt",13),width=30)
    zone_ajout_ath_prenom.insert(0,"Prénom")
    zone_ajout_ath_prenom.bind("<FocusIn>", retire_justi_ajout_ath_prenom)
    zone_ajout_ath_prenom.bind("<FocusOut>", remise_justi_ajout_ath_prenom)
    zone_ajout_ath_prenom.pack()
    global zone_ajout_ath_naissance
    zone_ajout_ath_naissance = tk.Entry(cadre_scrollbar_ath,fg="gray",font=("Tw Cent Mt",13),width=30)#on augmente le nombre de caractère que la barre peut afficher
    zone_ajout_ath_naissance.insert(0,"Date de naissance: AAAA-MM-JJ")
    zone_ajout_ath_naissance.bind("<FocusIn>", retire_justi_ajout_ath_naissance) 
    zone_ajout_ath_naissance.bind("<FocusOut>", remise_justi_ajout_ath_naissance) 
    zone_ajout_ath_naissance.pack()
    global zone_ajout_ath_pays
    zone_ajout_ath_pays = tk.Entry(cadre_scrollbar_ath,fg="gray",font=("Tw Cent Mt",13),width=30)
    zone_ajout_ath_pays.insert(0,"PAYS")
    zone_ajout_ath_pays.bind("<FocusIn>", retire_justi_ajout_ath_pays) 
    zone_ajout_ath_pays.bind("<FocusOut>", remise_justi_ajout_ath_pays) 
    zone_ajout_ath_pays.pack()
    global zone_ajout_ath_dis
    zone_ajout_ath_dis = tk.Entry(cadre_scrollbar_ath,fg="gray",font=("Tw Cent Mt",13),width=30)# ici on précise width=30 pour que date de naissance soit totalement afficher
    zone_ajout_ath_dis.insert(0,"DISCIPLINE")
    zone_ajout_ath_dis.bind("<FocusIn>", retire_justi_ajout_ath_dis)
    zone_ajout_ath_dis.bind("<FocusOut>", remise_justi_ajout_ath_dis) 
    zone_ajout_ath_dis.pack()

    fenetre.bind("<Return>", ajout_athlete) #lorsque la touche "entrée" du clavier est actionné, c'est la fonction ajout_athlete qui s'exécute

def ajout_athlete(event=None):
    effacer_label()
    effacer_infos_milieu_ath()
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
        if NOM!="NOM" and Prénom!="Prénom" and Naissance!="Date de naissance: AAAA-MM-JJ" and PAYS!="PAYS" and DISCIPLINE!="DISCIPLINE" and NOM!="" and Prénom!="" and Naissance!="" and PAYS!="" and DISCIPLINE!="":
            main.admin.ad_athlete(NOM,Prénom,Naissance,PAYS,DISCIPLINE)#on exécute l'ajout de l'athlète grâce à la fonction ad_athlete défini dans le main
            texte_affichage="L'athlète "+str(NOM)+" "+str(Prénom)+" né le "+str(Naissance)+" est ajouté aux jeux !"
            affichage = tk.Label(cadre_scrollbar_ath,text = texte_affichage, bg='#1fff23',font=("Tw Cent MT",13))  # Créer un Label avec du texte pour signifier que l'athlète est bien ajouter
            affichage.pack(pady=25)  # Placer le Label dans la fenêtre
        else:
            erreur_1 = tk.Label(cadre_scrollbar_ath,text = "Votre saisie est incomplète, réessayer !", bg='#ff3939',font=("Tw Cent MT",13))
            erreur_1.pack(pady=25)  # Placer le Label dans la fenêtre

    except Exception:
        erreur_2 = tk.Label(cadre_scrollbar_ath,text = "Votre saisie est incorrecte, respecter la mise en forme des entrées !", bg='#ff3939',font=("Tw Cent MT",13))  # Créer un Label avec du texte pour signifier qu'il faut respecter les entry
        erreur_2.pack(pady=25)  # Placer le Label dans la fenêtre

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
    effacer_milieu_vis()
    effacer_texte()
    cadre_scrollbar_vis.configure(label_text="Ajouter un visiteur")
    global zone_ajout_visiteur_nom
    zone_ajout_visiteur_nom = tk.Entry(cadre_scrollbar_vis,fg="gray",font=("Tw Cent Mt",13)) 
    zone_ajout_visiteur_nom.insert(0,"NOM")
    zone_ajout_visiteur_nom.bind("<FocusIn>", retire_justi_ajout_visiteur_nom) #le focus, c-a-d lorsque l'utilisateur commence à taper dans l'entrée
    zone_ajout_visiteur_nom.bind("<FocusOut>", remise_justi_ajout_visiteur_nom) #perd le focus, c-a-d lorsque l'utilisateur cesse de taper dans l'entrée ou passe à un autre widget ou quitte la fenêtre
    zone_ajout_visiteur_nom.pack()
    global zone_ajout_visiteur_prenom
    zone_ajout_visiteur_prenom = tk.Entry(cadre_scrollbar_vis,fg="gray",font=("Tw Cent Mt",13))
    zone_ajout_visiteur_prenom.insert(0,"Prénom")
    zone_ajout_visiteur_prenom.bind("<FocusIn>", retire_justi_ajout_visiteur_prenom)
    zone_ajout_visiteur_prenom.bind("<FocusOut>", remise_justi_ajout_visiteur_prenom)
    zone_ajout_visiteur_prenom.pack()

    fenetre.bind("<Return>", ajout_visiteur) #lorsque la touche "entrée" du clavier est actionné, c'est la fonction ajout_visiteur qui s'exécute

def ajout_visiteur(event=None):
    effacer_label()
    effacer_infos_milieu_vis()
    Nom=zone_ajout_visiteur_nom.get()
    NOM=Nom.upper()
    prénom=zone_ajout_visiteur_prenom.get()
    Prénom=prénom.capitalize() #pour transformer la chaine de caractère en minuscule et seulement le premier en MAJ
    ENTREE=str(NOM)+" "+str(Prénom)
    #print (ENTREE)
    if NOM!="NOM" and Prénom!="Prénom" and NOM!="" and Prénom!="":
        main.admin.ad_visiteur(NOM,Prénom)#on exécute l'ajout de l'athlète grâce à la fonction ad_athlete défini dans le main
        dic_vis=main.admin.ecriture_visiteur()
        texte_affichage_1="Le visiteur "+str(NOM)+" "+str(Prénom)+" est enregistré pour les jeux !"
        affichage_1 = tk.Label(cadre_scrollbar_vis,text = texte_affichage_1, bg='#1fff23',font=("Tw Cent MT",13))  # Créer un Label avec du texte pour signifier que le visiteur est bien ajouter
        affichage_1.pack()  # Placer le Label dans la fenêtre
        texte_affichage_2="Votre numéro de billet personnel est: "+str(dic_vis[ENTREE].numero)
        affichage_2 = tk.Label(cadre_scrollbar_vis,text = texte_affichage_2, bg='#1fff23',font=("Tw Cent MT",13))  # Créer un Label avec du texte pour afficher son numéro de billet
        affichage_2.pack()  # Placer le Label dans la fenêtre
    else:
        erreur = tk.Label(cadre_scrollbar_vis,text = "Votre saisie est incomplète, réessayer !", bg='#ff3939',font=("Tw Cent MT",13)) #Créer un Label avec du texte d'erreur comme quoi il n'a pas tout renseigner
        erreur.pack(pady=25)  # Placer le Label dans la fenêtre

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
    effacer_milieu_vis()
    effacer_texte()
    cadre_scrollbar_vis.configure(label_text="Supprimer un visiteur")
    global zone_suppr_visiteur_nom
    zone_suppr_visiteur_nom = tk.Entry(cadre_scrollbar_vis,fg="gray",font=("Tw Cent Mt",13)) 
    zone_suppr_visiteur_nom.insert(0,"NOM")
    zone_suppr_visiteur_nom.bind("<FocusIn>", retire_justi_suppr_visiteur_nom) #le focus, c-a-d lorsque l'utilisateur commence à taper dans l'entrée
    zone_suppr_visiteur_nom.bind("<FocusOut>", remise_justi_suppr_visiteur_nom) #perd le focus, c-a-d lorsque l'utilisateur cesse de taper dans l'entrée ou passe à un autre widget ou quitte la fenêtre
    zone_suppr_visiteur_nom.pack()
    global zone_suppr_visiteur_prenom
    zone_suppr_visiteur_prenom = tk.Entry(cadre_scrollbar_vis,fg="gray",font=("Tw Cent Mt",13))
    zone_suppr_visiteur_prenom.insert(0,"Prénom")
    zone_suppr_visiteur_prenom.bind("<FocusIn>", retire_justi_suppr_visiteur_prenom)
    zone_suppr_visiteur_prenom.bind("<FocusOut>", remise_justi_suppr_visiteur_prenom)
    zone_suppr_visiteur_prenom.pack()

    fenetre.bind("<Return>", supprimer_visiteur) #lorsque la touche "entrée" du clavier est actionné, c'est la fonction supprimer_visiteur qui s'exécute

def supprimer_visiteur(event=None):
    effacer_label()
    effacer_infos_milieu_vis()
    Nom=zone_suppr_visiteur_nom.get()
    NOM=Nom.upper()
    prénom=zone_suppr_visiteur_prenom.get()
    Prénom=prénom.capitalize() #pour transformer la chaine de caractère en minuscule et seulement le premier en MAJ
    if NOM!="NOM" and Prénom!="Prénom" and NOM!="" and Prénom!="":
        SORTIE=main.admin.del_visiteur(NOM,Prénom)
        if SORTIE=="ERREUR": #on test si le paus rentré est bien dans les jeux
            erreur_1 = tk.Label(cadre_scrollbar_vis,text = "Ce visiteur n'est pas enregistré pour ces jeux !", bg='#ff3939',font=("Tw Cent MT",13))  # Créer un Label avec le message d'erreur
            erreur_1.pack(pady=25)
            redirection_1 = tk.Label(cadre_scrollbar_vis,text = "Pour vous enregistrer et obtenir votre ticket", bg='#ff3939',font=("Tw Cent MT",13))  # Créer un Label avec le message de redirection
            redirection_1.pack()
            redirection_2 = tk.Label(cadre_scrollbar_vis,text = "cliquer sur le bouton << Ajouter un visiteur >>", bg='#ff3939',font=("Tw Cent MT",13))  # Créer un Label avec le message de redirection
            redirection_2.pack()
        else:
            texte_affichage="Le visiteur "+str(NOM)+" "+str(Prénom)+" a annulé son billet pour les jeux !"
            affichage = tk.Label(cadre_scrollbar_vis,text = texte_affichage, bg='#1fff23',font=("Tw Cent MT",13))  # Créer un Label avec du texte pour signifier que le visiteur est bien ajouter
            affichage.pack(pady=25)  # Placer le Label dans la fenêtre
            
    else:
        erreur_2 = tk.Label(cadre_scrollbar_vis,text = "Votre saisie est incomplète, réessayer !", bg='#ff3939',font=("Tw Cent MT",13))  # Créer un Label avec du texte d'erreur comme quoi il n'a pas tout renseigner
        erreur_2.pack(pady=25)  # Placer le Label dans la fenêtre

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
    effacer_milieu_ath()
    effacer_texte()
    cadre_scrollbar_ath.configure(label_text="Supprimer un athlète")
    global zone_suppr_ath_nom
    zone_suppr_ath_nom = tk.Entry(cadre_scrollbar_ath,fg="gray",font=("Tw Cent Mt",13)) 
    zone_suppr_ath_nom.insert(0,"NOM")
    zone_suppr_ath_nom.bind("<FocusIn>", retire_justi_suppr_ath_nom) #le focus, c-a-d lorsque l'utilisateur commence à taper dans l'entrée
    zone_suppr_ath_nom.bind("<FocusOut>", remise_justi_suppr_ath_nom) #perd le focus, c-a-d lorsque l'utilisateur cesse de taper dans l'entrée ou passe à un autre widget ou quitte la fenêtre
    zone_suppr_ath_nom.pack()
    global zone_suppr_ath_prenom
    zone_suppr_ath_prenom = tk.Entry(cadre_scrollbar_ath,fg="gray",font=("Tw Cent Mt",13))
    zone_suppr_ath_prenom.insert(0,"Prénom")
    zone_suppr_ath_prenom.bind("<FocusIn>", retire_justi_suppr_ath_prenom)
    zone_suppr_ath_prenom.bind("<FocusOut>", remise_justi_suppr_ath_prenom)
    zone_suppr_ath_prenom.pack()

    fenetre.bind("<Return>", supprimer_athlete) #lorsque la touche "entrée" du clavier est actionné, c'est la fonction supprimer_athlete qui s'exécute

def supprimer_athlete(event=None):
    effacer_label()
    effacer_infos_milieu_ath()
    Nom=zone_suppr_ath_nom.get()
    NOM=Nom.upper()
    prénom=zone_suppr_ath_prenom.get()
    Prénom=prénom.capitalize() #pour transformer la chaine de caractère en minuscule et seulement le premier en MAJ
    #print (ENTREE)
    if NOM!="NOM" and Prénom!="Prénom" and NOM!="" and Prénom!="":
        SORTIE=main.admin.del_athlete(NOM,Prénom)
        if SORTIE=="ERREUR": #on test si l'athlète rentré est bien dans les jeux
            erreur_1 = tk.Label(cadre_scrollbar_ath,text = "Cet athlète ne participe pas à ces jeux !", bg='#ff3939',font=("Tw Cent MT",13))  # Créer un Label avec le message d'erreur
            erreur_1.pack(pady=25)
        else:
            texte_affichage="L'athlète "+str(NOM)+" "+str(Prénom)+" ne participe plus à ces jeux !"
            affichage = tk.Label(cadre_scrollbar_ath,text = texte_affichage, bg='#1fff23',font=("Tw Cent MT",13))  # Créer un Label avec du texte pour signifier que le visiteur est bien ajouter
            affichage.pack(pady=25)  # Placer le Label dans la fenêtre
    else:
        erreur_2 = tk.Label(cadre_scrollbar_ath,text = "Votre saisie est incomplète, réessayer !", bg='#ff3939',font=("Tw Cent MT",13))  # Créer un Label avec du texte d'erreur comme quoi il n'a pas tout renseigner
        erreur_2.pack(pady=25)  # Placer le Label dans la fenêtre

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
    effacer_milieu_ath()
    effacer_texte()
    cadre_scrollbar_ath.configure(label_text="Modifier une récompense")
    global zone_rec_nom
    zone_rec_nom = tk.Entry(cadre_scrollbar_ath,fg="gray",font=("Tw Cent Mt",13),width=30)#on augmente le nombre de caractère que la barre peut afficher
    zone_rec_nom.insert(0,"NOM")
    zone_rec_nom.bind("<FocusIn>", retire_justi_rec_nom) #le focus, c-a-d lorsque l'utilisateur commence à taper dans l'entrée
    zone_rec_nom.bind("<FocusOut>", remise_justi_rec_nom) #perd le focus, c-a-d lorsque l'utilisateur cesse de taper dans l'entrée ou passe à un autre widget ou quitte la fenêtre
    zone_rec_nom.pack()
    global zone_rec_prenom
    zone_rec_prenom = tk.Entry(cadre_scrollbar_ath,fg="gray",font=("Tw Cent Mt",13),width=30)#on augmente le nombre de caractère que la barre peut afficher
    zone_rec_prenom.insert(0,"Prénom")
    zone_rec_prenom.bind("<FocusIn>", retire_justi_rec_prenom)
    zone_rec_prenom.bind("<FocusOut>", remise_justi_rec_prenom)
    zone_rec_prenom.pack()
    global zone_rec_medaille
    zone_rec_medaille = tk.Entry(cadre_scrollbar_ath,fg="gray",font=("Tw Cent Mt",13),width=30)#on augmente le nombre de caractère que la barre peut afficher
    zone_rec_medaille.insert(0,"Médaille (<<Rien>> pour supprimer)")
    zone_rec_medaille.bind("<FocusIn>", retire_justi_rec_medaille)
    zone_rec_medaille.bind("<FocusOut>", remise_justi_rec_medaille)
    zone_rec_medaille.pack()

    fenetre.bind("<Return>", modifier_recompense) #lorsque la touche "entrée" du clavier est actionné, c'est la fonction modifier_recompense qui s'exécute

def modifier_recompense(event=None):
    effacer_label()
    effacer_infos_milieu_ath()
    Nom=zone_rec_nom.get()
    NOM=Nom.upper()
    prénom=zone_rec_prenom.get()
    Prénom=prénom.capitalize() #pour transformer la chaine de caractère en minuscule et seulement le premier en MAJ
    médaille=zone_rec_medaille.get()
    Médaille=médaille.capitalize()
    if NOM!="NOM" and Prénom!="Prénom" and Médaille!="Médaille" and (Médaille=="Or" or Médaille=="Argent" or Médaille=="Bronze" or Médaille=="None" or Médaille=="Rien" or Médaille==" ") and NOM!="" and Prénom!="" and Médaille!="":
        SORTIE=main.admin.update_recompense(NOM,Prénom,Médaille)
        if SORTIE=="ERREUR": #on test si le paus rentré est bien dans les jeux
            erreur_1 = tk.Label(cadre_scrollbar_ath,text = "Cet athlète ne participe pas à ces jeux !", bg='#ff3939',font=("Tw Cent MT",13))  # Créer un Label avec le message d'erreur
            erreur_1.pack(pady=25)
        elif SORTIE=="DEJA LA MEDAILLE":
            erreur_2 = tk.Label(cadre_scrollbar_ath,text = "Cet athlète possède déjà cette médaille !", bg='#ff3939',font=("Tw Cent MT",13))  # Créer un Label avec le message d'erreur
            erreur_2.pack(pady=25)
        elif Médaille=="Or" or Médaille=="Argent":
            texte_affichage_1="L'athlète "+str(NOM)+" "+str(Prénom)+" possède maintenant la médaille d'"+Médaille+" !"
            affichage_1 = tk.Label(cadre_scrollbar_ath,text = texte_affichage_1, bg='#1fff23',font=("Tw Cent MT",13))  # Créer un Label avec du texte pour signifier que le visiteur est bien ajouter
            affichage_1.pack(pady=25)  # Placer le Label dans la fenêtre
        elif Médaille=="Bronze":
            texte_affichage_2="L'athlète "+str(NOM)+" "+str(Prénom)+" possède maintenant la médaille de Bronze !"
            affichage_2 = tk.Label(cadre_scrollbar_ath,text = texte_affichage_2, bg='#1fff23',font=("Tw Cent MT",13))  # Créer un Label avec du texte pour signifier que le visiteur est bien ajouter
            affichage_2.pack(pady=25)  # Placer le Label dans la fenêtre
        else:
            texte_affichage="L'athlète "+str(NOM)+" "+str(Prénom)+" ne possède plus de médaille !"
            affichage = tk.Label(cadre_scrollbar_ath,text = texte_affichage, bg='#1fff23',font=("Tw Cent MT",13))  # Créer un Label avec du texte pour signifier que le visiteur est bien ajouter
            affichage.pack(pady=25)  # Placer le Label dans la fenêtre
    else:
        erreur_3 = tk.Label(cadre_scrollbar_ath,text = "Votre saisie est incomplète ou incorrecte, réessayer !", bg='#ff3939',font=("Tw Cent MT",13))  # Créer un Label avec du texte d'erreur comme quoi il n'a pas tout renseigner
        erreur_3.pack(pady=25)  # Placer le Label dans la fenêtre

interface_accueil()
fenetre.mainloop() #on démarre la boucle de l'I.G, ce qui permet à la fenetre de rester active et de réagir aux événements de l'utilisateur jusqu'à ce que la fenêtre soit fermée
