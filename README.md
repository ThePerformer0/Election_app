# Election App

Une application web pour gérer les élections étudiantes.

## Description

Election App est une plateforme de vote en ligne conçue pour un établissement scolaire pour les élections du président de l'association des étudiants. Seuls les délégués de classe participent aux votes, et ceux-ci sont ajoutés par un membre de l'administration de l'école pour participer au vote. C'est également cet administrateur qui ajoute des candidats aux élections.

## Technologies utilisées

- **Backend** : Django
- **Frontend** : HTML, CSS (TailwindCSS), JavaScript

## Prérequis

- Python 3.9 ou supérieur
- pip (gestionnaire de paquets Python)
- Virtualenv (optionnel mais recommandé)

## Installation

1. Clonez le dépôt :

    ```sh
    git clone https://github.com/ThePerformer0/Election_app.git
    cd election_app
    cd election_project
    ```

2. Créez et activez un environnement virtuel :

    ```sh
    python -m venv venv
    source venv/bin/activate  # Sur Windows: venv\Scripts\activate
    ```

3. Installez les dépendances :

    ```sh
    pip install -r requirements.txt
    ```

4. Appliquez les migrations de la base de données :

    ```sh
    python manage.py migrate
    ```

5. Ajoutez des images pour les candidats :

    - Créez un dossier `media/candidats_photos/` dans le répertoire racine du projet.
    - Ajoutez les images des candidats dans ce dossier. Les images doivent être nommées de manière à correspondre aux candidats dans la base de données.

6. Démarrez le serveur de développement :

    ```sh
    python manage.py runserver
    ```


## Fonctionnalités

- Gestion des utilisateurs (étudiants)
- Création et gestion des élections
- Système de vote sécurisé
- Ajout des délégués de classe par l'administrateur
- Ajout des candidats aux élections par l'administrateur

## Contribution

Les contributions sont les bienvenues ! Veuillez soumettre une pull request ou ouvrir une issue pour discuter des changements que vous souhaitez apporter.

## Licence

Ce projet est sous licence MIT. Voir le fichier LICENSE pour plus de détails.
