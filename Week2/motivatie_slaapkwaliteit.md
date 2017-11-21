# Uitwerking opdracht
**Opdracht** Paardensprong

**Weeknummer** 2

**Studentnummer** S1096607

**Naam student** Mies van der Lippe

**Specialisatie** FICT

**Pogingnummer**1

## Vraagstelling
Zie : https://dodona.ugent.be/nl/exercises/1795071955/

## Invoer
De tijd van in slaap vallen, en de minimale tijd waarop men wil ontwaken

## Uitvoer
Een wekker die niet in diepe slaap zou moeten zijn

## Verbanden in en uitvoer
Aan de begintijd wordt steeds 90 minuten toegevoegd tot de tijd over de minimale
tijd heen gaat.

## Beperkingen
De begintijd moet voor middernacht zijn, en de eindtijd erna.

## Voorbeelden
Verwachte invoer:
```
22:03 (tijd uu:mm)
06:03 (tijd uu:mm)
```
Verwachte uitvoer:
```
07:03
```
Voorbeelden van ongeldige invoer
```
00:30
00u:30m
00.30
```
## Ontwerp
Ik zet de begin- en eindtijd om in een datum voor en na middernacht en maak een
wekker aan met de begintijd. Aan de wekker voeg ik steeds 90 minuten toe tot de
minimale ontwaaktijd overschreden wordt.

## Pseudocode
begin_tijd = input("begintijd")
eind_tijd = input("eindtijd")

wekker = begintijd

zolang wekker < eind_tijd
    wekker += 90 minuten

## Test
```
Tijd van in slaap vallen (hh:mm):
22:03
Tijd om wakker worden (hh:mm):
06:03
```
```
07:03
```