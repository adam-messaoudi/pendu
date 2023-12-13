import pygame  # Importation du module pygame pour créer le jeu
import random  # Importation du module random pour choisir un mot aléatoire
import sys  # Importation du module sys pour gérer la sortie du jeu
import os  # Importation du module os pour les opérations liées au système d'exploitation

# Initialisation de Pygame
pygame.init()

# Définition des couleurs utilisées dans le jeu
BLANC = (255, 255, 255)
NOIR = (0, 0, 0)
ROUGE = (255, 0, 0)
VERT = (0, 255, 0)

# Paramètres de la fenêtre
largeur, hauteur = 800, 600  # Définition de la taille de la fenêtre
fenetre = pygame.display.set_mode((largeur, hauteur))  # Création de la fenêtre
pygame.display.set_caption('Jeu du Pendu')  # Titre de la fenêtre

# Chargement des images du pendu depuis le dossier "image"
images_pendu = []
for i in range(7):
    image_path = os.path.join("image", f"pendu{i}.png")
    try:
        image = pygame.image.load(image_path)
        images_pendu.append(image)  # Ajouter l'image chargée à la liste
    except pygame.error:
        print("Erreur lors du chargement de l'image:", image_path)
        sys.exit()

# Liste de mots à deviner
liste_mots = ["ordinateur", "programmation", "python", "intelligence", "apprentissage", "developpement", "algorithmes", "donnees", "logiciel", "machine", "apprentissage", "codage", "computation", "informations", "analyse", "reseau", "interface", "systeme", "technologie", "science"]

# Fonction pour choisir un mot aléatoire dans la liste de mots
def choisir_mot(liste_mots):
    return random.choice(liste_mots).lower()

# Fonction pour afficher le mot caché avec les lettres trouvées
def afficher_mot_cache(mot, lettres_trouvees):
    mot_cache = ""
    for lettre in mot:
        if lettre in lettres_trouvees:
            mot_cache += lettre + " "  # Ajoute la lettre si elle a été trouvée
        else:
            mot_cache += "_ "  # Ajoute un espace pour chaque lettre non trouvée
    return mot_cache

# Fonction principale pour jouer au pendu
def jouer_pendu():
    while True:
        erreurs = 0  # Initialisation du compteur d'erreurs
        lettres_trouvees = []  # Initialisation de la liste des lettres trouvées
        mot_a_deviner = choisir_mot(liste_mots)  # Choix aléatoire d'un mot à deviner dans la liste
        max_erreurs = 6  # Définition du nombre maximum d'erreurs autorisées

        while True:
            fenetre.fill(BLANC)  # Remplissage de la fenêtre avec la couleur blanche

            # Gestion des événements (clavier, fermeture de fenêtre)
            for event in pygame.event.get():
                if event.type == pygame.QUIT:  # Si l'événement est de fermeture de fenêtre
                    pygame.quit()  # Ferme Pygame
                    sys.exit()  # Termine le programme

                if event.type == pygame.KEYDOWN:  # Si une touche est pressée
                    if event.key == pygame.K_ESCAPE:  # Si la touche pressée est Echap
                        pygame.quit()  # Ferme Pygame
                        sys.exit()  # Termine le programme

                    if event.key >= pygame.K_a and event.key <= pygame.K_z:  # Si la touche pressée est une lettre
                        lettre = chr(event.key)  # Obtient la lettre correspondante à la touche
                        if lettre not in lettres_trouvees:  # Vérifie si la lettre n'a pas déjà été choisie
                            lettres_trouvees.append(lettre)  # Ajoute la lettre à la liste des lettres trouvées
                            if lettre not in mot_a_deviner:  # Si la lettre ne fait pas partie du mot à deviner
                                erreurs += 1  # Incrémente le compteur d'erreurs

            # Affichage du mot caché
            mot_cache = afficher_mot_cache(mot_a_deviner, lettres_trouvees)
            font = pygame.font.Font(None, 60)  # Définit la police et la taille du texte
            text = font.render(mot_cache, True, NOIR)  # Crée un rendu du mot caché
            text_rect = text.get_rect(midleft=(largeur // 3, hauteur // 2))  # Positionne le texte au milieu de la fenêtre
            fenetre.blit(text, text_rect)  # Affiche le texte dans la fenêtre

            # Affichage de l'image du pendu à gauche du mot caché
            image_rect = images_pendu[erreurs].get_rect(midright=(largeur // 4, hauteur // 2.5))
            fenetre.blit(images_pendu[erreurs], image_rect)

            # Vérification de la victoire ou de la défaite
            if erreurs >= max_erreurs or "_" not in mot_cache:
                font = pygame.font.Font(None, 80)  # Définit la police et la taille du texte pour le message final
                if erreurs >= max_erreurs:
                    text = font.render('Défaite!', True, ROUGE)  # Rendu du texte 'Défaite!'
                else:
                    text = font.render('Victoire!', True, VERT)  # Rendu du texte 'Victoire!'
                text_rect = text.get_rect(center=(largeur // 2, hauteur // 2 + 100))  # Positionne le texte au centre de la fenêtre
                fenetre.blit(text, text_rect)  # Affiche le texte dans la fenêtre
                pygame.display.update()  # Met à jour l'affichage
                break  # Sort de la boucle de jeu

            pygame.display.update()  # Met à jour l'affichage à chaque itération

        pygame.time.wait(2000)  # Attend 2 secondes avant de redémarrer le jeu après victoire ou défaite

# Lancement du jeu
jouer_pendu()
