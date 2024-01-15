# 11.4_vererbung_SchiffeUndBoote
Das vorliegende Projekt enthält einige Python-Klassen[^1], deren Struktur im nachfolgenden UML-Klassendiagramm dargestellt wird.
![](UML-Klassendiagramm_SchiffeUndBoote.drawio.png)


## Arbeitsauftrag
1)  Erstellen Sie - beispielhaft - Objekte auf Basis der vorhandenen Klassen. Orientieren Sie sich dabei an diesem C#-Code:
```cs
Land china = new Land("China", "CH");
Land deutschland = new Land ("Deutschland", "D");
Land uk = new Land("United Kindgom", "UK");
Besitzer chef = new Besitzer("Sherlock", "Holmes", "Baker Street", "221B", "NW1", "London", uk);

Containerschiff c = new Containerschiff("Ever Given", china, 400,59, 33, 16, 20124, 59300);
Tankschiff t = new Tankschiff("CABO SOUNION", deutschland, 229, 32, 15, 8, 40000, 20000);
Segelboot falke = new Segelboot("Unsinkbar II", chef, 5, 3, 2, 1, 1);
Sportboot iltis = new Sportboot("Unsink-Bar", chef, 16, 5, 5, 3, 25);
```
2)  Wenden Sie das [DRY-Prinzip](https://www.generic.de/blog/dry-vs-kiss-clean-code-prinzipien) an, indem Sie Vererbung einsetzen um Wiederholungen zu minimieren!

    - Suchen Sie nach gemeinsamen Attributen in den Klassen um daraus geeignete Eltern-Klassen abzuleiten!

    - Ihr Refactoring ist erfolgreich, wenn die Objekte aus (1) immer noch erzeugt werden können, aber die Klassen frei von Wiederholungen sind.

3)  Erweitern Sie den Code, damit die folgenden Anforderungen erfüllt werden:

    a)  Über `ist_panamax` soll abgefragt werden können, ob man mit diesem Wasserfahrzeug durch den Panamakanal (alte Schleusen) passt.

    b)  'ist_scheinfrei': Gibt Auskunft darüber, ob man einen Sportbootführerschein Binnen benötigt, um hiermit zu fahren. Allgemein gilt: Länge bis 15m, Segelfläche nicht größer als 6m², LeistungInKw nicht höher als 11.

    c)  lloyd_registrierung: Setzt sich bei allen Wasserfahrzeugen aus dem Namen in UpperCase zusammen. Sofern vorhanden soll der Nachname und Wohnort des Besitzers ebenfalls ausgegeben werden. Beispiele (bezogen auf die obigen Objekte):

        - `EVERGIVEN`

        - `UNSINKBARII--Holmes--London`

4)  Ergänzen Sie das Projekt um geeignete UnitTests.

[^1]: Der Code wurde ursprünglich in C# verfasst und mit Hilfe von ChatGPT in Python übersetzt. Also halten Sie Ausschau nach Fehlern oder Unstimmigkeiten!