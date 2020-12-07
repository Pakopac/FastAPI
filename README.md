# FastAPI
## Installation

```
pip install fastapi
```

```
pip install uvicorn
```

## run

```
uvicorn main:app --reload
```

## Route

Une route est un endroit spécifique de l'application qui va être appelé par l'utilisateur et qui va renvoyer un résultat. il existe plusieurs méthodes pour appeler ces routes mais les deux plus utilisé sont GET qui va récupérer le contenu et l'afficher et POST qui permet d'envoyer des données à la route.

## Fonction async

Une fonction asynchrone permet d'executer du code de manière asynchrone c'est à dire que contrairement à une fonction normale le code ne va pas s'executer ligne par ligne en attendant que l'execution de chaque ligne soit terminée, on peut donc executer plusieurs lignes à la fois

## Uvicorn

Uvicorn est une implémentation de serveur ASGI, c'est une interface serveur / application de bas niveau minimale pour les frameworks asyncio.

## Gunicorn

Gunicorn est un serveur HTTP Python WSGI pour UNIX. C'est un serveur compatible avec divers framework web, implémenté simplement, léger sur les ressources du serveur et assez rapide.

## BaseModel

BaseModel est le modèle de base a importer dans FastAPI il permet d'importer tous les autres modèles (les modèles héritent de BaseModel).
On l'utilise en l'important et en la mettant en argument d'une classe:
```
from pydantic import BaseModel

class User(BaseModel):
    ...
```