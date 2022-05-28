from cgitb import text
from random import randint
from tabnanny import check
import numpy as np
from charles import Population
from charles import Population, Individual
from copy import deepcopy
from selection import roulette_wheel, tournament, rank
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
    arr = np.array(problem)

    pop = Population(
        size=500,
        full_array = arr,
        replacement=False,
        optim="max",
    )

    for selection in [tournament, roulette_wheel]:
        pop.evolve(gens=10,
            select=selection,
            crossover=single_point_crossover,
            mutate=swap_mutation,
            co_p=0.9, mu_p=0.1,
            elitism=False,
            full_array_evolve=arr)

    for crossovering in [uniform_crossover]:
        pop.evolve(gens=10,
            select=tournament,
            crossover=crossovering,
            mutate=swap_mutation,
            co_p=0.9, mu_p=0.1,
            elitism=False,
            full_array_evolve=arr)

    for mutating in [scramble_mutation, swap_mutation, inversion_mutation]:

            pop.evolve(gens=10,
                select=tournament,
                crossover=single_point_crossover,
                mutate=mutating,
                co_p=0.9, mu_p=0.1,
                elitism=False,
                full_array_evolve=arr)
