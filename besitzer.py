from land import Land

class Besitzer:
    def __init__(self, vorname, nachname, strasse, hausnummer, plz, ort, land):
        self.vorname = vorname
        self.nachname = nachname
        self.strasse = strasse
        self.hausnummer = hausnummer
        self.plz = plz
        self.ort = ort
        self.land = land

    def get_vorname(self):
        return self.vorname

    def get_nachname(self):
        return self.nachname

    def get_strasse(self):
        return self.strasse

    def get_hausnummer(self):
        return self.hausnummer

    def get_plz(self):
        return self.plz

    def get_ort(self):
        return self.ort

    def get_land(self):
        return self.land
