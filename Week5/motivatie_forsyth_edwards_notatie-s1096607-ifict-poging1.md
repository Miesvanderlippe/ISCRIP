# Uitwerking opdracht
**Opdracht** Forsyth notatie

**Weeknummer** 5

**Studentnummer** S1096607

**Naam student** Mies van der Lippe

**Specialisatie** FICT

**Pogingnummer**1

## Vraagstelling
Zie : https://dodona.ugent.be/nl/exercises/867899652/

## Invoer
Er wordt gekozen of er encodering of decodering gedaan wordt met een cijfer. 
Daarna vult de gebruiker de sequentie in gevolgd door de seperator. Deze is 
optioneel.  

## Uitvoer
De gecodeerde of gedecodeerde sequentie.  

## Verbanden in en uitvoer
Allereerst bepaalt de gebruiker welke functie gebruikt zal worden. Dan wordt 
deze dus door een van de twee functies omgezet. Hierbij worden of cijfers 
vervangen met N seperatoren, of seperatoren vervangen met N. Dit wordt op 
twee verschillende manieren terug gecommuniceerd naar de gebruiker. Danwel als 
grid danwel als string.    

## Beperkingen
Er wordt geen donder gecontrolleerd. Ongeldige borden, seperators en dergelijke 
kunnen voor problemen zorgen.   

## Voorbeelden
Verwachte invoer:
```
Kies een van de opties:
1) Fen omzetten naar grid
2) Grid omzetten naar Fen notatie
2
Geef uw Grid (zonder enters)
rnbqkbnrpppppppp<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<PPPPPPPPRNBQKBNR
Geef uw seperator
<
```
Verwachte uitvoer:
```
rnbqkbnr/pppppppp/8/8/8/8/PPPPPPPP/RNBQKBNR
```
Voorbeelden van ongeldige invoer
```
Voer uw tekst in:
DingenDieGeenMeervoudVanAchtZijn
```

## Ontwerp
Ik zal een functie maken om het omzetten van cijfers naar N seperatoren te 
faciliteren. Dan is het decoderen van een Fosyth notatie een eitje. Het 
encoderen zal ik gewoon doen met een reeks string replacements. 

## Pseudocode
```
functie decodeer: 
    vervang getallen met n seperatoren
    vervang / met nieuwe regels

functie encodeer: 
    vervang n*de seperator met n
    voeg na elk achtste letter een / toe

vraag de gebruiker wat hij wil doen 
voer dit uit
```

## Test
```

Kies een van de opties:
1) Fen omzetten naar grid
2) Grid omzetten naar Fen notatie
2
Geef uw Grid (zonder enters)
rnbqkbnrpppppppp<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<PPPPPPPPRNBQKBNR
Geef uw seperator
<
rnbqkbnr/pppppppp/8/8/8/8/PPPPPPPP/RNBQKBNR
```