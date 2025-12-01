import csv
import requests
import os
import matplotlib.pyplot as plt

# Fonction pour trouver le chemin complet d'un fichier donné
def find_file(filename, start_dir="."):
    """Recherche récursive d'un fichier dans un répertoire donné.
    Args:
        filename (str): Le nom du fichier à rechercher.
        start_dir (str): Le répertoire de départ pour la recherche.
        Returns:
        str: Le chemin complet du fichier s'il est trouvé, sinon None.
    """
    for root, dirs, files in os.walk(start_dir):
        if filename in files:
            return os.path.join(root, filename)
    return None

# Fonction pour obtenir la date d'aujourd'hui au format YYYY-MM-DD
def getTodayDate():
    """Obtient la date d'aujourd'hui au format YYYY-MM-DD.
    Returns:
        str: La date d'aujourd'hui au format YYYY-MM-DD.
    """
    from datetime import date
    today = date.today()
    return today.strftime("%Y-%m-%d")

# Fonction pour télécharger les données météorologiques
def download_meteorological_data():
    """Télécharge les données météorologiques historiques pour Montpellier depuis l'API Open-Meteo et les enregistre dans un fichier CSV.
    """
    today= getTodayDate()
    dateDebut=input("Entrez la date de début (DD-MM-YYYY) defaut(01-01-2025) : ")
    if not dateDebut:
        dateDebut = "2025-01-01"
    else:
        dateDebut = "-".join(dateDebut.split("-")[::-1])  # Convertir en format YYYY-MM-DD
    url = "https://archive-api.open-meteo.com/v1/archive"
    params = {
        "latitude": 43.6119,
        "longitude": 3.8772,
        "start_date": dateDebut,
        "end_date": today,
        "daily": "temperature_2m_min,temperature_2m_max,precipitation_sum,relative_humidity_2m_mean",
        "timezone": "Europe/Paris",
        "format": "csv"
    }
    try:
        response = requests.get(url, params=params)
    except Exception as e:
        print("Erreur lors de la requête :", e)
        return
    
    fichier_csv = find_file("meteo_montpellier.csv")
    # Vérification
    if response.status_code == 200:
        with open(fichier_csv, "w") as f:
            f.write(response.text)
        print("CSV téléchargé : meteo_montpellier.csv")
    else:
        print("Erreur :", response.status_code, response.text)

# Classe pour stocker les données météorologiques
class dataMeteo:
    """Classe pour stocker les données météorologiques quotidiennes.
        Attributes:
            date (str): La date des données météorologiques.
            temperature_min (float): La température minimale.
            temperature_max (float): La température maximale.
            precipitations (float): Les précipitations.
            humidite (float): L'humidité moyenne.
        Methods:
            __init__(self, date, tmin, tmax, precip, humid): Initialise une instance de dataMeteo avec les données fournies.    
    """
    def __init__(self, date, tmin, tmax, precip, humid):
        self.date = date
        self.temperature_min = float(tmin)
        self.temperature_max = float(tmax)
        self.precipitations = float(precip)
        self.humidite = float(humid)

# Fonction pour récupérer et nettoyer les données météorologiques
def recupererDonnees():
    """Récupère et nettoie les données météorologiques depuis le fichier CSV.
    Returns:
        list: Une liste d'instances de dataMeteo contenant les données nettoyées.
    """
    download_meteorological_data()
    reader = None
    with open(find_file("meteo_montpellier.csv"), 'r') as recupCSV:
        reader = csv.reader(recupCSV)
        dataSetMeteo = list(reader)
        dataSetMeteoClean = []
        for i, row in enumerate(dataSetMeteo):
            if i >= 4: 
                meteo = dataMeteo(date=row[0], tmin=row[1], tmax=row[2], precip=row[3], humid=row[4])
                dataSetMeteoClean.append(meteo) 
        return dataSetMeteoClean

