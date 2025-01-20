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
    