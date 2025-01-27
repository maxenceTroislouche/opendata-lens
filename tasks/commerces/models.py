class Commerce:
    nom: str
    description: str
    adresse: str
    mail: str
    type: str
    longitude: float
    latitude: float

    def __init__(self, nom: str, description: str, adresse: str, mail: str, type: str, longitude: float, latitude: float):
        self.nom = nom
        self.description = description
        self.adresse = adresse
        self.mail = mail
        self.type = type
        self.longitude = longitude
        self.latitude = latitude

    @staticmethod
    def build(line):
        return Commerce(
            nom=line[4],
            description="test",
            adresse="",
            mail="",
            type=line[3],
            longitude=float(line[0]),
            latitude=float(line[1])
        )

    def __str__(self):
        return f"{self.nom} - {self.description}"

    def __repr__(self):
        return self.__str__()

    def to_dict(self):
        return {
            "nom": self.nom,
            "description": self.description,
            "adresse": self.adresse,
            "mail": self.mail,
            "type": self.type,
            "longitude": self.longitude,
            "latitude": self.latitude
        }