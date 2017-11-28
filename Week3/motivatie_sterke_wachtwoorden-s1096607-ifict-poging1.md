# Uitwerking opdracht
**Opdracht** Sterke wachtwoorden

**Weeknummer** 3

**Studentnummer** S1096607

**Naam student** Mies van der Lippe

**Specialisatie** FICT

**Pogingnummer**1

## Vraagstelling
Zie : https://dodona.ugent.be/nl/exercises/417422714/

## Invoer
Het aantal wachtwoorden dat de gebruiker wil testen, ieder wachtwoord. 

## Uitvoer
De sterkte van de wachtwoorden (sterk, matig, zwak) 

## Verbanden in en uitvoer
Het programma test elk ingevoerd wachtwoord op sterkte. 

## Beperkingen
De checks zijn niet heel sterk. Negatieve aantalen geven een probleem.   

## Voorbeelden
Verwachte invoer:
```
3
nietsterk
H3$lSt3rKenW8w0Rd
GematigdSterk
```
Verwachte uitvoer:
```
zwak
sterk
matig
```
Voorbeelden van ongeldige invoer
```
Aantal te testen wachtwoorden
-100

Process finished with exit code 0
```

## Ontwerp
De wachtwoorden worden aan de tand gevoeld met een paar simpele voorwaarden.   

## Pseudocode
```
wachtwoorden =[]

# gebruiker om wachtwoorden vragen met for-loop 

voor elk wachtwoord in wachtwoorden:
    score = 0 
    
    # voorwaardes zijn gedefineerd in de opracht, alsmede de scores
    if voorwaarde: 
        score += n 
    
    print(vertaal_score(score))

```

## Test
```
Aantal te testen wachtwoorden
3
Wachtwoord0
MiesTest
Wachtwoord1
Mrun34508UNF*#
Wachtwoord2
439gnrnjie((((
matig
sterk
sterk
```