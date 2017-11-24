# Uitwerking opdracht
**Opdracht** Interessante getallen

**Weeknummer** 2

**Studentnummer** S1096607

**Naam student** Mies van der Lippe

**Specialisatie** FICT

**Pogingnummer**1

## Vraagstelling
Zie : https://dodona.ugent.be/nl/exercises/211647828/

## Invoer
Het aantal interssante getallen dat je wil genereren 

De apparate getallen.  

## Uitvoer
Een lijst met interessante getallen 

## Verbanden in en uitvoer
Het eerste getal bepaald hoeveel opvolgende invoer gevraagd zal worden. Voor elk
opvolgend getal zal een interessant getal gegenereerd worden. 

## Beperkingen
Er is geen controlle op invoer

Wanneer er geen interessant getal gegenereerd kan worden blijft het programma
oneindig veel pogingen doen. 

## Voorbeelden
Verwachte invoer: 
```
2
1
10 
```
Verwachte uitvoer:
```
1
190
```
Voorbeelden van ongeldige invoer
```
Getal tussen 0 en 50:
3
Getal tussen 0 en 100:
63
Getal tussen 0 en 100:
87
Getal tussen 0 en 100:
49
```
## Ontwerp
Allereerst vraag ik uiteraard om de getallen. Daarna ga ik elk ingevoerd getal
af met een functie die steeds het getal opteld en controleerd of het totaal
van de cijfers overeenkomt met het getal. 

## Pseudocode
aantal_ingvoer = input("aantal getallen")
voor elk getal in aantal_invoer: 
    invoer.append(input("Getal""))    

voor elk getal in invoer:
    bereken_getal(getal)
## Test
```

Getal tussen 0 en 50:
2
Getal tussen 0 en 100:
1
Getal tussen 0 en 100:
10
```
```
1
190
```