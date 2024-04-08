
import tkinter as tk
from tkinter import font
import admin

def effacer():
    cadre_bouton_athlete.destroy()
    cadre_bouton_visiteur.destroy()

def afficher():
    text = tk.Label(text = "")
    text.place(x=200, y=200)

def creer_bouton(fenetre, texte, commande, largeur, hauteur, couleur,police, taille):
    bouton = tk.Button(fenetre, text=texte, command=lambda: commande(), width=largeur, height=hauteur, bg=couleur, font=(police, taille))
    bouton.pack() #permet d'afficher le bouton
    return bouton

def afficher_interface_athlete():
    effacer()
    # Supprimer les boutons initiaux
    bouton1.destroy()
    bouton2.destroy()

    # Créer un Frame à gauche pour les boutons de gauche
    cadre_gauche = tk.Frame(fenêtre)
    cadre_gauche.pack(side="left", fill="y")

    # Ajouter trois boutons au Frame de gauche
    creer_bouton(cadre_gauche, f"Afficher tous les athlètes", admin.admin.afficher_athlete, 20, 2, '#9ef0f6','Tw Cen MT',12)
    creer_bouton(cadre_gauche, f"Afficher par pays", afficher, 20, 2,'#6ecaf2','Tw Cen MT',12)
    creer_bouton(cadre_gauche, f"Afficher par discipline", afficher, 20, 2, '#2969eb','Tw Cen MT',12)

    # Créer un Frame central pour le champ de texte et le menu déroulant
    cadre_central = tk.Frame(fenêtre)
    cadre_central.pack(side="left",fill="x", expand=True)

    # Créer un champ de texte dans le Frame central
    champ_texte = tk.Entry(cadre_central, width=20)
    champ_texte.pack(pady=(0, 20))  # Ajoute un espace entre le champ de texte et le menu déroulant

    # Créer un menu déroulant dans le Frame central, sous le champ de texte
    options_menu = ["Option 1", "Option 2", "Option 3"]
    variable_menu = tk.StringVar(fenêtre)
    variable_menu.set(options_menu[0])  # Définir l'option par défaut
    menu_deroulant = tk.OptionMenu(cadre_central, variable_menu, *options_menu)
    menu_deroulant.pack()


    # Créer un Frame à droite pour les boutons de droite
    cadre_droit = tk.Frame(fenêtre)
    cadre_droit.pack(side="right", fill="y")

    # Ajouter trois boutons au Frame de droite
    creer_bouton(cadre_droit, f"caca", afficher, 20, 2,'#9ef0f6','Tw Cen MT',12)
    creer_bouton(cadre_droit, f"pipi", afficher, 20, 2,'#6ecaf2','Tw Cen MT',12)
    creer_bouton(cadre_droit, f"popo", afficher, 20, 2,'#2969eb','Tw Cen MT',12)



def afficher_interface_visiteur():
    effacer()
    # Supprimer les boutons initiaux
    bouton1.destroy()
    bouton2.destroy()

    # Créer un Frame à gauche pour les boutons de gauche
    cadre_gauche = tk.Frame(fenêtre)
    cadre_gauche.pack(side="left", fill="y")

    # Ajouter trois boutons au Frame de gauche
    for i in range(1, 4):
        creer_bouton(cadre_gauche, f"Bouton G{i}", afficher, 20,2, 'red','Tw Cen MT',12)

    # Créer un Frame central pour le champ de texte et le menu déroulant
    cadre_central = tk.Frame(fenêtre)
    cadre_central.pack(side="left", fill ="x", expand=True)

    # Créer un champ de texte dans le Frame central
    champ_texte = tk.Entry(cadre_central, width=20)
    champ_texte.pack(pady=(0, 20))  # Ajoute un espace entre le champ de texte et le menu déroulant

    # Créer un menu déroulant dans le Frame central, sous le champ de texte
    options_menu = ["Option 1", "Option 2", "Option 3"]
    variable_menu = tk.StringVar(fenêtre)
    variable_menu.set(options_menu[0])  # Définir l'option par défaut
    menu_deroulant = tk.OptionMenu(cadre_central, variable_menu, *options_menu)
    menu_deroulant.pack()

    # Créer un Frame à droite pour les boutons de droite
    frame = tk.Frame(fenêtre)
    frame.pack(side="right", fill="both")

    # Ajouter trois boutons au Frame de droite
    for i in range(1, 4):
        creer_bouton(frame, f"Bouton D{i}", afficher,20,2,'Tw Cen MT',12)

# Créer la fenêtre principale
fenêtre = tk.Tk()
fenêtre.title("Interface Dynamique avec Animations de Bouton")
fenêtre.configure(bg='#f4fefe')

cadre_bouton_athlete = tk.Frame(fenêtre)
cadre_bouton_athlete.pack(side="left", fill="x", expand=True)
cadre_bouton_athlete.configure(bg ='#f4fefe')


cadre_bouton_visiteur = tk.Frame(fenêtre)
cadre_bouton_visiteur.pack(side="right", fill="x", expand=True)
cadre_bouton_visiteur.configure(bg ='#f4fefe')
# Définir la taille de la fenêtre à 900x500 pixels
fenêtre.geometry("900x500")
fenêtre.minsize(500,300)
# Créer et placer deux boutons initiaux au centre
bouton1 = creer_bouton(cadre_bouton_athlete, "Athlètes", afficher_interface_athlete, 20, 10, '#5FD4EE','Tw Cen MT',20)
bouton2 = creer_bouton(cadre_bouton_visiteur, "Visiteurs", afficher_interface_visiteur, 20, 10, '#EE5F5F','Tw Cen MT',20)

# Démarrer la boucle événementielle de l'interface graphique
fenêtre.mainloop()

