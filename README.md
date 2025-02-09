# Election App

Une application web pour gérer les élections étudiantes.

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
    git clone https://github.com/votre-utilisateur/election_app.git
    cd election_app
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
    python backend/manage.py migrate
    ```

5. Démarrez le serveur de développement :

    ```sh
    python backend/manage.py runserver
    ```

## Structure du projet

- [backend](http://_vscodecontentref_/0) : Contient le code source du backend Django.
  - [backend](http://_vscodecontentref_/1) : Configuration principale du projet Django.
  - [core/](http://_vscodecontentref_/2) : Application principale avec les modèles et vues de base.
  - `students/` : Application pour gérer les étudiants.
  - `votes/` : Application pour gérer les votes.
- [frontend](http://_vscodecontentref_/3) : Contient les fichiers statiques (HTML, CSS, JavaScript).
- [requirements.txt](http://_vscodecontentref_/4) : Liste des dépendances Python.
- [README.md](http://_vscodecontentref_/5) : Documentation du projet.

## Fonctionnalités

- Gestion des utilisateurs (étudiants)
- Création et gestion des élections
- Système de vote sécurisé

## Contribution

Les contributions sont les bienvenues ! Veuillez soumettre une pull request ou ouvrir une issue pour discuter des changements que vous souhaitez apporter.

## Licence

Ce projet est sous licence MIT. Voir le fichier LICENSE pour plus de détails.