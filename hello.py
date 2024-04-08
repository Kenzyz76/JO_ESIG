
import tkinter as tk

def effacer():
    cadre_bouton_athlete.destroy()
    cadre_bouton_visiteur.destroy()

def afficher():
    text = tk.Label(text = "")
    text.place(x=200, y=200)

def creer_bouton(fenetre, texte, commande, largeur, hauteur):
    bouton = tk.Button(fenetre, text=texte, command=lambda: commande(), width=largeur, height=hauteur)
    bouton.pack()
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
    creer_bouton(cadre_gauche, f"Afficher tous les athlètes", afficher, 15, 2)

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
    menu_deroulant = tk.OptionMenu(cadre_central, variable_menu, options_menu)
    menu_deroulant.pack()


    # Créer un Frame à droite pour les boutons de droite
    cadre_droit = tk.Frame(fenêtre)
    cadre_droit.pack(side="right", fill="y")

    # Ajouter trois boutons au Frame de droite
    for i in range(1, 4):
        creer_bouton(cadre_droit, f"Bouton D{i}", afficher, 3, 3)

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
        creer_bouton(cadre_gauche, f"Bouton G{i}", afficher)

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
        creer_bouton(frame, f"Bouton D{i}", afficher)

# Créer la fenêtre principale
fenêtre = tk.Tk()
fenêtre.title("Interface Dynamique avec Animations de Bouton")

cadre_bouton_athlete = tk.Frame(fenêtre)
cadre_bouton_athlete.pack(side="left", fill="x", expand=True)

cadre_bouton_visiteur = tk.Frame(fenêtre)
cadre_bouton_visiteur.pack(side="right", fill="x", expand=True)
# Définir la taille de la fenêtre à 900x500 pixels
fenêtre.geometry("900x500")
fenêtre.minsize(500,300)
# Créer et placer deux boutons initiaux au centre
bouton1 = creer_bouton(cadre_bouton_athlete, "Athlètes", afficher_interface_athlete, 20, 20)
bouton2 = creer_bouton(cadre_bouton_visiteur, "Visiteurs", afficher_interface_visiteur, 20, 20)

# Démarrer la boucle événementielle de l'interface graphique
fenêtre.mainloop()

