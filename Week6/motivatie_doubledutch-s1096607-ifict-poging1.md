# Uitwerking opdracht
**Opdracht** Forsyth notatie

**Weeknummer** 6

**Studentnummer** S1096607

**Naam student** Mies van der Lippe

**Specialisatie** FICT

**Pogingnummer**1

## Vraagstelling
Zie : https://dodona.ugent.be/nl/exercises/1153066363/

## Invoer
Er wordt de gebruiker gevraagd een zin of woord in te voeren.   

## Uitvoer
De vertaalde zin

## Verbanden in en uitvoer
De zin word woord voor woord vertaald naar het doubledutch taaltje. Dit wordt
teruggekoppeld aan de gebruiker.     

## Beperkingen
Zover bekend zijn er geen beperkingen

## Voorbeelden
Verwachte invoer:
```
Woord of zin om te vertalen
Yesterday
```
Verwachte uitvoer:
```
yubesustuterugdudayub
```
Voorbeelden van ongeldige invoer
```
Nan
```

## Ontwerp
Ik breek de zin op in woorden. Deze vertaal ik door te kijken naar of een letter
gevolgd word door eenzelfde letter en afhankelijk daarvan vertaal ik de letter
(combinatie) 

## Pseudocode
```
functie medeklinkers
    open bestand
    lees regels
    splits op letter en vertaling
    controles
    teruggeven

functie vertaalWoord: 
    voor elke letter in het woord
        controleer of de volgende letter hetzelfde is
            vertaal samen
        anders
            veraal alleen
    geef vertaling terug 

functie vertaal zin
    voor elk woord in zin 
        vertaalWoord(woord)
    geef vertaling terug
```

## Test
```
Woord of zin om te vertalen
Yesterday
yubesustuterugdudayub
```