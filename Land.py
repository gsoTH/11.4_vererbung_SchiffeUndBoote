class Land:
    def __init__(self, name, kuerzel):
        self._name = name
        self._kuerzel = kuerzel

    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, value):
        self._name = value

    @property
    def kuerzel(self):
        return self._kuerzel

    @kuerzel.setter
    def kuerzel(self, value):
        self._kuerzel = value

# Beispiel-Nutzung:
# land = Land("Deutschland", "DE")

# Zugriff auf Properties:
# print(land.name)
# print(land.kuerzel)
