# 11.4_vererbung_SchiffeUndBoote
Die Struktur der Klassen[^1] ist im nachfolgenden UML-Klassendiagramm zusammengefasst[^2]: 
[![](https://mermaid.ink/img/pako:eNrdVU1v2zAM_SuCThuWBKnt5sOHAet6XE_pqTAQKDZtC5GpTKabNkH--2jny03SFOhpm08K3-MT-SKJaxnbBGQoI4yNKst7rTKniggT7SAmbVHcPUaIlkBE8qkSyhhA8YPI6VlFvIQXXZIGx8sMqPsAlLMi9qIIJ0AETsxtUTCKlRMlmDrn2boaF_dQLiFrRBZGrzSxfMmko4xIlMugJDCGehFXKfhrKhW_FCbrbaD-ugJVAaEoybWD8wrcCkwrvolwu7iDUtOKC-x2vzdqbfU9-GYHrvviJqji_CLAP1nsPJ6rqsSKbXFn0MKszmLW0VnMcMFhq-xDWz8tktIIroxznaYXuzvhfGzj6W77KGAGU43TAvifxlBopDZh5kDTNUJuIb-G88lKM4XZFYrClcrNNN63dEYwwCe02mrMly34YNmjwvkVt47wP22UUQlftqWOc6pZ9AmjJixgZtZS49P-jrS9OjA-tmq2Sw9PhP4iy8q6m5RLibdKvwvvCH-rX6rpvosvCPzUTM-b-vpsdSJOjVzwnb5u5J7xXxj57tH6pJHHtLfKTfIh1uzTpO3slx3Jb26hdMIjrzE2kpRDAZEMeZlAqipD9ZypqaoiO3nFWIbkKujIapEogt2IlGHKw4qjkGiy7mE7Rptp2pELhTJcyxcZ3vhB73YYBGM_6I-8vn_jdeSrDEeD3njsjYe-7w0H_mDobTpyZS2r9nuDYDQYDm69fuD7fW9028g9NWBdx-YP6wRoVQ?type=png)](https://mermaid.live/edit#pako:eNrdVU1v2zAM_SuCThuWBKnt5sOHAet6XE_pqTAQKDZtC5GpTKabNkH--2jny03SFOhpm08K3-MT-SKJaxnbBGQoI4yNKst7rTKniggT7SAmbVHcPUaIlkBE8qkSyhhA8YPI6VlFvIQXXZIGx8sMqPsAlLMi9qIIJ0AETsxtUTCKlRMlmDrn2boaF_dQLiFrRBZGrzSxfMmko4xIlMugJDCGehFXKfhrKhW_FCbrbaD-ugJVAaEoybWD8wrcCkwrvolwu7iDUtOKC-x2vzdqbfU9-GYHrvviJqji_CLAP1nsPJ6rqsSKbXFn0MKszmLW0VnMcMFhq-xDWz8tktIIroxznaYXuzvhfGzj6W77KGAGU43TAvifxlBopDZh5kDTNUJuIb-G88lKM4XZFYrClcrNNN63dEYwwCe02mrMly34YNmjwvkVt47wP22UUQlftqWOc6pZ9AmjJixgZtZS49P-jrS9OjA-tmq2Sw9PhP4iy8q6m5RLibdKvwvvCH-rX6rpvosvCPzUTM-b-vpsdSJOjVzwnb5u5J7xXxj57tH6pJHHtLfKTfIh1uzTpO3slx3Jb26hdMIjrzE2kpRDAZEMeZlAqipD9ZypqaoiO3nFWIbkKujIapEogt2IlGHKw4qjkGiy7mE7Rptp2pELhTJcyxcZ3vhB73YYBGM_6I-8vn_jdeSrDEeD3njsjYe-7w0H_mDobTpyZS2r9nuDYDQYDm69fuD7fW9028g9NWBdx-YP6wRoVQ)

## Hinweise zum Code
- Im Ordner `tests/` sind Testfälle für jede Klasse (Testabdeckung 100%). Informationen zur Testdurchführung mit `pytest` und Abdeckungsanalyse mit `coverage` finden Sie [hier](https://gso-schule-koeln.gitbook.io/fu1).

- Dieses Repository arbeitet mit get_*() und set_*() Methoden. Für Lehrzwecke wird somit deutlich, dass man den Zugriff auf die "privaten" Attribute einer Klasse steuert. Das ist allerdings nicht sehr pythonic<sup>TM</sup>, denn es gibt [keine echte Möglichkeit, den Zugriff auf Attribute zu verhindern](https://docs.python.org/3/tutorial/classes.html#private-variables). Eine Variante mit `_`-Präfix und `@Properties` finden Sie in einer [alten Version dieses Repos](https://github.com/gsoTH/11.4_vererbung_SchiffeUndBoote/tree/f77c4745bf010f2622e53c6af7c0e43dfcbe00a3).

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

