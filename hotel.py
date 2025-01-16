import pandas as pd

# Charger le fichier CSV pour en examiner le contenu
input_file = "data/HA9bergements_touristiques.csv"
data = pd.read_csv(input_file)

import pandas as pd

output_file = "formatted_hotel.csv"

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

# Exporter les données formatées dans un nouveau fichier CSV
formatted_data.to_csv(output_file, index=False, sep=";")

print(f"Données formatées et enregistrées dans {output_file}")

