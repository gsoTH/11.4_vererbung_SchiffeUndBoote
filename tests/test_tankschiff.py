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
    assert tankschiff.get_name() == name
    assert tankschiff.get_land() == land
    assert tankschiff.get_laenge_in_metern() == laenge_in_metern
    assert tankschiff.get_breite_in_metern() == breite_in_metern
    assert tankschiff.get_hoehe_in_metern() == hoehe_in_metern
    assert tankschiff.get_tiefgang_in_metern() == tiefgang_in_metern
    assert tankschiff.get_ladegewicht_in_t() == ladegewicht_in_t
    assert tankschiff.get_leistung_in_kw() == leistung_in_kw

