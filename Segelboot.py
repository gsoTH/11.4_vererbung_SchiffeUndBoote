import Land
import Besitzer

class Segelboot:
    def __init__(self, name, laenge_in_metern, breite_in_metern, hohe_in_metern, tiefgang_in_metern, segelflaeche_in_qm2, besitzer):
        self._name = name
        self._laenge_in_metern = laenge_in_metern
        self._breite_in_metern = breite_in_metern
        self._hohe_in_metern = hohe_in_metern
        self._tiefgang_in_metern = tiefgang_in_metern
        self._segelflaeche_in_qm2 = segelflaeche_in_qm2
        self._besitzer = besitzer

    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, value):
        self._name = value

    @property
    def besitzer(self):
        return self._besitzer

    @besitzer.setter
    def besitzer(self, value):
        self._besitzer = value

    @property
    def laenge_in_metern(self):
        return self._laenge_in_metern

    @laenge_in_metern.setter
    def laenge_in_metern(self, value):
        self._laenge_in_metern = value

    @property
    def breite_in_metern(self):
        return self._breite_in_metern

    @breite_in_metern.setter
    def breite_in_metern(self, value):
        self._breite_in_metern = value

    @property
    def hohe_in_metern(self):
        return self._hohe_in_metern

    @hohe_in_metern.setter
    def hohe_in_metern(self, value):
        self._hohe_in_metern = value

    @property
    def tiefgang_in_metern(self):
        return self._tiefgang_in_metern

    @tiefgang_in_metern.setter
    def tiefgang_in_metern(self, value):
        self._tiefgang_in_metern = value

    @property
    def segelflaeche_in_qm2(self):
        return self._segelflaeche_in_qm2

    @segelflaeche_in_qm2.setter
    def segelflaeche_in_qm2(self, value):
        self._segelflaeche_in_qm2 = value

# Beispiel-Nutzung:
# land_objekt = land_objekt = Land("Deutschland", "DE")
# besitzer = Besitzer("Max", "Mustermann", "Musterstraße", "123", "12345", "Musterstadt", land_objekt)
# segelboot = Segelboot("Boot2", 12, 6, 3, 1.5, 80, besitzer)

# Zugriff auf Properties:
# print(segelboot.name)
# print(segelboot.besitzer.vorname)
# print(segelboot.laenge_in_metern)
