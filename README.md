# Révision de concepts de programmation 1

Ce dépôt contient un petit programme de comptabilité personnelle écrit en
Python. Il est toutefois très incomplet et pas très bien écrit. En utilisant les concepts
appris dans le cours de Concepts de programmation 1, vous devez améliorer ce
programme.

## Objectifs pédagogiques

- Utiliser les classes et la programmation orientée objet pour bien structurer
  le code.
- Utiliser les exceptions pour gérer les erreurs.
- Coder de façon modulaire en utilisant des fonctions et des modules.
- Lire et écrire des fichiers.

## Énoncé

### Séance 1 : Comprendre le code existant et l'améliorer (3h)

Dans un premier temps, vous devez comprendre le code existant. Voici les étapes à suivre :

1. Faire une duplication (fork) de ce dépôt dans votre compte GitHub.
2. Cloner votre duplication (fork) sur votre machine locale.
3. Exécuter le code pour voir comment il fonctionne (`uv run piledger`)
4. Lire le code existant pour comprendre son fonctionnement.

Ensuite, vous devez l'améliorer en suivant les consignes ci-dessous. Vous pouvez
faire ces améliorations dans l'ordre que vous souhaitez.

- Répartir le code en plusieurs modules pour améliorer la lisibilité.
- Ajouter des commentaires et des docstrings pour expliquer le code.
- Utiliser les bonnes structures de données (set, dict, list).
- Utiliser des classes pour représenter les concepts principaux (par exemple, une
  classe `Transaction` pour représenter une transaction financière) au lieu
  d'utiliser des dictionnaires.
- Utiliser des exceptions pour gérer les erreurs (par exemple, lors de la lecture
  d'un fichier).
- Améliorer la lecture du fichier CSV en utilisant le module `csv` de la bibliothèque
  standard. Même chose pour l'exportation des écritures d'un compte.
- Simplifier les boucles et les conditions pour les rendre plus lisibles.
- Ajouter les annotations de types.
- Tout autre amélioration que vous jugez pertinente.

**À la fin de cette séance, vous faites un pull request (PR) vers ce dépôt original.**

### Séance 2 : Révision par les pairs

#### Révision par les pairs (environ 1h30)

En groupe de 5, vous devez faire une révision des PR des autres membres de votre groupe. Voici les étapes à suivre :

1. Cloner le dépôt de votre collègue sur votre machine locale ou lire le code en ligne.
2. Laisser des commentaires constructifs sur la PR de votre collègue.

#### Correction de la PR (environ 1h30)

Par la suite, chaque membre doit corriger sa propre PR en fonction des
commentaires reçus. Vous pouvez choisir d'implémenter ou non les suggestions
faites par vos collègues, mais vous devez formuler une réponse dans les
commentaires de la PR pour expliquer vos choix.

Lorsque vous modifiez votre code dans la branche utilisée pour la pull request,
celle-ci sera automatiquement mise à jour.

## Retour par l'enseignant

Après la séance 2, je vais réviser les PR et faire un retour en classe lors du
prochain cours.
