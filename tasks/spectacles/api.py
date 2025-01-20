import abc
import requests
from models import Evenement


class BaseEventGetter(abc.ABC):
    @abc.abstractmethod
    def run(self) -> list[Evenement]:
        pass

class TicketMasterEventGetter(BaseEventGetter):
    API_KEY = "nXl77hUTalCO6opfzFDmJ3S6mqHvV8aK"
    POSTAL_CODE = "62300"
    EVENTS_URL = f"https://app.ticketmaster.com/discovery/v2/events?apikey={API_KEY}&postalCode={POSTAL_CODE}&locale=*&size=200&city=Lens&countryCode=FR"
    PARAMS = {}

    def _call_api(self) -> dict:
        response = requests.get(self.EVENTS_URL, params=self.PARAMS)

        if response.status_code != 200:
            raise Exception(f"Une erreur est survenue lors de la requete à : {self.EVENTS_URL}")

        return response.json()

    def run(self) -> list[Evenement]:
        data = self._call_api()
        api_events = data.get("_embedded", {}).get("events", [])
        events = []

        for event in api_events:
            new_event = Evenement(
                date=event.get("dates").get("start").get("localDate"),
                heure=event.get("dates").get("start").get("localTime"),
                duree=-1,
                nom=event.get("name"),
                type="SPECTACLE",
                description=event.get("description"),
                adresse=event.get('_embedded', {}).get('venues', [])[0].get('name'),
                longitude=event.get("_embedded", {}).get("venues")[0].get("location", {}).get("longitude"),
                latitude=event.get("_embedded", {}).get("venues")[0].get("location", {}).get("latitude"),
                image=event.get("images")[0].get("url")
            )

            if "KASTELET" in new_event.adresse:
                new_event.longitude = 2.8212238
                new_event.latitude = 50.4259397

            events.append(new_event)

        return events

class RCLEventGetter(BaseEventGetter):
    EVENTS_URL = "https://www.rclens.fr/fr/calendar-results/ajax/10037"
    DESIRED_STADIUM = "Stade Bollaert-Delelis"  # Remplacez par le nom réel du stade

    def _call_api(self) -> dict:
        response = requests.get(self.EVENTS_URL)
        if response.status_code != 200:
            raise Exception("Erreur lors de l'appel à l'api RCLens")
        
        return response.json()
    
    def _filter_data(self, data: dict) -> list:
        filtered_events = []
        for event in data.get("matchs", []):
            if event.get("stadium") == self.DESIRED_STADIUM:
                filtered_events.append(event)

        return filtered_events


    def run(self) -> list[Evenement]:
        data = self._call_api()
        api_events = self._filter_data(data)
        events = []

        for event in api_events:
            new_event = Evenement(
                date=event.get("date", {}).get("time").split(" ")[0],
                heure=event.get("date", {}).get("time").split(" ")[1],
                duree=-1,
                nom=f"{event.get("home_team")} - {event.get("away_team")}",
                type="MATCH",
                description=f"Match {event.get("home_team")} contre {event.get("away_team")}",
                adresse=self.DESIRED_STADIUM,
                longitude=2.81497,  # Fixed
                latitude=50.43285,  # Fixed
                image=event.get("competition_logo")
            )
            events.append(new_event)
        
        return events

