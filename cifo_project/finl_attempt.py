from charles import Population
from selection import tournament, roulette_wheel, rank
from mutation import swap_mutation, inversion_mutation, scramble_mutation
from crossover import single_point_crossover, multi_point_crossover, uniform_crossover
import numpy as np
from main import load_sudoku
import timeit

start = timeit.default_timer()
selection_methods = {'tournament':tournament}
mutation_methods = {'swap':swap_mutation}
crossover_methods = {'multi_point':multi_point_crossover}


if __name__ == '__main__':
    problem = load_sudoku("problem_hard.txt")
    arr = np.array(problem)

    # running each combination of methods several times in order to calculate an average
    for _ in range(10): 
        pop = Population(
            size=1000,
            full_array = arr,
            replacement=True,
            filename = 'final', 
            folder=r"final", 
            optim="max"
        )

        pop.evolve(gens=1500,
                select = tournament,
                crossover = multi_point_crossover,
                mutate = swap_mutation,
                co_p = 0.9,
                mu_p= 0.9,
                elitism=True,
                conv_param=[500,200,100],
                full_array_evolve=arr,
                log = True)

stop = timeit.default_timer()

print('Time: ', stop - start)  