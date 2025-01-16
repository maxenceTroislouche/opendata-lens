import csv

from database import MongoDatabase
from models import Commerce

# https://www.data.gouv.fr/fr/datasets/base-nationale-des-commerces-ouverte/#/community-reuses

def main():
    print("Début tâche commerces")

    liste_commerces = []
    first_row = True
    with open('./data.csv', 'r', encoding="utf-8") as file:
        csv_reader = csv.reader(file, delimiter=";")
        for row in csv_reader:
            if first_row:
                first_row = False
                continue

            if row[19] != "Lens":
                continue

            print(row)
            liste_commerces.append(Commerce.build(row))

    db = MongoDatabase()
    db.insert_shops(liste_commerces)
    db.close()

    print(liste_commerces)

if __name__ == "__main__":
    main()
