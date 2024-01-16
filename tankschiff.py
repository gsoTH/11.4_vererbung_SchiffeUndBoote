from land import Land

class Tankschiff:
    def __init__(self, name, land, laenge_in_metern, breite_in_metern, hoehe_in_metern, tiefgang_in_metern, ladegewicht_in_t, leistung_in_kw):
        self.name = name
        self.land = land
        self.laenge_in_metern = laenge_in_metern
        self.breite_in_metern = breite_in_metern
        self.hoehe_in_metern = hoehe_in_metern
        self.tiefgang_in_metern = tiefgang_in_metern
        self.ladegewicht_in_t = ladegewicht_in_t
        self.leistung_in_kw = leistung_in_kw

    def get_name(self):
        return self.name

    def get_land(self):
        return self.land

    def get_laenge_in_metern(self):
        return self.laenge_in_metern

    def get_breite_in_metern(self):
        return self.breite_in_metern

    def get_hoehe_in_metern(self):
        return self.hoehe_in_metern

    def get_tiefgang_in_metern(self):
        return self.tiefgang_in_metern

    def get_ladegewicht_in_t(self):
        return self.ladegewicht_in_t

    def get_leistung_in_kw(self):
        return self.leistung_in_kw