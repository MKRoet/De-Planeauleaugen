# De Planeauleaugen - AmstelHaege

Heuristieken, Universiteit van Amsterdam

## De opdracht

Lever een plattegrond (2D of 3D) af voor ieder van de drie huizenvarianten voor de nieuw te bouwen wijk Amstelhaege. De scores voor een plattegrond is de opgetelde waarde van alle huizen in de wijk.
[Heuristieken/AmstelHaege](http://heuristieken.nl/wiki/index.php?title=Amstelhaege)

### Uitwerking opdracht

Elk huis op de plattegrond heeft een eigen waarde, waarvan de eengezinswoning de laagste, en de maison de hoogste. Ook elke meter extra vrijstand levert extra waarde op.
Deze code genereert een plattegrond (met 20, 40 of 60 huizen), die op een bepaalde manier wordt ingedeeld, met als doel het berekenen van een zo hoog mogelijke score.
Hiervoor worden algoritmes als random, hillclimber en simulated annealing gebruikt. Deze algoritmes kijken of een huis een andere plaats in kan nemen, en of zo de waarde van de plattegrond hoger wordt. Als dit het geval is, moet deze staat worden opgeslagen. 

### Wat heb je nodig

Zorg dat je python 3 gebruikt en de volgende onderdelen zijn geïnstalleerd:
- matplotlib
- numpy

## Programma runnen

Hoe werkt het programma?

$ python main.py [aantal huizen] [aantal runs] [algoritme]

- aantal huizen: 20, 40 of 60
- aantal runs: hoe vaak moet het programma draaien ('1' is in dit geval genoeg)
- algoritme: kies welk algoritme gebruikt moet worden (keuze uit: random, hillclimber, hillclimberswap of simulatedannealer)

Voer op de command line bijvoorbeeld het volgende in: python main.py 20 1 hillclimber

De plattegrond wordt middels matplotlib gegenereerd. Deze is te zien bij gebruik van het random-algoritme in dezelfde map als waarin het programma staat opgeslagen.

## Auteurs

* **Jet van den Berg**
* **Maurice Roet**
* **Chantal Stangenberger**
