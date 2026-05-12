# README

Dépôt contenant les TPs python selenium.

## TP1

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
Veuillez créer localement ce fichier par vous même avec vos credentials (le fichier credentials.yaml est contenu dans le fichier [.gitignore](.gitignore)) ou remplacez les lignes correspondantes dans le fichier [pages/login_page.py](pages/login_page.py)

````
# credentials.yaml
credentials:
    LOGIN : "your_login"
    PASSWORD : "your_password"
````


```
# login_page.py
# class LoginPage(BasePage):
USERNAME = credentials["credentials"]["USERNAME"]
PASSWORD = credentials["credentials"]["PASSWORD"]
```

## Lancer le projet

Pour lancer le projet, rendez vous dans le dossier TP1, puis lancez le fichier [main.py](TP1/main.py).

#### Exemple

````
cd TP1
python main.py
````

Si vous souhaitez exécuter une partie du projet en particulier, utilisez un argument parmi "login", "dropdown" ou "add_remove_element". Par défaut, le projet execute l'argument "all" qui execute toutes les parties en même temps.

#### Exemple

```
# Pour n'executer que la partie "login"
python main.py -t "login"
```

### Nettoyer dossier screenshots/


Pour nettoyer le dossier screenshots/ qui accumule des captures d'écran en cas d'erreur, executez le fichier clean_screenshots.sh (pour MacOS et Linux). Pour Windows, créez un fichier .bat qui permet de supprimer le contenu du dossier TP1/screenshots/ qui se créera automatiquement à l'execution du projet.

#### Exemple

```
# Depuis le dossier racine
cd TP1
sh clean_screenshots.sh
```

## TP2

Pour lancer le TP2, effectuez les mêmes actions, en prenant soin de se rendre dansl e dossier TP2 au lieu du dossier TP1.
Les arguments du fichier main.py sont désormais "dynamics_controls" , WIP.

