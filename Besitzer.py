import Land

class Besitzer:
    def __init__(self, vorname, nachname, strasse, hausnummer, plz, ort, land):
        self._vorname = vorname
        self._nachname = nachname
        self._strasse = strasse
        self._hausnummer = hausnummer
        self._plz = plz
        self._ort = ort
        self._land = land

    @property
    def vorname(self):
        return self._vorname

    @property
    def nachname(self):
        return self._nachname

    @property
    def strasse(self):
        return self._strasse

    @property
    def hausnummer(self):
        return self._hausnummer

    @property
    def plz(self):
        return self._plz

    @property
    def ort(self):
        return self._ort

    @property
    def land(self):
        return self._land

# Beispiel-Nutzung:
# land_objekt = Land("Deutschland", "DE")
# besitzer = Besitzer("Max", "Mustermann", "Musterstraße", "123", "12345", "Musterstadt", land_objekt)

# Zugriff auf Properties:
# print(besitzer.vorname)
# print(besitzer.nachname)
# print(besitzer.strasse)
