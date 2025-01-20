"""
Export mongo database to a json file
"""
import json
from pymongo import MongoClient

# Configuration de la connexion MongoDB
MONGO_URI = "mongodb://admin:securepassword@localhost:27017/"
DB_NAME = "opendatalens"
COLLECTION_NAMES = ("commerce", "evenement")
OUTPUT_FILE = "opendatalens_dump.json"

print("Connexion à la base de données")

# Connexion au serveur MongoDB
client = MongoClient(MONGO_URI)
db = client[DB_NAME]

data = {}

print("Récupération des données")

# Get data
for collection_name in COLLECTION_NAMES:
    print(f"Récupération pour {collection_name}")
    collection = db[collection_name]
    cursor = collection.find({})  # Empty query
    documents = list(cursor)
    for doc in documents:
        doc.pop('_id')  # ObjectId is not serializable
    data[collection_name] = documents

print(f"Export dans {OUTPUT_FILE}")

# Export data
with open(OUTPUT_FILE, "w", encoding="utf-8") as file:
    json.dump(data, file, ensure_ascii=False, indent=4)

print("Export terminé !")
