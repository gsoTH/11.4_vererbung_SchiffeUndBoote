from tankschiff import Tankschiff
from land import Land

def test_Tankschiff__kann_erstellt_werden():
    # Arrange
    name = "Bitte nicht auslaufen"
    land = Land("China", "CH")
    laenge_in_metern = 400
    breite_in_metern = 59
    hoehe_in_metern = 33
    tiefgang_in_metern = 16
    ladegewicht_in_t = 200000
    leistung_in_kw = 59300

    # Act
    tankschiff = Tankschiff(name, land, laenge_in_metern, breite_in_metern, hoehe_in_metern, tiefgang_in_metern, ladegewicht_in_t, leistung_in_kw)

    # Assert
    assert tankschiff.name == name
    assert tankschiff.land == land
    assert tankschiff.laenge_in_metern == laenge_in_metern
    assert tankschiff.breite_in_metern == breite_in_metern
    assert tankschiff.hoehe_in_metern == hoehe_in_metern
    assert tankschiff.tiefgang_in_metern == tiefgang_in_metern
    assert tankschiff.ladegewicht_in_t == ladegewicht_in_t
    assert tankschiff.leistung_in_kw == leistung_in_kw

