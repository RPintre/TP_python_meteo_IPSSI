# Analyse Météo Montpellier

Ce script Python permet de récupérer, analyser et visualiser des données météo historiques pour Montpellier. Il peut aussi générer un rapport complet et afficher des graphiques.

## Fonctionnalités

- Téléchargement automatique des données depuis l’API Open-Meteo.
- Stockage des données dans un CSV (`meteo_montpellier.csv`).
- Analyse des données : températures moyennes, humidité moyenne, jours de pluie, températures mini/maxi.
- Affichage de graphiques pour températures et précipitations.
- Génération d’un rapport complet pouvant être sauvegardé dans un fichier texte.
- Menu simple pour choisir ce qu’on veut faire.

## Modules nécessaires

Le script utilise les modules suivants :  

- `requests`  
- `matplotlib`  
- `csv`  
- `os`  

Assurez-vous que ces modules sont installés avant d’exécuter le script.

## Utilisation

1. Télécharger ou copier le script sur votre machine.
2. Lancer le script.
3. Suivre le menu interactif :

- **1** : Afficher un échantillon des données.  
- **2** : Calculer la moyenne des températures.  
- **3** : Vérifier s’il a plu à une date donnée.  
- **4** : Trouver la température minimale.  
- **5** : Trouver la température maximale.  
- **6** : Compter le nombre de jours de pluie.  
- **7** : Générer un rapport complet.  
- **8** : Afficher le graphique des températures.  
- **9** : Afficher le graphique des précipitations.  
- **10** : Enregistrer le rapport dans un fichier texte.  
- **0** : Quitter.  

> Lors du téléchargement, il demande une date de début. Si rien n’est saisi, il prend `01-01-2025` par défaut.

## Comment ça marche

- `download_meteorological_data()` : télécharge les données depuis l’API et les sauvegarde.  
- `dataMeteo` : classe pour stocker les infos du jour (température, pluie, humidité…).  
- Fonctions d’analyse : calcul de moyennes, températures mini/maxi, jours de pluie.  
- Fonctions graphiques : affichage des températures et précipitations avec matplotlib.  
- `rapportComplet()` : génère un résumé complet de la période.  
- `menu()` : interface utilisateur pour lancer toutes les fonctions facilement.  

## Remarques

- Les fichiers CSV et TXT sont enregistrés dans le même dossier que le script.  
- Les dates dans le menu doivent être au format **JJ-MM-AAAA**.  
- Les graphiques s’ouvrent dans une fenêtre externe (fermer pour revenir au menu).  
