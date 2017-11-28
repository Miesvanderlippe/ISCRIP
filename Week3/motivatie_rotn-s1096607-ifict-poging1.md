# Uitwerking opdracht
**Opdracht** Caesarrotatie

**Weeknummer** 3

**Studentnummer** S1096607

**Naam student** Mies van der Lippe

**Specialisatie** FICT

**Pogingnummer**1

## Vraagstelling
Zie : https://dodona.ugent.be/nl/exercises/105361566/

## Invoer
Het programma vraagt of de gebruiker wil encoderen of decoderen, wat het bericht
is en hoeveel plekken er verschoven moet worden.  

## Uitvoer
Het versleutelde- of ontsleutelde bericht. 

## Verbanden in en uitvoer
Het bericht wordt versleuteld of ontsleuteld met de shift die door de gebruiker
ingevoert is. 

## Beperkingen
Speciale karakters kunnen niet ge-encodeerd worden.  

## Voorbeelden
Verwachte invoer:
```
Encode(e) of decode (d)?
e
Bericht:
Hey dit is mijn documentatie
Shift:
20
```
Verwachte uitvoer:
```
Bys xcn cm gcdh xiwogyhnuncy
```
Voorbeelden van ongeldige invoer

ongeldige invoer is niet echt mogelijk. Er wordt alleen gecontroleerd of het 
eerste antwoord 'e' van encode is. De rest is niet gevoelig. 

## Ontwerp
Ik gebruik de index in de ascii strings (lowercase, uppercase) waarbij ik een 
shift optel of aftrek, die doe ik modulo 26 en gebruik ik weer als index op 
dezelfde strings.  

## Pseudocode
```
def versleutel_letter(letter, shift)
    nieuwe_index = (ascii_uppercase.index(letter) + shift) % 26
    return ascii_uppercase[nieuwe_index]
    
resultaat = ""
for letter in string: 
    resultaat += versleutel_letter(letter)
```

## Test
```

Encode(e) of decode (d)?
e
Bericht:
Hey dit is een test man 
Shift:
15
Wtn sxi xh ttc ithi bpc
```
```
Encode(e) of decode (d)?
d
Bericht:
Wtn sxi xh ttc ithi bpc
Shift:
15
Hey dit is een test man
```