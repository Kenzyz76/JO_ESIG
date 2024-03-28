
import tkinter as tk

def animer_bouton(bouton):
    couleur_originale = bouton.cget('bg')  # Récupérer la couleur d'origine du bouton
    bouton.config(bg='red')  # Changer la couleur du bouton en rouge
    bouton.after(100, lambda: bouton.config(bg=couleur_originale))  # Remettre la couleur d'origine après 100ms

def creer_bouton(frame, texte, commande):
    bouton = tk.Button(frame, text=texte, command=lambda: commande(bouton))
    bouton.pack(pady=5)
    return bouton

def afficher_nouvelle_interface(bouton):
    animer_bouton(bouton)  # Anime le bouton qui a été cliqué

    # Supprimer les boutons initiaux
    bouton1.destroy()
    bouton2.destroy()

    # Créer un Frame à gauche pour les boutons de gauche
    frame_gauche = tk.Frame(root)
    frame_gauche.pack(side=tk.LEFT, fill=tk.Y, padx=10)

    # Ajouter trois boutons au Frame de gauche
    for i in range(1, 4):
        creer_bouton(frame_gauche, f"Bouton G{i}", animer_bouton)

    # Créer un Frame central pour le champ de texte et le menu déroulant
    frame_central = tk.Frame(root)
    frame_central.pack(side=tk.LEFT, padx=20)

    # Créer un champ de texte dans le Frame central
    champ_texte = tk.Entry(frame_central, width=20)
    champ_texte.pack(pady=(0, 20))  # Ajoute un espace entre le champ de texte et le menu déroulant

    # Créer un menu déroulant dans le Frame central, sous le champ de texte
    options_menu = ["Option 1", "Option 2", "Option 3"]
    variable_menu = tk.StringVar(root)
    variable_menu.set(options_menu[0])  # Définir l'option par défaut
    menu_deroulant = tk.OptionMenu(frame_central, variable_menu, *options_menu)
    menu_deroulant.pack()

    # Créer un Frame à droite pour les boutons de droite
    frame_droite = tk.Frame(root)
    frame_droite.pack(side=tk.LEFT, fill=tk.Y, padx=10)

    # Ajouter trois boutons au Frame de droite
    for i in range(1, 4):
        creer_bouton(frame_droite, f"Bouton D{i}", animer_bouton)

# Créer la fenêtre principale
root = tk.Tk()
root.title("Interface Dynamique avec Animations de Bouton")

# Définir la taille de la fenêtre à 400x300 pixels
root.geometry("400x300")

# Créer et placer deux boutons initiaux au centre
bouton1 = creer_bouton(root, "Option 1", afficher_nouvelle_interface)
bouton2 = creer_bouton(root, "Option 2", afficher_nouvelle_interface)

# Démarrer la boucle événementielle de l'interface graphique
root.mainloop()
