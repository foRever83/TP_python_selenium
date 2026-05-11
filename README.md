# README

## Dépôt contenant les TPs python selenium.

### Initialiser l'environnement du projet

Afin de faire fonctionner ce projet correctement, pensez à créer un environement virtuel Python et d'ajouter les dépendances contenues dans le fichier [Requirements.txt](Requirements.txt).
Depuis la base du projet :

```
python -m venv .venv
# Sur mac
source /Scripts/Activate
pip install -r Requirements.txt
```

### Ajout des credentials

Par mesure de sécurité, les login et mot de passe ont été sauvegardés dans un fichier yaml, nommé par défaut *credentials.yaml* qui n'a pas été ajouté à ce fichier.
Veuillez créer localement ce fichier par vous même avec vos credentials (le fichier crednetials.yaml est contenu dans le fichier [.gitignore](.gitignore)) ou remplacez les lignes correspondantes dans le fichier [base_page.py](base_page.py)

````
# credentials.yaml
credentials:
    LOGIN : "your_login"
    PASSWORD : "your_password"
````


```
# base-page.py
# class BasePage:
USERNAME = credentials["credentials"]["USERNAME"]
PASSWORD = credentials["credentials"]["PASSWORD"]
```