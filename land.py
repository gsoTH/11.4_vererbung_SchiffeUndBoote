class Land:
    def __init__(self, name, kuerzel):
        self._name = name
        self._kuerzel = kuerzel

    @property
    def name(self):
        return self._name

    @property
    def kuerzel(self):
        return self._kuerzel

# Beispiel-Nutzung:
# land = Land("Deutschland", "DE")

# Zugriff auf Properties:
# print(land.name)
# print(land.kuerzel)
