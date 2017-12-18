#-------------------------------------------------------------------------------
# File name: main.py
#
# Authors: Jet van den Berg, Maurice Roet, Chantal Stangenberger
#
# Course: Heuristics
#
# This file prompt the user for how many houses, which algorithm, how many runs
# of the algorithm and the amount of iterations should be used to generate the
# different floor plans. After the specification of the desired algorithm, the
# specific algorithm will be called from algorithms.py
#-------------------------------------------------------------------------------

from Data_structure.objectclasses import *
import Algorithms.algorithms
import sys

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
        print("Choose amount of iterations, for the random algorithm you can choose 0")
        exit()

    # Calls the specific algorithm function from algorithms.py, which corresponds
    # to the user input.
    if algorithm == "random":
        Algorithms.algorithms.RandomAlgorithm(total_houses, runs_algorithm)
    elif algorithm == "hillclimber":
        Algorithms.algorithms.HillClimber(total_houses, runs_algorithm,\
            amount_iterations)
    elif algorithm == "simulated-annealing":
        Algorithms.algorithms.SimulatedAnnealing(total_houses, runs_algorithm,\
            amount_iterations)

if __name__ == '__main__':
    main()
