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

## Documentation des fonctions et classes

# Functions

`affichageDonneesMeteoSample(data, n=20)`
:   Affiche un échantillon des données météorologiques.
    Args:
        data (list): La liste des données météorologiques.
        n (int): Le nombre d'entrées à afficher (par défaut 20).

`afficherGraphiquePrecipitations(data)`
:   Affiche un graphique des précipitations.
    Args:
        data (list): La liste des données météorologiques.

`afficherGraphiqueTemperatures(data)`
:   Affiche un graphique des températures minimales et maximales.
    Args:
        data (list): La liste des données météorologiques.

`create_report_file(report)`
:   Crée un fichier texte contenant le rapport météorologique.
    Args:
        report (str): Le rapport complet sous forme de chaîne de caractères.

`download_meteorological_data()`
:   Télécharge les données météorologiques historiques pour Montpellier depuis l'API Open-Meteo et les enregistre dans un fichier CSV.

`find_file(filename, start_dir='.')`
:   Recherche récursive d'un fichier dans un répertoire donné.
    Args:
        filename (str): Le nom du fichier à rechercher.
        start_dir (str): Le répertoire de départ pour la recherche.
        Returns:
        str: Le chemin complet du fichier s'il est trouvé, sinon None.

`formatDateEN(date_str)`
:   Formate une date au format anglais (AAAA-MM-JJ).
    Args:
        date_str (str): La date au format YYYY-MM-DD.
    Returns:
        str: La date formatée au format AAAA-MM-JJ.

`formatDateFR(date_str)`
:   Formate une date au format français (JJ/MM/AAAA).
    Args:
        date_str (str): La date au format YYYY-MM-DD.
    Returns:
        str: La date formatée au format JJ/MM/AAAA.

`getTodayDate()`
:   Obtient la date d'aujourd'hui au format YYYY-MM-DD.
    Returns:
        str: La date d'aujourd'hui au format YYYY-MM-DD.

`humiditeMoyenne(data)`
:   Calcule l'humidité moyenne à partir des données météorologiques.
    Args:
        data (list): La liste des données météorologiques.
    Returns:
        float: L'humidité moyenne.

`ilAplu(data, date)`
:   Vérifie s'il a plu à une date donnée.
    Args:
        data (list): La liste des données météorologiques.
        date (str): La date à vérifier au format YYYY-MM-DD.
    Returns:
        bool or None: True s'il a plu, False s'il n'a pas plu, None si la date n'est pas trouvée.

`jourLepluschaud(data)`
:   Trouve le jour le plus chaud à partir des données météorologiques.
    Args:
        data (list): La liste des données météorologiques.
    Returns:
        tuple: Le jour le plus chaud et la température maximale.

`jourLeplusfroid(data)`
:   Trouve le jour le plus froid à partir des données météorologiques.
    Args:
        data (list): La liste des données météorologiques.
    Returns:
        tuple: Le jour le plus froid et la température minimale.

`menu()`
:   Affiche un menu interactif pour l'utilisateur afin de réaliser des analyses météorologiques.

`moyenneTemperatures(data)`
:   Calcule la température moyenne à partir des données météorologiques.
    Args:
        data (list): La liste des données météorologiques.
    Returns:
        float: La température moyenne.

`nombreJoursDePluie(data)`
:   Compte le nombre de jours de pluie à partir des données météorologiques.
    Args:
        data (list): La liste des données météorologiques.
    Returns:
        int: Le nombre de jours de pluie.

`rapportComplet(data)`
:   Génère un rapport complet à partir des données météorologiques.
    Args:
        data (list): La liste des données météorologiques.
    Returns:
        str: Le rapport complet sous forme de chaîne de caractères.

`recupererDonnees()`
:   Récupère et nettoie les données météorologiques depuis le fichier CSV.
    Returns:
        list: Une liste d'instances de dataMeteo contenant les données nettoyées.

`statistiques(data)`
:   Calcule diverses statistiques à partir des données météorologiques.
    Args:
        data (list): La liste des données météorologiques.
    Returns:
        dict: Un dictionnaire contenant les statistiques calculées.

`temperatureMaximale(data)`
:   Trouve la température maximale à partir des données météorologiques.
    Args:
        data (list): La liste des données météorologiques.
    Returns:
        float or None: La température maximale, ou None si les données sont vides.

`temperatureMinimale(data)`
:   Trouve la température minimale à partir des données météorologiques.
    Args:
        data (list): La liste des données météorologiques.
    Returns:
        float or None: La température minimale, ou None si les données sont vides.

# Classes

`dataMeteo(date, tmin, tmax, precip, humid)`
:   Classe pour stocker les données météorologiques quotidiennes.
    Attributes:
        date (str): La date des données météorologiques.
        temperature_min (float): La température minimale.
        temperature_max (float): La température maximale.
        precipitations (float): Les précipitations.
        humidite (float): L'humidité moyenne.
    Methods:
        __init__(self, date, tmin, tmax, precip, humid): Initialise une instance de dataMeteo avec les données fournies.