import tkinter as tk
import admin

def effacer_fenetre():
    for child in fenêtre.winfo_children():
        if isinstance(child, tk.Frame):
            child.destroy()

def effacer_label():
    for child in fenêtre.winfo_children():
        if isinstance(child, tk.Label):
            child.destroy()

def afficher_athlete():
    effacer_label()
    y_position = 10
    for element in admin.admin.afficher_athlete():
        athlete = tk.Label(text = element)  # Créer un Label avec les informations de l'athlète
        athlete.configure(bg='#3399FF')
        athlete.place(x=200, y=y_position)  # Placer le Label dans la fenêtre
        y_position += 30

def afficher_visiteur():
    effacer_label()
    y_position = 10
    for element in admin.admin.afficher_visiteur():
        text = tk.Label(text = element)  # Créer un Label avec les informations de l'athlète
        text.configure(bg='#3399FF')
        text.place(x=200, y=y_position)  # Placer le Label dans la fenêtre
        y_position += 30


def creer_bouton(fenetre, texte, commande, largeur, hauteur, couleur,police, taille):
    bouton = tk.Button(fenetre, text=texte, command=lambda: commande(), width=largeur, height=hauteur, bg=couleur, font=(police, taille))
    bouton.pack() #permet d'afficher le bouton
    return bouton

def afficher_interface_athlete():
    effacer_fenetre()
    # Supprimer les boutons initiaux

    cadre_bouton_retour1 = tk.Frame(fenêtre, width=100, height=100, bg='grey')
    cadre_bouton_retour1.place(x=0, y=500, anchor='sw')

    creer_bouton(cadre_bouton_retour1, f"Retour", interface_principale, 3, 2, '#EE5F5F' , 'Tw Cen MT',20)

    # Créer un Frame à gauche pour les boutons de gauche
    cadre_gauche = tk.Frame(fenêtre)
    cadre_gauche.pack(side="left", fill="y")

    # Ajouter trois boutons au Frame de gauche
    creer_bouton(cadre_gauche, f"Afficher tous les athlètes", afficher_athlete, 20, 2, '#9ef0f6','Tw Cen MT',12)
    creer_bouton(cadre_gauche, f"Afficher par pays", afficher_athlete, 20, 2,'#6ecaf2','Tw Cen MT',12)
    creer_bouton(cadre_gauche, f"Afficher par discipline", afficher_athlete, 20, 2, '#2969eb','Tw Cen MT',12)


    # Créer un Frame à droite pour les boutons de droite
    cadre_droit = tk.Frame(fenêtre)
    cadre_droit.pack(side="right", fill="y")

    # Ajouter trois boutons au Frame de droite
    creer_bouton(cadre_droit, f"caca", afficher_athlete, 20, 2,'#9ef0f6','Tw Cen MT',12)
    creer_bouton(cadre_droit, f"pipi", afficher_athlete, 20, 2,'#6ecaf2','Tw Cen MT',12)
    creer_bouton(cadre_droit, f"popo", afficher_athlete, 20, 2,'#2969eb','Tw Cen MT',12)
    cadre_bouton_retour1.lift() # permet de placer le cadre cadre_bouton_retour1 au premier plan


def afficher_interface_visiteur():
    effacer_fenetre()
    # Supprimer les boutons initiaux
    cadre_bouton_retour2 = tk.Frame(fenêtre, width=100, height=100, bg='grey')
    cadre_bouton_retour2.place(x=0, y=500, anchor='sw')

    creer_bouton(cadre_bouton_retour2, f"Retour", interface_principale, 3, 2, '#EE5F5F' , 'Tw Cen MT',20)

    # Créer un Frame à gauche pour les boutons de gauche
    cadre_gauche = tk.Frame(fenêtre)
    cadre_gauche.pack(side="left", fill="y")


    # Ajouter trois boutons au Frame de gauche
    creer_bouton(cadre_gauche, f"Afficher tous les visiteurs", afficher_visiteur, 20,2, 'red','Tw Cen MT',12)

    # Créer un Frame à droite pour les boutons de droite
    cadre_droit = tk.Frame(fenêtre)
    cadre_droit.pack(side="right", fill="both")

    # Ajouter trois boutons au Frame de droite

    creer_bouton(cadre_droit, "caca", afficher_athlete,20,2, 'red','Tw Cen MT',12)
    cadre_bouton_retour2.lift() # permet de placer le cadre cadre_bouton_retour1 au premier plan


# Créer la fenêtre principale
fenêtre = tk.Tk()
fenêtre.title("Gestion des JO")
fenêtre.configure(bg='#f4fefe')



def interface_principale(): 
    effacer_fenetre()
    effacer_label()
    cadre_bouton_athlete = tk.Frame(fenêtre)
    cadre_bouton_athlete.pack(side="left", fill="x", expand=True)
    cadre_bouton_athlete.configure(bg ='#f4fefe')
    cadre_bouton_visiteur = tk.Frame(fenêtre)
    cadre_bouton_visiteur.pack(side="right", fill="x", expand=True)
    cadre_bouton_visiteur.configure(bg = '#f4fefe')
    cadre_bouton_retour = tk.Frame(fenêtre, width=100, height=100, bg='green')
    cadre_bouton_retour.place(x=0, y=500, anchor='sw')


    # Définir la taille de la fenêtre à 900x500 pixels
    fenêtre.geometry("1000x500")
    fenêtre.minsize(500,300)
    # Créer et placer deux boutons initiaux au centre
    creer_bouton(cadre_bouton_athlete, "Athlètes", afficher_interface_athlete, 20, 10, '#5FD4EE','Tw Cen MT',20)
    creer_bouton(cadre_bouton_visiteur, "Visiteurs", afficher_interface_visiteur, 20, 10, '#EE5F5F','Tw Cen MT',20)
    creer_bouton(cadre_bouton_retour, "Quitter", fenêtre.destroy, 3, 2, '#EE5F5F' , 'Tw Cen MT',20)

interface_principale()
fenêtre.mainloop()