# URL Checker

Petit outil codé en Django pour monitorer des URLs.

## Fonctionnalitées

Ce projet permettra de monitorer des URLs.

- [ ] De pouvoir renseigner des URLs et leur responsabilité métier (qu'une erreur n'envoie pas juste l'URL www.google.com/admin mais également "Partie Admin Google")
- [ ] De pouvoir logguer toutes les vérifications (ayant entrainées une erreur ou non)
- [ ] De définir des critères d'erreur :
    - [ ] Code HTTP
    - [ ] présence de texte sur la page
    - [ ] temps de réponse
    - [ ] validation du certificat SSL
    - [ ] délai en j avant expiration
- [ ] L'envoi d'un mail pour les sites ayant été en erreur avec des infos sur les erreurs si possible.
- [ ] Créer un module d'administration complet.

## Installation

Pour pouvoir installer le projet il faut avoir installé precedement `python3`, `python3-venv` et `pip`
``` bash
# TODO : Complete with correct repo name/url
git clone https://github.com/plezan/urlChecker
cd urlChecker
python3 -m venv ../venv_urlChecker
source ../venv_urlChecker/bin/activate
pip install -r requirements.txt
```

configuration du projet
```
cp urlChecker/example_dev_settings.py urlChecker/local_settings.py
python manage.py migrate
```

## Evaluation

Ce projet a été réalisé pour une évaluation sur l'utilisation des fonctionnalités de Django :

- Utilisation des CBV, ModelForm ou formulaires Django
- Utilisation des models, urls
- Qualité de conception et développement
- La lisibilité du code compte. Un code lisible est un code maintenable.
- Le front-end compte pour très peu dans l'évaluation, concentrez-vous sur le - back-end et l'utilisation de Django.
- Il est important de bien peaufiner ses models. Ils sont la base du projet.

> Toutes les fonctionnalités ne sont pas demandées. Vous pouvez d'ailleurs imaginer d'autres fonctionnalités. Le but est d'expérimenter Django. Ajouter les champs qui vous semblent utiles. 
