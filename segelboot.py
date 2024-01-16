from land import Land
from besitzer import Besitzer

class Segelboot:
    def __init__(self, name, laenge_in_metern, breite_in_metern, hoehe_in_metern, tiefgang_in_metern, segelflaeche_in_qm2, besitzer):
        self.name = name
        self.laenge_in_metern = laenge_in_metern
        self.breite_in_metern = breite_in_metern
        self.hoehe_in_metern = hoehe_in_metern
        self.tiefgang_in_metern = tiefgang_in_metern
        self.segelflaeche_in_qm2 = segelflaeche_in_qm2
        self.besitzer = besitzer

    def get_name(self):
        return self.name

    def get_besitzer(self):
        return self.besitzer

    def set_besitzer(self, value):
        self.besitzer = value

    def get_laenge_in_metern(self):
        return self.laenge_in_metern

    def get_breite_in_metern(self):
        return self.breite_in_metern

    def get_hoehe_in_metern(self):
        return self.hoehe_in_metern

    def get_tiefgang_in_metern(self):
        return self.tiefgang_in_metern

    def get_segelflaeche_in_qm2(self):
        return self.segelflaeche_in_qm2
