import requests
import json

from database import MongoDatabase
from models import Salle, Evenement


def get_events_json():
    BASE_URL = "https://billetterie.villedelens.fr/event_search_bis"
    BASE_HEADERS = {'User-Agent': 'Mozilla/5.0'}

    form_data = {
        "selection_all": 1,
        "lng": 1
    }

    response = requests.post(BASE_URL, data=form_data, headers=BASE_HEADERS)

    if response.status_code == 200:
        return json.loads(response.text)

    raise Exception(f"Erreur lors de l'appel à l'url: {BASE_URL}")


def main():
    print("Début tâche spectacles ...")

    events = get_events_json()

    liste_salles = [Salle.build(salle_data) for salle_data in events["vcalendar"]["VLISTE_SALLES"]]
    print(liste_salles)

    liste_events = [Evenement.build(event_data, liste_salles) for event_data in events["vcalendar"]["VEVENT"]]
    print(liste_events)

    db = MongoDatabase()
    db.insert_events(liste_events)
    db.close()

    print("Fin tâche spectacles")


if __name__ == "__main__":
    main()