# Fonctions d'analyse des données météorologiques
def affichageDonneesMeteoSample(data, n=20):
    """Affiche un échantillon des données météorologiques.
    Args:
        data (list): La liste des données météorologiques.
        n (int): Le nombre d'entrées à afficher (par défaut 20).
    """
    n_input = input("Combien d'entrées afficher ? (par défaut 20) : ")
    n = int(n_input) if n_input.isdigit() else n
    print(f"Affichage des {n} premières entrées des données météorologiques :")
    for i, meteo in enumerate(data[:n], start=1):
        print(f"Numero {i}: Date: {formatDateFR(meteo.date)}, Température min: {meteo.temperature_min}°C, Température max: {meteo.temperature_max}°C, Précipitations: {meteo.precipitations} mm, Humidité: {meteo.humidite} %")
    input("Appuyez sur Entrée pour continuer...")

# Calcul de la moyenne des températures
def moyenneTemperatures(data):
    """Calcule la température moyenne à partir des données météorologiques.
    Args:
        data (list): La liste des données météorologiques.
    Returns:
        float: La température moyenne.
    """
    total_temp = 0
    count = 0
    for meteo in data:
        total_temp += (float(meteo.temperature_min) + float(meteo.temperature_max)) / 2
        count += 1
    return total_temp / count if count > 0 else 0

# Calcul de l'humidité moyenne
def humiditeMoyenne(data):
    """Calcule l'humidité moyenne à partir des données météorologiques.
    Args:
        data (list): La liste des données météorologiques.
    Returns:
        float: L'humidité moyenne.
    """
    total_humidite = 0
    count = 0
    for meteo in data:
        total_humidite += float(meteo.humidite)
        count += 1
    return total_humidite / count if count > 0 else 0


# Vérification s'il a plu à une date donnée
def ilAplu(data, date):
    """Vérifie s'il a plu à une date donnée.
    Args:
        data (list): La liste des données météorologiques.
        date (str): La date à vérifier au format YYYY-MM-DD.
    Returns:
        bool or None: True s'il a plu, False s'il n'a pas plu, None si la date n'est pas trouvée.
    """
    for meteo in data:
        if meteo.date == date:
            return True if float(meteo.precipitations) >= 0.1 else False
    return None

# Trouver la température minimale
def temperatureMinimale(data):
    """Trouve la température minimale à partir des données météorologiques.
    Args:
        data (list): La liste des données météorologiques.
    Returns:
        float or None: La température minimale, ou None si les données sont vides.
    """
    min_temp = float('inf')
    for meteo in data:
        temp = float(meteo.temperature_min)
        if temp < min_temp:
            min_temp = temp
    return min_temp if min_temp != float('inf') else None

# Trouver la température maximale
def temperatureMaximale(data):
    """Trouve la température maximale à partir des données météorologiques.
    Args:
        data (list): La liste des données météorologiques.
    Returns:
        float or None: La température maximale, ou None si les données sont vides.
    """
    max_temp = float('-inf')
    for meteo in data:
        temp = float(meteo.temperature_max)
        if temp > max_temp:
            max_temp = temp
    return max_temp if max_temp != float('-inf') else None

# Compter le nombre de jours de pluie
def nombreJoursDePluie(data):
    """Compte le nombre de jours de pluie à partir des données météorologiques.
    Args:
        data (list): La liste des données météorologiques.
    Returns:
        int: Le nombre de jours de pluie.
    """
    count = 0
    for meteo in data:
        if float(meteo.precipitations) > 0:
            count += 1
    return count

# Trouver le jour le plus chaud
def jourLepluschaud(data):
    """Trouve le jour le plus chaud à partir des données météorologiques.
    Args:
        data (list): La liste des données météorologiques.
    Returns:
        tuple: Le jour le plus chaud et la température maximale.
    """
    max_temp = float('-inf')
    jour = None
    for meteo in data:
        temp = float(meteo.temperature_max)
        if temp > max_temp:
            max_temp = temp
            jour = meteo.date
    return jour, max_temp

