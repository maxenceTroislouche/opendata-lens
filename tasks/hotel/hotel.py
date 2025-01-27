import pandas as pd
from pymongo import MongoClient

# Configuration MongoDB
MONGO_URI = "mongodb://admin:securepassword@localhost:27017/"
DB_NAME = "opendatalens"
COLLECTION_NAME = "commerce"

# Charger le fichier CSV pour en examiner le contenu
input_file = "data.csv"
data = pd.read_csv(input_file)

# Charger les données
data = pd.read_csv(input_file)

# Reformater les données
formatted_data = pd.DataFrame({
    "Nom": data["nom_etabl"],
    "Adresse": data["adresse"] + ", " + data["ville"] + " " + data["cp"].astype(str),
    "Mail": data["e_mail"],  # Pas d'information sur les emails dans le fichier
    "Type": "Hébergement",  # Statique pour ce fichier
    "Longitude": data["X"],
    "Latitude": data["Y"]
})

# Connexion à MongoDB
client = MongoClient(MONGO_URI)
db = client[DB_NAME]
collection = db[COLLECTION_NAME]

# Exporter les données formatées dans un nouveau fichier CSV
documents = formatted_data.to_dict(orient="records")
collection.insert_many(documents)

