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
De tekst die omgezet moet worden naar T9 toetsen 

## Uitvoer
De cijfers zoals op het T9 toetsenbord.  

## Verbanden in en uitvoer
De tekst word letter per letter omgezet naar cijfers op een T9 toetsenbord.  

## Beperkingen
Alleen letters binnen het alfabet worden geacapteerd, de rest wordt een 0. Dit
klopt in principe voor punten en spaties maar niet voor getallen.  

## Voorbeelden
Verwachte invoer:
```
Voer uw tekst in:
Dit is de documentatie voor de Tee Negen opdracht
```
Verwachte uitvoer:
```
3480470330362863682843086670330833063436067372248
```
Voorbeelden van ongeldige invoer
```
Voer uw tekst in:
--40404040---43-934$$$%
00000000000000000000000
```

## Ontwerp
Er wordt per letter gekeken naar de positie op het toetsenbord.    

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
Voer uw tekst in:
DIt is de TNegenTest
34804703308634368378
```