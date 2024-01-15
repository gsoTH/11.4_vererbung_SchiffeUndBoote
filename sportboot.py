from land import Land
from besitzer import Besitzer

class Sportboot:
    def __init__(self, name, laenge_in_metern, breite_in_metern, hoehe_in_metern, tiefgang_in_metern, leistung_in_kw, besitzer):
        self._name = name
        self._laenge_in_metern = laenge_in_metern
        self._breite_in_metern = breite_in_metern
        self._hoehe_in_metern = hoehe_in_metern
        self._tiefgang_in_metern = tiefgang_in_metern
        self._leistung_in_kw = leistung_in_kw
        self._besitzer = besitzer

    @property
    def name(self):
        return self._name

    @property
    def besitzer(self):
        return self._besitzer

    @besitzer.setter
    def besitzer(self, value):
        self._besitzer = value

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
    def leistung_in_kw(self):
        return self._leistung_in_kw

    @leistung_in_kw.setter
    def leistung_in_kw(self, value):
        self._leistung_in_kw = value

# Beispiel-Nutzung:
# land_objekt = Land("Deutschland", "DE")
# besitzer = Besitzer("Max", "Mustermann", "Musterstraße", "123", "12345", "Musterstadt", land_objekt)
# motorboot = Motorboot("Boot1", 10, 5, 2, 1, 50, besitzer)

# Zugriff auf Properties:
# print(motorboot.name)
# print(motorboot.besitzer.vorname)
# print(motorboot.laenge_in_metern)
