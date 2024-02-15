# NitroGenerator

Le NitroGenerator est un script simple en Python qui interagit avec l'API Discord pour générer des jetons cadeaux Nitro. Ce script utilise l'API Discord des promotions partenaires pour créer des demandes de réalisation et obtenir des jetons Nitro.

## Description

Ce script Python permet de solliciter l'API Discord afin de générer des jetons Nitro pour les cadeaux. Il utilise la fonction de promotion des partenaires Discord pour obtenir ces jetons et les affiche pour utilisation ultérieure.

## Requirement 

Le navigateur Opera gx est requis pour ce git.

Compte PayPal avec carte bleue associé.

## Fonctionnalités

- Interaction avec l'API Discord pour générer des jetons Nitro.
- Affichage du jeton généré ainsi que d'une URL contenant le jeton.
- Utilisation simple avec une saisie de l'ID de l'utilisateur partenaire.

1. Exécutez le script dans un environnement Python.

### Kali Linux
```bash
pip install requests
git clone https://github.com/LucasTylczak/NitroGenerator/
cd NitroGenerator
python3 generateur_nitro.py
```
### Windows Powershell
```bash
pip install requests
git clone https://github.com/LucasTylczak/NitroGenerator/
cd .\NitroGenerator\
python .\generateur_nitro.py

```
2. Entrez l'ID de le partnerUserId lorsqu'on vous le demande.

### Trouver le partnerUserId
[Aide pour le partnerUserId](https://drive.google.com/file/d/1BGZqmuAbGrN6c43arhMngLd9mhrL4tgo/view?usp=sharing)

4. Le script fera une requête à l'API Discord et récupérera un jeton Nitro.

5. Le jeton généré sera affiché avec une URL contenant le jeton.

6. N'oubliez pas de dissocier par la suite votre compte PayPal à votre compte discorde.

## Avertissement

Ce script est fourni à des fins éducatives uniquement. Utilisez-le de manière responsable et respectez les conditions d'utilisation de Discord. Je ne suis pas responsable de tout abus ou conséquence résultant de l'utilisation de ce script.
