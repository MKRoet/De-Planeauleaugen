#-------------------------------------------------------------------------------
# File name: main.py
#
# Authors: Jet van den Berg, Maurice Roet, Chantal Stangenberger
#
# Course: Heuristics
#
# This program creates a floor plan in which 20, 40 or 60 houses are placed.
# Uses the other file 'houseclasses.py' and algoritms.py to generate the
# necessary data.
#-------------------------------------------------------------------------------

import sys
from Data_structure.houseclasses import *
from copy import deepcopy
from Algorithms.algorithms import *

#-------------------------------------------------------------------------------

def main():
    # Command line arguments: which type of floor plan should be displayed,
    # which type of algorithm should be used, how many runs of the algorithm and
    # the amount of iterations in the algorithm.
    total_houses = int(sys.argv[1])
    if not total_houses in [20, 40, 60]:
        print("The amount of houses has to be 20, 40 or 60.")
        exit()
    algorithm = sys.argv[2]
    if not algorithm in ["random", "hillclimber", "simulated-annealing"]:
        print("Choose between 'random', 'hillclimber' or 'simulated-annealing'")
        exit()
    runs_algorithm = int(sys.argv[3])
    if runs_algorithm == 0:
        print("The algorithm must be run at least once.")
        exit()
    try:
        amount_iterations = int(sys.argv[4])
    except:
        print("Choose how many iterations you want, for the random algorithm you can choose 0")
        exit()

    if algorithm == "random":
        RandomAlgorithm(total_houses, runs_algorithm)
    elif algorithm == "hillclimber":
        HillClimber(total_houses, runs_algorithm, amount_iterations)
    elif algorithm == "simulated-annealing":
        SimulatedAnnealing(total_houses, runs_algorithm, amount_iterations)

if __name__ == '__main__':
    main()
