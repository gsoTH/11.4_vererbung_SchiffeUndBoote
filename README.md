# 11.4_vererbung_SchiffeUndBoote
Die Struktur der Klassen[^1] ist im nachfolgenden UML-Klassendiagramm zusammengefasst[^2]: 
[![](https://mermaid.ink/img/pako:eNrdVcGO2jAQ_RXLp1YFxCYhQA6V2u6xe6KnVSRkkkli4djUmSy7Qfx7J4FAlrCstKe2OZl5b55nHrZnxyMTAw94qCMliuJeitSKPNTaILCQP5ZMKAWafUO0clUiLeFZFijB0jIFHD4AZqShR2GoF4AIlq1NnhOqS8sKUHXOk7E1zu6h2ELaiGyUrCSSfEGkswyLhU2hQFAKRyHVxehramM_hY53h0D9DZkWOQSsQNsNrkuwFahOfB_qw-I7FBIrKnA4_NqoddVb8NUOVPfVTbSIsqsA_SSxfjwTZaFLssX2oI2qejFjsRdTVHDQKfvU1g-jUUgNtogymSRXu7vgvG_j5W5tFHQKS6mXOdA_rQMmNXYJKwsSbxEyA9ktnE5Wkgqd3qAIXYlMLaO2pR5BAZ3Q8qCx3nbgk2W_hF7fcOsM_9NGKRHTZdvKKMOahR8wakECamUMNj61d6Tr1YnxvlWrY3pwIfQXWVbU3SRUSnRQ-p07Z_hL_VIt2y4-aaCnZtlv6vOTkTG7NHJDd_q2kS3jvzDyzaP1QSPPaa-Vm-RTrNmnSTvazwec3txcyJiGXGNsyDGDHEIe0DKGRJQK6zlTU0WJZvGiIx6gLWHAy00sEI5DkQcJDSuKQizR2IfD4Gzm54BvhObBjj_z4M71RpOp581dbzxzxu6dM-AvPJj5o_ncmU9d15n6rj919gNeGUOq45HvzfypP3HGnuuOndmkkXtswLqO_R-UjmMU?type=png)](https://mermaid.live/edit#pako:eNrdVcGO2jAQ_RXLp1YFxCYhQA6V2u6xe6KnVSRkkkli4djUmSy7Qfx7J4FAlrCstKe2OZl5b55nHrZnxyMTAw94qCMliuJeitSKPNTaILCQP5ZMKAWafUO0clUiLeFZFijB0jIFHD4AZqShR2GoF4AIlq1NnhOqS8sKUHXOk7E1zu6h2ELaiGyUrCSSfEGkswyLhU2hQFAKRyHVxehramM_hY53h0D9DZkWOQSsQNsNrkuwFahOfB_qw-I7FBIrKnA4_NqoddVb8NUOVPfVTbSIsqsA_SSxfjwTZaFLssX2oI2qejFjsRdTVHDQKfvU1g-jUUgNtogymSRXu7vgvG_j5W5tFHQKS6mXOdA_rQMmNXYJKwsSbxEyA9ktnE5Wkgqd3qAIXYlMLaO2pR5BAZ3Q8qCx3nbgk2W_hF7fcOsM_9NGKRHTZdvKKMOahR8wakECamUMNj61d6Tr1YnxvlWrY3pwIfQXWVbU3SRUSnRQ-p07Z_hL_VIt2y4-aaCnZtlv6vOTkTG7NHJDd_q2kS3jvzDyzaP1QSPPaa-Vm-RTrNmnSTvazwec3txcyJiGXGNsyDGDHEIe0DKGRJQK6zlTU0WJZvGiIx6gLWHAy00sEI5DkQcJDSuKQizR2IfD4Gzm54BvhObBjj_z4M71RpOp581dbzxzxu6dM-AvPJj5o_ncmU9d15n6rj919gNeGUOq45HvzfypP3HGnuuOndmkkXtswLqO_R-UjmMU)

## Hinweise zum Code
- Das vorliegende Projekt enthält einige Python-Klassen, die `@properties` statt `get_`-Methoden einsetzen. Dadurch ist ein Zugriff z.B. durch `land.name`statt `land.get_name` möglich. Damit das geht, werden die Attribute mit einem Unterstrich gekennzeichnet[^3]. Mehr zum `@property`-Dekorator finden Sie [hier](https://realpython.com/python-property/#using-property-as-a-decorator).

- Im Ordner `tests/` sind Testfälle für jede Klasse (Testabdeckung 100%). Informationen zur Testdurchführung mit `pytest` und Abdeckungsanalyse mit `coverage` finden Sie [hier](https://gso-schule-koeln.gitbook.io/fu1).

## Arbeitsauftrag
1)  Refactoring: Wenden Sie das [DRY-Prinzip](https://www.generic.de/blog/dry-vs-kiss-clean-code-prinzipien) an, indem Sie Vererbung einsetzen um Wiederholungen zu minimieren!

    - Suchen Sie nach gemeinsamen Attributen in den Klassen um daraus geeignete Eltern-Klassen abzuleiten!

    - Ihr Refactoring ist erfolgreich, wenn alle Testfälle weiterhin erfolgreich sind.

2)  Erweitern Sie den Code, damit die folgenden Anforderungen erfüllt werden:

    a)  Über `ist_panamax` soll abgefragt werden können, ob man mit diesem Wasserfahrzeug durch den Panamakanal (alte Schleusen) passt.

    b)  `ist_scheinfrei`: Gibt Auskunft darüber, ob man einen Sportbootführerschein Binnen benötigt, um hiermit zu fahren. Allgemein gilt: Länge bis 15m, Segelfläche nicht größer als 6m², LeistungInKw nicht höher als 11.

    c)  `lloyd_registrierung`: Setzt sich bei allen Wasserfahrzeugen aus dem Namen in UpperCase zusammen. Sofern vorhanden soll der Nachname und Wohnort des Besitzers ebenfalls ausgegeben werden. Beispiele (bezogen auf die obigen Objekte):

        - "EVERGIVEN"

        - "UNSINKBARII--Holmes--London"

    d)  Der Name eines Bootes kann nur geändert werden, wenn **gleichzeitig** der Besitzer wechselt.

    e)  Es soll nicht mehr nur von einem Boot zu seinem Besitzer navigiert werden können, sondern auch umgekehrt.

    Ist:
    [![](https://mermaid.ink/img/pako:eNotjb0OwjAQg18lurl9gQwMiJGJrrcciVsi5QcllwGqvjtB4MmyLX87ueJBlji7KK1dgmxVEmcfKpyGks31xtkMLdgQ76WomeeTOaMFfaP-OpoooSYJflzt34xJH0hgssN6rNKj8qAcYypdy_LKjqzWjon604vijya7Smw4PqqANBw?type=png)](https://mermaid.live/edit#pako:eNotjb0OwjAQg18lurl9gQwMiJGJrrcciVsi5QcllwGqvjtB4MmyLX87ueJBlji7KK1dgmxVEmcfKpyGks31xtkMLdgQ76WomeeTOaMFfaP-OpoooSYJflzt34xJH0hgssN6rNKj8qAcYypdy_LKjqzWjon604vijya7Smw4PqqANBw)

    Soll:
    [![](https://mermaid.ink/img/pako:eNotjb0OwjAQg18lurl9gYyIkYmutxyJWyLlByWXAaq-e4PAk2Vb_nZyxYMscXZRWrsG2aokzj5UOA0lm9udsxlasCE-SlEzz-aCFvSD-qtoooSaJPjxtH8zJn0igckO67FKj8oDcoypdC3LOzuyWjsm6i8vij-Z7Cqx4TgBf4kz3g?type=png)](https://mermaid.live/edit#pako:eNotjb0OwjAQg18lurl9gYyIkYmutxyJWyLlByWXAaq-e4PAk2Vb_nZyxYMscXZRWrsG2aokzj5UOA0lm9udsxlasCE-SlEzz-aCFvSD-qtoooSaJPjxtH8zJn0igckO67FKj8oDcoypdC3LOzuyWjsm6i8vij-Z7Cqx4TgBf4kz3g)

[^1]: Der Code wurde ursprünglich in C# verfasst und mit Hilfe von ChatGPT in Python übersetzt. Also halten Sie Ausschau nach Fehlern oder Unstimmigkeiten!

[^2]: Jedes UML-Diagramm dient in erster Linie der Kommunikation. Ich möchte hier nicht auf jedes Detail (Konstruktoren, get-Methoden) eingehen. Daher habe ich nur einen Teil dargestellt. Auf Abweichungen zwischen UML und tatsächlicher Syntax wird u.a. in [dieser Diskussion](https://stackoverflow.com/questions/470097/how-to-represent-a-c-sharp-property-in-uml) eingegangen.

[^3]: Ohne den Unterstrich hieße das Attribut exakt wie die Eigenschaft und der Interpreter wüsste nicht, worauf zugegriffen wird. Der Unterstrich ist eine Möglichkeit der Unterscheidung zwischen Attribut und Eigenschaft . In C# gib es ein ähnliches Vorgehen, bei dem Attribute immer LowerCase sind (z.B. `istEchtSo`), während die zugehörigen Eigenschaften exakt wie das Attribut heißen, aber UpperCase sind (z.B. `IstEchtSo`).
