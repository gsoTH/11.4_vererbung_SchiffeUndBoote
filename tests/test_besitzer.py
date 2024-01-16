from besitzer import Besitzer
from land import Land

def test_Besitzer__kann_erstellt_werden():
    # Arrange
    vorname = "Max"
    nachname = "Mustermann"
    strasse = "Musterstraße"
    hausnummer = "123"
    plz = "12345"
    ort = "Musterstadt"
    land = Land("Deutschland", "DE")

    # Act
    besitzer = Besitzer(vorname, nachname, strasse, hausnummer, plz, ort, land)

    # Assert
    assert besitzer.get_vorname() == vorname
    assert besitzer.get_nachname() == nachname
    assert besitzer.get_strasse() == strasse
    assert besitzer.get_hausnummer() == hausnummer
    assert besitzer.get_plz() == plz
    assert besitzer.get_ort() == ort
    assert besitzer.get_land() == land