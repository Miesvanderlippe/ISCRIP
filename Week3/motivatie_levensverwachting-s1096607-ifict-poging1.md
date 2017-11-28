# Uitwerking opdracht
**Opdracht** Levensverwachting

**Weeknummer** 3

**Studentnummer** S1096607

**Naam student** Mies van der Lippe

**Specialisatie** FICT

**Pogingnummer**1

## Vraagstelling
Zie : https://dodona.ugent.be/nl/exercises/849566952/

## Invoer
Geen gebruikers-invoer mogelijk. Alleen programatische invoer wordt 
geaccepteerd. 
```
levensverwachting(geslacht: str, roker: bool, sport: int,
                      alcohol: int, fastfood: bool)->float:
``` 

## Uitvoer
De levensverwachting.

## Verbanden in en uitvoer
Met de inputs worden jaren toegevoegd of afgetrokken van een basisverwachting. 
Dit resulteert uiteindelijk in een verwachting. 

## Beperkingen
De berekening is simplistisch en de input is hoofdletter- en spelfout gevoelig. 

## Voorbeelden
Verwachte invoer:
```
levensverwachting(geslacht='man', roker=True, sport=2, alcohol=10,
                            fastfood=True)
```
Verwachte uitvoer:
```
65.5
```
Voorbeelden van ongeldige invoer
```
levensverwachting(geslacht='mAn', roker=True, sport=2, alcohol=10,
                            fastfood=True)
```
## Ontwerp
De invoer word stuk voor stuk aan de tand gevoeld en als er aan bepaalde 
voorwaarden voldaan is word de verwachte levensduur aangepast. 

## Pseudocode
```
basis_verwachting = 70
# dit voor veel voorwaardes
if voorwaarde N: 
    basis_verwachting += 5
```

## Test
```
print(levensverwachting(geslacht='man', roker=True, sport=2, alcohol=10,
                            fastfood=True))

print(levensverwachting(geslacht='man', roker=True, sport=5, alcohol=5,
                        fastfood=True))

print(levensverwachting(geslacht='vrouw', roker=False, sport=5, alcohol=0,
                        fastfood=False))

print(levensverwachting(geslacht='vrouw', roker=False, sport=3, alcohol=14,
                        fastfood=True))

print(levensverwachting(geslacht='man', roker=False, sport=4, alcohol=4,
                        fastfood=False))
```
```
65.5
70
87
78.5
82
```