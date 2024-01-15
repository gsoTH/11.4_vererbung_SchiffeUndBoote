from land import Land

class Containerschiff:
    def __init__(self, name, land, laenge_in_metern, breite_in_metern, hoehe_in_metern, tiefgang_in_metern, anzahl_container, leistung_in_kw):
        self._name = name
        self._land = land
        self._laenge_in_metern = laenge_in_metern
        self._breite_in_metern = breite_in_metern
        self._hoehe_in_metern = hoehe_in_metern
        self._tiefgang_in_metern = tiefgang_in_metern
        self._anzahl_container = anzahl_container
        self._leistung_in_kw = leistung_in_kw

    @property
    def name(self):
        return self._name

    @property
    def land(self):
        return self._land

    @property
    def laenge_in_metern(self):
        return self._laenge_in_metern

    @property
    def breite_in_metern(self):
        return self._breite_in_metern

    @property
    def hoehe_in_metern(self):
        return self._hoehe_in_metern

    @property
    def tiefgang_in_metern(self):
        return self._tiefgang_in_metern

    @property
    def anzahl_container(self):
        return self._anzahl_container

    @property
    def leistung_in_kw(self):
        return self._leistung_in_kw


# Zugriff auf Properties:
# print(containerschiff.name)
# print(containerschiff.land)
# print(containerschiff.laenge_in_metern)
