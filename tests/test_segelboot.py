from segelboot import Segelboot
from besitzer import Besitzer
from land import Land

def test_Segelboot__kann_erstellt_werden():
    # Arrange
    name = "Unsink-Bar"
    laenge_in_metern = 16
    breite_in_metern = 5
    hoehe_in_metern = 5
    tiefgang_in_metern = 3
    segelflaeche_in_qm2 = 5
    besitzer = Besitzer("Sherlock", 
                        "Holmes", 
                        "Baker Street", 
                        "221B", 
                        "NW1", 
                        "London", 
                        Land(   "United Kingdom", 
                                "UK"))

    # Act
    segelboot = Segelboot(name, laenge_in_metern, breite_in_metern, hoehe_in_metern, tiefgang_in_metern, segelflaeche_in_qm2, besitzer)

    # Assert
    assert segelboot.get_name() == name
    assert segelboot.get_laenge_in_metern() == laenge_in_metern
    assert segelboot.get_breite_in_metern() == breite_in_metern
    assert segelboot.get_hoehe_in_metern() == hoehe_in_metern
    assert segelboot.get_tiefgang_in_metern() == tiefgang_in_metern
    assert segelboot.get_segelflaeche_in_qm2() == segelflaeche_in_qm2
    assert segelboot.get_besitzer() == besitzer


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
    segelboot = Segelboot("Unsink-Bar", 16, 5, 5, 3, 5, besitzer_alt)
    
    besitzer_neu = Besitzer("Jean-Luc", 
                        "Picard", 
                        "Rue de Marronniers", 
                        "1", 
                        "39700", 
                        "La Barre", 
                        Land(   "Frankreich", 
                                "FR"))

    # Act 
    segelboot.set_besitzer(besitzer_neu)
    
    # Assert
    assert segelboot.get_besitzer() == besitzer_neu