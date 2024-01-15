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
    assert besitzer.vorname == vorname
    assert besitzer.nachname == nachname
    assert besitzer.strasse == strasse
    assert besitzer.hausnummer == hausnummer
    assert besitzer.plz == plz
    assert besitzer.ort == ort
    assert besitzer.land == land