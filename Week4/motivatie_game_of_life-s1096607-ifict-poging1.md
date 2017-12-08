# Uitwerking opdracht
**Opdracht** Game of Life

**Weeknummer** 4

**Studentnummer** S1096607

**Naam student** Mies van der Lippe

**Specialisatie** FICT

**Pogingnummer**1

## Vraagstelling
Zie : https://dodona.ugent.be/nl/exercises/511272034/

## Invoer
Geen  

## Uitvoer
De velden met cellen.  

## Verbanden in en uitvoer
Daar is dus geen verband tussen, er is geen invoer.    

## Beperkingen
De velden worden niet gecontroleerd. Dit betekent dat als er een non-vierkant 
veld of een veld met andere letters dan X en O er fouten op zullen treden.   

## Voorbeelden
Verwachte invoer:
```
NaN
```
Verwachte uitvoer:
```
De velden met daarin de huidige generatie maal 4 generaties.
```
Voorbeelden van ongeldige invoer
```
NaN
```

## Ontwerp
Er wordt per letter gekeken naar de positie op het toetsenbord. Dit voor allebei
de woorden. De resulterende cijferreeksen worden vergeleken.     

## Pseudocode
```

functie buren(veld, positie)
    controleerd de posities om de cel. 

functie simuleer generatie: 
    voor elke cel:
        aantal buren(generatie, cel)
        als buren 3 is leeft de cel 
        als buren 2 of 3 is en de cel al leeft blijft deze leven 
        anders is de cel door in de volgende generatie
        
functie toongeneratie()
    plet het veld naar regels en cellen
    

```

## Test
```
X O O O O O O O
X O O O O O O O
X O O O O O O O
X O O O O O O O
X O O O O O O O
X O O O O O O O

O O O O O O O O
X X O O O O O O
X X O O O O O O
X X O O O O O O
X X O O O O O O
O O O O O O O O

O O O O O O O O
X X O O O O O O
O O X O O O O O
O O X O O O O O
X X O O O O O O
O O O O O O O O

O O O O O O O O
O X O O O O O O
O O X O O O O O
O O X O O O O O
O X O O O O O O
O O O O O O O O
```