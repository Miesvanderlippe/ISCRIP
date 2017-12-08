# Uitwerking opdracht
**Opdracht** Dronken mier

**Weeknummer** 4

**Studentnummer** S1096607

**Naam student** Mies van der Lippe

**Specialisatie** FICT

**Pogingnummer**1

## Vraagstelling
Zie : https://dodona.ugent.be/nl/exercises/276629077/

## Invoer
Geen

## Uitvoer
De genomen stappen om een situatie op te lossen in zowel een kaartje met positie
als coordinaten.  

## Verbanden in en uitvoer
Er is geen invoer.    

## Beperkingen
Als de functies verkeerd worden aangeroepen wordt dit niet afgevangen.   

## Voorbeelden
Verwachte invoer:
```
NaN
```
Verwachte uitvoer:
```
De velden met een pijl voor de mier
De posities als lijst [(1,2)]
```
Voorbeelden van ongeldige invoer
```
NaN
```

## Ontwerp
Ik zal kijken welke richting het spoor staat op een positie. Dan pas ik de 
coordinaten aan aan de hand van deze richting en pas de nieuwe coordinaten aan.
Daarna zal ik het oude spoor roteren.     

## Pseudocode
```
functie bekijkrichting(pijltje)
    geef richting terug

functie zoekpijl(veld, positie)
    zoek pijl op en geef deze terug

functie stap(veld, positie)
    pijl = zoekpijl(veld, positie)
    richting = bekijkrichting(pijl)
    
    positie = nieuwe_positie # afhankelijk van richting. 
    
functie stappen()
    zolang de positie niet het doel is 
        nieuwe positie = stap
        
    geef veld en positie terug

```

## Test
```
> > > >
^ < ^ v
^ v ^ ^
🢂 > v >
-------
> > > >
^ < ^ v
^ v ^ ^
v 🢂 v >
-------
> > > >
^ < ^ v
^ v ^ ^
v v 🢃 >
-------
> > > >
^ < ^ v
^ v ^ ^
v v 🢀 >
-------
> > > >
^ < ^ v
^ v ^ ^
v 🢃 ^ >
-------
> > > >
^ < ^ v
^ v ^ ^
v 🢀 ^ >
-------
> > > >
^ < ^ v
^ v ^ ^
🢃 ^ ^ >
-------
> > > >
^ < ^ v
^ v ^ ^
🢀 ^ ^ >
-------
> > > >
^ < ^ v
^ v ^ ^
🢁 ^ ^ >
-------
> > > >
^ < ^ v
🢁 v ^ ^
> ^ ^ >
-------
> > > >
🢁 < ^ v
> v ^ ^
> ^ ^ >
-------
🢂 > > >
> < ^ v
> v ^ ^
> ^ ^ >
-------
v 🢂 > >
> < ^ v
> v ^ ^
> ^ ^ >
-------
v v 🢂 >
> < ^ v
> v ^ ^
> ^ ^ >
-------
v v v 🢂
> < ^ v
> v ^ ^
> ^ ^ >
[(3, 0), (3, 1), (3, 2), (3, 2), (3, 1), (3, 1), (3, 0), (3, 0), (3, 0), (2, 0), (1, 0), (0, 0), (0, 1), (0, 2), (0, 3)]
```