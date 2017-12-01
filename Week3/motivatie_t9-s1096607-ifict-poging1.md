# Uitwerking opdracht
**Opdracht** GSMOniemen

**Weeknummer** 3

**Studentnummer** S1096607

**Naam student** Mies van der Lippe

**Specialisatie** FICT

**Pogingnummer**1

## Vraagstelling
Zie : https://dodona.ugent.be/nl/exercises/1858246142/

## Invoer
Men geeft een tweetal woorden waarvan gecontroleerd word of deze met dezelfde 
toetsen op een T9 toetsenbord geschreven kunnen worden.  

## Uitvoer
Of de woorden met dezelfde toetsen geschreven worden. 

## Verbanden in en uitvoer
De twee woorden worden letter per letter omgezet naar cijfers op een T9 
toetsenbord. Deze cijferreeks word vergeleken en het resultaat word terug 
gegeven.   

## Beperkingen
Alleen letters binnen het alfabet worden geacapteerd, de rest wordt een 0. Dit
klopt in principe voor punten en spaties maar niet voor getallen.  

## Voorbeelden
Verwachte invoer:
```
Woord1: 
aanbod
Woord2:
bamboe
```
Verwachte uitvoer:
```
True
```
Voorbeelden van ongeldige invoer
```
Voer uw tekst in:
--40404040---43-934$$$%
00000000000000000000000
```

## Ontwerp
Er wordt per letter gekeken naar de positie op het toetsenbord. Dit voor allebei
de woorden. De resulterende cijferreeksen worden vergeleken.     

## Pseudocode
```
woord = input("woord")
uitvoer = ""

for letter in word: 
    uitvoer += zet_om_naar_t9(letter)
    
print(uitvoer)

```

## Test
```
Woord 1:
bamboe
Woord 2:
aanbod
True
```