from land import Land

def test_Land__kann_erstellt_werden():
    # Arrange
    name = "Deutschland"
    kuerzel = "DE"

    # Act
    land = Land(name, kuerzel)

    # Assert
    assert land.name == name
    assert land.kuerzel == kuerzel