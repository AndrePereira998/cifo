# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.


from cgitb import text
from random import randint
from tabnanny import check
import numpy as np

from charles import Population

from charles import Population, Individual
#from charles.search import hill_climb, sim_annealing
from copy import deepcopy
#from data.ks_data import weights, values, capacity
from selection import roulette_wheel, tournament
from mutation import scramble_mutation, swap_mutation, inversion_mutation
from crossover import single_point_crossover,multi_point_crossover,uniform_crossover
from random import random
from operator import attrgetter



def load_sudoku(txt):     
    my_file = open(txt, "r")
    text = my_file.read()
    problem = text.split(" ")
    problem = list(map(int, problem))
    my_file.close()
    return problem

def solution_gen(number, problem): 
    """ function generating solutions from the initial array 'problem' """
    solutions = []
    problem_aux = problem

    for i in range(number): 
        problem_aux = problem
        for pos,value in enumerate(problem):   # for each '0' in the array we will create a random number between 1 and 9
            if value == 0: 
                problem_aux[pos] = randint(1,9)
        solutions.append(problem_aux)    # an array with all the numbers that were generated 
    return solutions     

def before_fitness(full_array, solutions): 
    """ function merging the solution and problem array in order to check the fitness of the solution """
    sol_pos = 0
    for pos, value in enumerate(full_array):
        if value == 0:    # every '0' of the problem array will be replace with the corresponding digit from the solution array
            full_array[pos] = solutions[sol_pos]
            sol_pos += 1
    return full_array   



                
# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    problem = load_sudoku("problem.txt")
    #solutions = solution_gen(5,problem)
    #print(solutions)
    #problem = [8,2,7,1,5,4,3,9,6,9,6,5,3,2,7,1,4,8,3,4,1,6,8,9,7,5,2,5,9,3,4,6,8,2,7,1,4,7,2,5,1,3,6,8,9,6,1,8,9,7,2,4,3,5,7,8,6,2,3,5,9,1,4,1,5,4,7,9,6,8,2,3,2,3,9,8,4,1,5,6,7]
    arr = np.array(problem)

    pop = Population(
        size=500,
        full_array = arr,
        replacement=False,
        optim="max",
    )

    print(pop)

    for selection in [tournament, roulette_wheel]:
        pop.evolve(gens=10,
            select=selection,
            crossover=single_point_crossover,
            mutate=swap_mutation,
            co_p=0.9, mu_p=0.1,
            elitism=False,
            full_array_evolve=arr)
    print('cross')
    for crossovering in [uniform_crossover]:
        pop.evolve(gens=10,
            select=tournament,
            crossover=crossovering,
            mutate=swap_mutation,
            co_p=0.9, mu_p=0.1,
            elitism=False,
            full_array_evolve=arr)

    for mutating in [scramble_mutation, swap_mutation, inversion_mutation]:
            print(mutating)
            pop.evolve(gens=10,
                select=tournament,
                crossover=single_point_crossover,
                mutate=mutating,
                co_p=0.9, mu_p=0.1,
                elitism=False,
                full_array_evolve=arr)



    

    #before_fitness(problem, solutions)




# See PyCharm help at https://www.jetbrains.com/help/pycharm/