# Trouver le jour le plus froid
def jourLeplusfroid(data):
    """Trouve le jour le plus froid à partir des données météorologiques.
    Args:
        data (list): La liste des données météorologiques.
    Returns:
        tuple: Le jour le plus froid et la température minimale.
    """
    min_temp = float('inf')
    jour = None
    for meteo in data:
        temp = float(meteo.temperature_min)
        if temp < min_temp:
            min_temp = temp
            jour = meteo.date
    return jour, min_temp

# Formater une date au format FR
def formatDateFR(date_str):
    """Formate une date au format français (JJ/MM/AAAA).
    Args:
        date_str (str): La date au format YYYY-MM-DD.
    Returns:
        str: La date formatée au format JJ/MM/AAAA.
    """
    jour, mois, annee = date_str.split('-')[2], date_str.split('-')[1], date_str.split('-')[0]
    return f"{jour}/{mois}/{annee}"

# Formater une date au format EN
def formatDateEN(date_str):
    """Formate une date au format anglais (AAAA-MM-JJ).
    Args:
        date_str (str): La date au format YYYY-MM-DD.
    Returns:
        str: La date formatée au format AAAA-MM-JJ.
    """
    annee, mois, jour = date_str.split('-')[0], date_str.split('-')[1], date_str.split('-')[2]
    return f"{annee}-{mois}-{jour}"


def statistiques(data):   
    """Calcule diverses statistiques à partir des données météorologiques.
    Args:
        data (list): La liste des données météorologiques.
    Returns:
        dict: Un dictionnaire contenant les statistiques calculées.
    """
    dataset = {
        "moyenne_temperature": moyenneTemperatures(data),
        "humidite_moyenne": humiditeMoyenne(data),
        "temperature_min": temperatureMinimale(data),
        "temperature_max": temperatureMaximale(data),
        "nombre_jours_pluie": nombreJoursDePluie(data),
        "jour_plus_chaud": jourLepluschaud(data),
        "jour_plus_froid": jourLeplusfroid(data)
    }
    return dataset

# Générer un rapport complet
def rapportComplet(data):
    """Génère un rapport complet à partir des données météorologiques.
    Args:
        data (list): La liste des données météorologiques.
    Returns:
        str: Le rapport complet sous forme de chaîne de caractères.
    """
    dico = statistiques(data)
    jour_froid, temp_froide = formatDateFR(dico["jour_plus_froid"][0]), dico["jour_plus_froid"][1]
    jour_chaud, temp_chaude = formatDateFR(dico["jour_plus_chaud"][0]), dico["jour_plus_chaud"][1]
    rapport=(f"----- RAPPORT MÉTÉO -----\n Date de début : {formatDateFR(data[0].date)} ----- Date de fin : {formatDateFR(data[-1].date)}\n Température moyenne : {round(dico['moyenne_temperature'],2)}°C\n Température minimale : {temp_froide}°C le {jour_froid}\n Température maximale : {temp_chaude}°C le {jour_chaud}\n Humidité moyenne : {round(dico['humidite_moyenne'],2)}% \n Jours de pluie: {dico['nombre_jours_pluie']} jours sur un total de {len(data)} jours\n Ce qui fait {round((dico['nombre_jours_pluie']/len(data))*100,2)}% de jours de pluie sur la période\n------------------------")
    return rapport


# Fonctions pour afficher des graphiques
def afficherGraphiqueTemperatures(data):
    """Affiche un graphique des températures minimales et maximales.
    Args:
        data (list): La liste des données météorologiques.
    """
    dates = [meteo.date for meteo in data]
    temp_min = [float(meteo.temperature_min) for meteo in data]
    temp_max = [float(meteo.temperature_max) for meteo in data]

    plt.figure(figsize=(10, 5))
    plt.plot(dates, temp_min, label='Température Min', color='blue')
    plt.plot(dates, temp_max, label='Température Max', color='red')
    plt.title('Températures à Montpellier')
    plt.xlabel('Date')
    plt.ylabel('Température (°C)')
    plt.legend()
    plt.xticks(rotation=45)
    plt.tight_layout()
    plt.show()

