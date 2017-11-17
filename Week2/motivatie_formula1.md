# Uitwerking opdracht
**Opdracht** Formule 1

**Weeknummer** 1

**Studentnummer** S1096607

**Naam student** Mies van der Lippe

**Specialisatie** FICT

**Pogingnummer**1

## Vraagstelling
Zie : << URL >>

## Invoer
De tijdsduur en de lengte van een raceronde. De duur is in minuten en mag 
fracties bevatten. De afstand is in kilometers en daarvoor geldt hetzelfde.  

## Uitvoer
In hoeveel racerondes en in wat voor afstand de race zal worden afgelegd. 

## Verbanden in en uitvoer
Aan de hand van de invoer wordt een heel simplistische simulatie van de race 
uitgevoerd en wordt gekeken welke limiet als eerste bereikt wordt. 

## Beperkingen
De simulatie is heel veel simplistischer dan degene die voor echte races gedaan
wordt. 

De invoer is wat omslachtig. Meestal voert men tijd aan de hand van minuten:
seconde ingevoerd. 

## Voorbeelden
Verwachte invoer: 
```
Naam circuit
5.031 (Afstand in km )
1.54178 (Tijd in minuten) 
```
Verwachte uitvoer:
```
De grote prijs van België wordt verreden over 42 ronden (294.168 km).
```
Voorbeelden van ongeldige invoer
```
[Geen naam]
4,83km (letters, comma in plaats van punt)
1:40m (dubbele punt in plaats van commagetal, letter)
```
## Ontwerp
Ik vraag de gebruiker om de invoer. Daarna simuleer ik de race door rondes te 
simuleren en de tijd en afstand bij te houden tot een van de twee maximalen 
overschreven wordt. 

## Pseudocode
zolang de afstand en tijd niet overschreden zijn 
    verreden_aftand += rondeafstand
    verreden_tijd += rondetijd
weergeven_uitvoer()
## Test
```
Monaco
3.340
1.13895
```
```
De grote prijs van Monaco wordt verreden over 78 ronden (260.52 km).
```