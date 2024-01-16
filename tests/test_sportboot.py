from sportboot import Sportboot
from besitzer import Besitzer
from land import Land

def test_Sportboot__kann_erstellt_werden():
    # Arrange
    name = "Unsink-Bar"
    laenge_in_metern = 16
    breite_in_metern = 5
    hoehe_in_metern = 5
    tiefgang_in_metern = 3
    leistung_in_kw = 5
    besitzer = Besitzer("Sherlock", 
                        "Holmes", 
                        "Baker Street", 
                        "221B", 
                        "NW1", 
                        "London", 
                        Land(   "United Kingdom", 
                                "UK"))

    # Act
    sportboot = Sportboot(name, laenge_in_metern, breite_in_metern, hoehe_in_metern, tiefgang_in_metern, leistung_in_kw, besitzer)

    # Assert
    assert sportboot.get_name() == name
    assert sportboot.get_laenge_in_metern() == laenge_in_metern
    assert sportboot.get_breite_in_metern() == breite_in_metern
    assert sportboot.get_hoehe_in_metern() == hoehe_in_metern
    assert sportboot.get_tiefgang_in_metern() == tiefgang_in_metern
    assert sportboot.get_leistung_in_kw() == leistung_in_kw
    assert sportboot.get_besitzer() == besitzer


def test_besitzer__veraenderbar():
    # Arrange
    besitzer_alt = besitzer = Besitzer("Sherlock", 
                        "Holmes", 
                        "Baker Street", 
                        "221B", 
                        "NW1", 
                        "London", 
                        Land(   "United Kingdom", 
                                "UK"))
    sportboot = Sportboot("Unsink-Bar", 16, 5, 5, 3, 5, besitzer_alt)
    
    besitzer_neu = Besitzer("Jean-Luc", 
                        "Picard", 
                        "Rue de Marronniers", 
                        "1", 
                        "39700", 
                        "La Barre", 
                        Land(   "Frankreich", 
                                "FR"))

    # Act 
    sportboot.set_besitzer(besitzer_neu)
    
    # Assert
    assert sportboot.get_besitzer() == besitzer_neu

def test_leistung_in_kw__veraenderbar():
    # Arrange
    leistung_in_kw_alt = 5
    sportboot = Sportboot("Unsink-Bar", 16, 5, 5, 3, leistung_in_kw_alt, Besitzer("Sherlock", "Holmes", "Baker Street", "221B", "NW1", "London", Land("United Kingdom", "UK")))
    leistung_in_kw_neu = 25

    # Act 
    sportboot.set_leistung_in_kw(leistung_in_kw_neu)

    # Assert
    assert sportboot.get_leistung_in_kw() == leistung_in_kw_neu

    