# Fonction pour afficher le graphique des précipitations
def afficherGraphiquePrecipitations(data):
    """Affiche un graphique des précipitations.
    Args:
        data (list): La liste des données météorologiques.
    """
    dates = [meteo.date for meteo in data]
    precipitations = [float(meteo.precipitations) for meteo in data]

    plt.figure(figsize=(10, 5))
    plt.bar(dates, precipitations)
    plt.title('Précipitations à Montpellier')
    plt.xlabel('Date')
    plt.ylabel('Précipitations (mm)')
    plt.xticks(rotation=45)
    plt.tight_layout()
    plt.show()

# Fonction pour créer un fichier rapport en fichier txt
def create_report_file(report):
    """Crée un fichier texte contenant le rapport météorologique.
    Args:
        report (str): Le rapport complet sous forme de chaîne de caractères.
    """
    with open("rapport_meteo.txt", "w", encoding="utf-8") as f:
        f.write(report)
    print("Rapport enregistré dans 'rapport_meteo.txt'")

# Menu interactif pour l'utilisateur
def menu():
    """Affiche un menu interactif pour l'utilisateur afin de réaliser des analyses météorologiques."""
    choix = ''
    data = recupererDonnees()
    while choix != '0':
        print("--------------------------------------------------")
        print("Menu des analyses météorologiques :")
        print("1. Afficher un échantillon des données")
        print("2. Calculer la moyenne des températures")
        print("3. Vérifier s'il a plu à une date donnée")
        print("4. Trouver la température minimale")
        print("5. Trouver la température maximale")
        print("6. Compter le nombre de jours de pluie")
        print("7. Générer un rapport complet")
        print("8. Afficher le graphique des températures")
        print("9. Afficher le graphique des précipitations")
        print("10. Enregistrer le rapport complet dans un fichier")
        print("0. Quitter")
        choix = input("Choisissez une option: ")
    
        if(choix == '1'):
            affichageDonneesMeteoSample(data)
        elif(choix == '2'):
            print("Moyenne des températures :", moyenneTemperatures(data))
            input("Appuyez sur Entrée pour continuer...")
        elif(choix == '3'):
            date = input("Entrez la date (DD-MM-YYYY) : ")
            pluie = ilAplu(data, formatDateEN(date))
            if pluie is not None:
                if pluie:
                    print(f"Il a plu le {date}.")
                else:
                    print(f"Il n'a pas plu le {date}.")
            else:
                print("Date non trouvée dans les données.")
        elif(choix == '4'):
            print("Température minimale :", temperatureMinimale(data))
            input("Appuyez sur Entrée pour continuer...")
        elif(choix == '5'):
            print("Température maximale :", temperatureMaximale(data))
            input("Appuyez sur Entrée pour continuer...")
        elif(choix == '6'):
            print("Nombre de jours de pluie :", nombreJoursDePluie(data))
            input("Appuyez sur Entrée pour continuer...")
        elif(choix == '7'):
            print("Rapport complet :\n", rapportComplet(data))
            input("Appuyez sur Entrée pour continuer...")
        elif(choix == '8'):
            afficherGraphiqueTemperatures(data)
            input("Appuyez sur Entrée pour continuer...")
        elif(choix == '9'):
            afficherGraphiquePrecipitations(data)
            input("Appuyez sur Entrée pour continuer...")
        elif(choix == '10'):
            report = rapportComplet(data)
            create_report_file(report)
            input("Appuyez sur Entrée pour continuer...")
        elif(choix == '0'):
            print("Au revoir!")

# Lancer le menu si le script est exécuté directement
if __name__ == "__main__":
    menu()