# ue19-lab-05 – Joke app

Petite application Python 3 qui interroge l'API publique [JokeAPI](https://v2.jokeapi.dev/) avec la librairie `requests` et affiche une blague aléatoire.

## Fonctionnalités
- Récupère une blague aléatoire (mode "safe") depuis JokeAPI
- Gère les deux formats de blague : en une ligne, ou question + chute

## Fichiers
- `app.py` : le programme qui interroge l'API
- `requirements.txt` : les dépendances (`requests`)
- `Dockerfile` : construit l'image du conteneur qui exécute `app.py`

## Installation et lancement sans Docker
Prérequis : Python 3

```bash
pip install -r requirements.txt
python app.py
```

## Lancement avec Docker
Prérequis : Docker

```bash
docker build -t ue19-lab-05 .
docker run --rm ue19-lab-05
```
