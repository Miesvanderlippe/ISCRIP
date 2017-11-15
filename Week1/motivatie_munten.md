#Uitwerking opdracht
**Opdracht** Munten

**Weeknummer** 1

**Studentnummer** S1096607

**Naam student** Mies van der Lippe

**Specialisatie** FICT

**Pogingnummer**1

##Vraagstelling
Zie : https://dodona.ugent.be/nl/exercises/1576457755/

##Invoer
De waardes van de verschillende munten

##Uitvoer
De totale waarde van de munten, het totaal aantal munten

##Verbanden in en uitvoer
De gebruiker voert de waardes van de verschillende munten in. Daarvan houd
ik de totale waarde en het totale aantal bij. 

##Beperkingen
Vraagt altijd om alle munten

Controlleerd niet op foutsituaties

Accepteerd negatieve getallen

##Voorbeelden
Verwachte invoer: 
```
5
4
3
2
1
0
40
11
```
Verwachte uitvoer:
```
Aantal munten: 66
Totale waarde: 62.68
```
Voorbeelden van ongeldige invoer
```
120 euro (bevat letters)
-299 (negatief getal)
```
##Ontwerp
Ik maak een lijstje van alle verwachte muntstukken. Dat ga ik af en vraag de 
gebruiker om hoeveel zij van dit muntstuk hebben. Na elke vraag update ik de 
totalen. 

##Pseudocode
```
for waarde in munten

    aantal = input()
    totaal += aantal
    totale_waarde += aantal * waarde
```

##Test
```
Aantal munten met waarde 1ct
5
Aantal munten met waarde 2ct
4
Aantal munten met waarde 5ct
3
Aantal munten met waarde 10ct
2
Aantal munten met waarde 20ct
1
Aantal munten met waarde 50ct
0
Aantal munten met waarde 100ct
40
Aantal munten met waarde 200ct
11
```
```
Aantal munten: 66
Totale waarde: 62.68
```