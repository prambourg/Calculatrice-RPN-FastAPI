# Exercice technique pour le CACIB
## Enoncé
### Contexte
Réalisation d’une calculatrice RPN (notation polonaise inversée) en mode client/serveur. Utilisation de FastAPI ou Flask au choix, j'ai choisi FastAPI pour Swagger UI et l'interaction aisée avec l'API.
### Fonctionnalités demandées
- Ajout d’un élément dans une pile
- Récupération de la pile
- Nettoyage de la pile
- Opération +
- Opération -
- Opération *
- Opération /
### Livrables
- Repo GitHub (celui-là même)
- Fichier todo.md regroupant améliorations et raccourcis dans le contexte d'une production ultra courte (~2h)
- Fichier roadmap.md contenant un backlog plus étoffé pour de futurs développement
## Utilisation
Création de l'environnement virtuel
> python -m venv venv

Activation de l'environnement virtuel, selon l'OS

Installer les dépendances 
> pip install -r requirements.txt

Lancer FastAPI
> fastapi dev main.py

On retrouve alors l'API interactive à l'adresse suivant : http://127.0.0.1:8000/docs
