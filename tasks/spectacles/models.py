class Salle:
    id: int
    nom: str
    adresse1: str
    adresse2: str
    code_postal: str
    ville: str
    telephone: str

    def __init__(self, id: int, nom: str, adresse1: str, adresse2: str, code_postal: str, ville: str, telephone: str):
        self.id = id
        self.nom = nom
        self.adresse1 = adresse1
        self.adresse2 = adresse2
        self.code_postal = code_postal
        self.ville = ville
        self.telephone = telephone

    def __str__(self):
        return f"Salle: {self.nom} - {self.ville}"

    def __repr__(self):
        return self.__str__()

    @staticmethod
    def build(event_dict: dict) -> "Salle":
        return Salle(
            id=event_dict["id_salle"],
            nom=event_dict["nom"],
            adresse1=event_dict["adresse1"],
            adresse2=event_dict["adresse2"],
            code_postal=event_dict["code_postal"],
            ville=event_dict["ville"],
            telephone=event_dict["telephone"]
        )

class Evenement:
    date: str
    heure: str
    duree: int
    nom: str
    type: str
    description: str
    adresse: str
    longitude: float
    latitude: float
    image: str

    def __init__(self, date: str, heure: str, duree: int, nom: str, type: str, description: str, adresse: str, longitude: float, latitude: float, image: str):
        self.date = date
        self.heure = heure
        self.duree = duree
        self.nom = nom
        self.type = type
        self.description = description
        self.adresse = adresse
        self.longitude = longitude
        self.latitude = latitude
        self.image = image

    def __str__(self):
        return f"Evenement: {self.nom} - {self.adresse}"

    def __repr__(self):
        return self.__str__()

    @staticmethod
    def build(event_dict: dict, liste_salles: list[Salle]) -> "Evenement":
        salle = None
        for s in liste_salles:
            if s.id in event_dict["X_RSI_ID_SALLES"]:
                salle = s
                break

        if salle is None:
            raise Exception(f"Impossible de trouver la salle pour l'événement: {event_dict['nom']}")

        return Evenement(
            date="01/01/2026",  # TODO: Récupérer l'info
            heure="20h00",  # TODO: Récupérer l'info
            duree=123,  # TODO: Récupérer l'info
            nom=event_dict["SUMMARY"],
            type="SPECTACLE",
            description="test",  # TODO: Récupérer l'info
            adresse=f"{salle.nom}: {salle.adresse1} {salle.code_postal} {salle.ville}",
            longitude=1.0,  # TODO: Récupérer l'info
            latitude=1.0,  # TODO: Récupérer l'info
            image="tmp_image"
        )

    def to_dict(self):
        return {
            "date": self.date,
            "heure": self.heure,
            "duree": self.duree,
            "nom": self.nom,
            "type": self.type,
            "description": self.description,
            "adresse": self.adresse,
            "longitude": self.longitude,
            "latitude": self.latitude,
            "image": self.image
        }
