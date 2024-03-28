
import tkinter as tk

def animer_bouton(bouton):
    couleur_originale = bouton.cget('bg')  # Récupérer la couleur d'origine du bouton
    bouton.config(bg='red')  # Changer la couleur du bouton en rouge
    bouton.after(100, lambda: bouton.config(bg=couleur_originale))  # Remettre la couleur d'origine après 100ms

def creer_bouton(frame, texte, commande):
    bouton = tk.Button(frame, text=texte, command=lambda: commande(bouton), width=10, height=10)
    bouton.pack(pady=5)
    return bouton

def afficher_interface_athlete():

    # Supprimer les boutons initiaux
    bouton1.destroy()
    bouton2.destroy()

    # Créer un Frame à gauche pour les boutons de gauche
    cadre_gauche = tk.Frame(fenêtre)
    cadre_gauche.pack(side=tk.LEFT, fill="y",expand=False,  padx=10)

    # Ajouter trois boutons au Frame de gauche
    for i in range(1, 4):
        creer_bouton(cadre_gauche, f"Bouton G{i}", animer_bouton)

    # Créer un Frame central pour le champ de texte et le menu déroulant
    cadre_central = tk.Frame(fenêtre)
    cadre_central.pack(side=tk.LEFT, padx=20, expand=True)

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
    frame.pack(side=tk.RIGHT, fill="y", padx=10)

    # Ajouter trois boutons au Frame de droite
    for i in range(1, 4):
        creer_bouton(frame, f"Bouton D{i}", animer_bouton)

def afficher_interface_visiteur(bouton):
    animer_bouton(bouton)  # Anime le bouton qui a été cliqué

    # Supprimer les boutons initiaux
    bouton1.destroy()
    bouton2.destroy()

    # Créer un Frame à gauche pour les boutons de gauche
    cadre_gauche = tk.Frame(fenêtre)
    cadre_gauche.pack(side="left", fill="y")

    # Ajouter trois boutons au Frame de gauche
    for i in range(1, 4):
        creer_bouton(cadre_gauche, f"Bouton G{i}", animer_bouton)

    # Créer un Frame central pour le champ de texte et le menu déroulant
    cadre_central = tk.Frame(fenêtre)
    cadre_central.pack(side="left", padx=20, expand=False)

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
        creer_bouton(frame, f"Bouton D{i}", animer_bouton)

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
bouton1 = creer_bouton(cadre_bouton_athlete, "Athlètes", afficher_interface_athlete)
bouton2 = creer_bouton(cadre_bouton_visiteur, "Visiteurs", afficher_interface_visiteur)

# Démarrer la boucle événementielle de l'interface graphique
fenêtre.mainloop()
