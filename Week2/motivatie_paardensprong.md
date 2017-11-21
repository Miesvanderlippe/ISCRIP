# Uitwerking opdracht
**Opdracht** Paardensprong

**Weeknummer** 2

**Studentnummer** S1096607

**Naam student** Mies van der Lippe

**Specialisatie** FICT

**Pogingnummer**1

## Vraagstelling
Zie : https://dodona.ugent.be/nl/exercises/56374393/

## Invoer
De begin- en eindpositie van de zet die gecontrolleerd moet worden.   

## Uitvoer
Of de zet gedaan mag worden met een paard.  

## Verbanden in en uitvoer
De zet in de invoer wordt gecontrolleerd en resulteerd in de uitvoer.  

## Beperkingen
Het script kan niet overweg met hoofdletters in de positie.

Er kan buiten het bord getreden worden. 

## Voorbeelden
Verwachte invoer: 
```
a1 (Start positie)
b2 (Eind positie)
```
Verwachte uitvoer:
```
het paard kan niet springen van a1 naar b2
```
Voorbeelden van ongeldige invoer
```
ba
22
l2
mm
```
## Ontwerp
Eerst zet ik de letter om naar een positie op het bord. Daarna  vergelijk ik de
omgezette coordinaten. 

## Pseudocode
positie1 = zet_om(input("Pos1"))
positie2 = zet_om(input("Pos2"))

geldige_zet = (verschil(positie1.x, positie2.x) == 2 and 
verschil(positie1.y, positie2.y) == 1 )or (verschil(positie1.x, positie2.x) == 
1 and verschil(positie1.y, positie2.y) == 2 ) 
 
## Test
```
Pos 1
a1
Pos 2
b3
```
```
het paard kan springen van a1 naar b3
```