from containerschiff import Containerschiff
from land import Land

def test_Containerschiff__kann_erstellt_werden():
    # Arrange
    name = "Ever Given"
    land = Land("China", "CH")
    laenge_in_metern = 400
    breite_in_metern = 59
    hoehe_in_metern = 33
    tiefgang_in_metern = 16
    anzahl_container = 20124
    leistung_in_kw = 59300

    # Act
    containerschiff = Containerschiff(name, land, laenge_in_metern, breite_in_metern, hoehe_in_metern, tiefgang_in_metern, anzahl_container, leistung_in_kw)

    # Assert
    assert containerschiff.get_name() == name
    assert containerschiff.get_land() == land
    assert containerschiff.get_laenge_in_metern() == laenge_in_metern
    assert containerschiff.get_breite_in_metern() == breite_in_metern
    assert containerschiff.get_hoehe_in_metern() == hoehe_in_metern
    assert containerschiff.get_tiefgang_in_metern() == tiefgang_in_metern
    assert containerschiff.get_anzahl_container() == anzahl_container
    assert containerschiff.get_leistung_in_kw() == leistung_in_kw

