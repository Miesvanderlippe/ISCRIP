# Uitwerking opdracht
**Opdracht** Mars

**Weeknummer** 1

**Studentnummer** S1096607

**Naam student** Mies van der Lippe

**Specialisatie** FICT

**Pogingnummer**1

## Vraagstelling
Zie : https://dodona.ugent.be/nl/exercises/1813154454/

## Invoer
Het aantal marsdagen (heel getal)

## Uitvoer
De duur in aardse tijd

## Verbanden in en uitvoer
De invoer wordt met een formule omgezet naar de uitvoer

## Beperkingen
Kan alleen overweg met hele getallen

Controlleerd niet op foutsituaties

## Voorbeelden
Verwachte invoer: 
```
1876
```
Verwachte uitvoer:
```
1927d 13h 45m 58s
```
Voorbeelden van ongeldige invoer
```
120 dagen (bevat letters)
102.434 (te exact, we willen hele dagen)
```
## Ontwerp
Ik wil graag de tijd omzetten in een eenheid die exact genoeg is voor de 
toepassing en makkelijk om te zetten is naar een tijdsduur in aardse tijd, in 
een leesbaar format. Hiervoor gebruik ik secondes. Die zet ik vervolgens om in 
datum. 

## Pseudocode
sol_days = gebruikers_invoer

aardse_seconde = sol_days * aantal aardse seconde in sol dag

uitvoer = leesbare_datum(aardse_seconde) 

## Test
```
1876
```
```
1927d 13h 45m 58s
```