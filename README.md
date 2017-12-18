# De Planeauleaugen - AmstelHaege

Heuristieken, Universiteit van Amsterdam

## De opdracht

Lever een plattegrond (2D of 3D) af voor ieder van de drie huizenvarianten voor de nieuw te bouwen wijk Amstelhaege. De scores voor een plattegrond is de opgetelde waarde van alle huizen in de wijk.
Zie: [Heuristieken/AmstelHaege](http://heuristieken.nl/wiki/index.php?title=Amstelhaege)

### Uitwerking opdracht

Elk huis op de plattegrond heeft een eigen waarde, waarvan de eengezinswoning de laagste, en de maison de hoogste. Ook elke meter extra vrijstand levert extra waarde op.
Deze code genereert een plattegrond (met 20, 40 of 60 huizen), die op een bepaalde manier wordt ingedeeld, met als doel het berekenen van een zo hoog mogelijke score.
Hiervoor worden algoritmes als random, hillclimber en simulated annealing gebruikt. Deze algoritmes kijken of een huis een andere plaats in kan nemen, en of zo de waarde van de plattegrond hoger wordt. Als dit het geval is, moet deze staat worden opgeslagen. 

### Wat heb je nodig

Zorg dat je python 3 gebruikt en de volgende onderdelen zijn geïnstalleerd:
* matplotlib
* numpy
* tqdm

### Indeling github

Dit project is ingedeeld in verschillende mappen: 
* 'Algorithms' bevat de algoritmes.
* 'Data_structure' bevat de object classes (zoals huizen en water), methods van deze classes, en de plotmap-functie.
* 'Experimenten' bevat de grafieken van experimentaties van meerdere runs op een algoritme, met verschillende functies.
* 'Presentatie' bevat de presentatie over dit project.

## Programma runnen

Hoe werkt het programma?

$ python main.py [aantal huizen] [algoritme] [aantal runs] [aantal iteraties van algoritme]

* aantal huizen: 20, 40 of 60
* algoritme: kies welk algoritme gebruikt moet worden (keuze uit: random, hillclimber of simulated-annealing)
* aantal runs: hoe vaak moet het programma draaien ('1' is vaak geval genoeg, tenzij er gekeken moet worden naar gemiddelde van meerdere runs)
* aantal iteraties van algoritme: een getal naar keuze (vul voor het random algoritme '0' in)

Voer op de command line bijvoorbeeld het volgende in: python main.py 20 hillclimber 1 100

De plattegronden worden middels matplotlib gegenereerd. Deze zijn te zien in dezelfde map als waarin het programma staat opgeslagen:
* bij een random algoritme onder de naam: 'randomMap.png'
* bij een hill climber onder de naam: 'hillClimberMap0.png' (Let op dat wanneer het programma vaker dan één keer wordt gerund, de plattegronden een cijfer krijgen, overeenkomend met de runs van het algoritme).
* bij een simulated annealing onder de naam: 'simulatedAnnealingMap0.png'. (Let op dat wanneer het programma vaker dan één keer wordt gerund, de plattegronden een cijfer krijgen, overeenkomend met de runs van het algoritme).

## Auteurs

* **Jet van den Berg**
* **Maurice Roet**
* **Chantal Stangenberger**
