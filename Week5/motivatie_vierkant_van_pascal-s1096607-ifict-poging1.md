# Uitwerking opdracht
**Opdracht** Vierkant van Pascal

**Weeknummer** 5

**Studentnummer** S1096607

**Naam student** Mies van der Lippe

**Specialisatie** FICT

**Pogingnummer**1

## Vraagstelling
Zie : https://dodona.ugent.be/nl/exercises/1799377797/

## Invoer
De gebruiker kiest hoe groot het vierkant moet worden en welk getal er op de 
kantlijn gezet zal worden.  

## Uitvoer
Een vierkant van Pascal  

## Verbanden in en uitvoer
De gebruiker bepaalt het formaat en het basisgetal voor het vierkant.     

## Beperkingen
Als de getallen in het vierkant langer worden dan 8 cijfers komt het vierkant 
niet uit. 

## Voorbeelden
Verwachte invoer:
```
Hoe groot wilt u het vierkant?
5
Wel getal wilt u als basis getal gebruiken?
10
```
Verwachte uitvoer:
```
      10      10      10      10      10
      10      20      30      40      50
      10      30      60     100     150
      10      40     100     200     350
      10      50     150     350     700
```
Voorbeelden van ongeldige invoer
```
Hoe groot wilt u het vierkant?
15
Wel getal wilt u als basis getal gebruiken?
9
       9       9       9       9       9       9       9       9       9       9       9       9       9       9       9
       9      18      27      36      45      54      63      72      81      90      99     108     117     126     135
       9      27      54      90     135     189     252     324     405     495     594     702     819     945    1080
       9      36      90     180     315     504     756    1080    1485    1980    2574    3276    4095    5040    6120
       9      45     135     315     630    1134    1890    2970    4455    6435    9009   12285   16380   21420   27540
       9      54     189     504    1134    2268    4158    7128   11583   18018   27027   39312   55692   77112  104652
       9      63     252     756    1890    4158    8316   15444   27027   45045   72072  111384  167076  244188  348840
       9      72     324    1080    2970    7128   15444   30888   57915  102960  175032  286416  453492  697680 1046520
       9      81     405    1485    4455   11583   27027   57915  115830  218790  393822  680238 1133730 1831410 2877930
       9      90     495    1980    6435   18018   45045  102960  218790  437580  831402 1511640 2645370 4476780 7354710
       9      99     594    2574    9009   27027   72072  175032  393822  831402 1662804 3174444 58198141029659417651304
       9     108     702    3276   12285   39312  111384  286416  680238 1511640 3174444 6348888121687022246529640116600
       9     117     819    4095   16380   55692  167076  453492 1133730 2645370 581981412168702243374044680270086919300
       9     126     945    5040   21420   77112  244188  697680 1831410 447678010296594224652964680270093605400180524700
       9     135    1080    6120   27540  104652  348840 1046520 2877930 7354710176513044011660086919300180524700361049400
```

## Ontwerp
Ik zal een functie maken om het omzetten van cijfers naar N seperatoren te 
faciliteren. Dan is het decoderen van een Fosyth notatie een eitje. Het 
encoderen zal ik gewoon doen met een reeks string replacements. 

## Pseudocode
```
functie vierkantje
    maak een rij van breedte n 
    voor elke rij die we gaan maken 
        kijk naar de cel links van de huidige cel 
            tel daar de cel erboven bij op 
        voeg rij toe aan resultaat
    geef resultaat terug
```

## Test
```
Hoe groot wilt u het vierkant?
6
Wel getal wilt u als basis getal gebruiken?
9
       9       9       9       9       9       9
       9      18      27      36      45      54
       9      27      54      90     135     189
       9      36      90     180     315     504
       9      45     135     315     630    1134
       9      54     189     504    1134    2268
```
```
Hoe groot wilt u het vierkant?
8
Wel getal wilt u als basis getal gebruiken?
8
       8       8       8       8       8       8       8       8
       8      16      24      32      40      48      56      64
       8      24      48      80     120     168     224     288
       8      32      80     160     280     448     672     960
       8      40     120     280     560    1008    1680    2640
       8      48     168     448    1008    2016    3696    6336
       8      56     224     672    1680    3696    7392   13728
       8      64     288     960    2640    6336   13728   27456
```