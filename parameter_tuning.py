from charles import Population
from selection import tournament, roulette_wheel, rank
from mutation import swap_mutation, inversion_mutation, scramble_mutation
from crossover import single_point_crossover, multi_point_crossover, uniform_crossover
import numpy as np
from main import load_sudoku


selection_methods = {'tournament':tournament, 'roulette':roulette_wheel, 'rank':rank}
mutation_methods = {'swap':swap_mutation, 'inversion':inversion_mutation, 'scramble':scramble_mutation}
crossover_methods = {'single_point':single_point_crossover, 'multi_point':multi_point_crossover, 'uniform':uniform_crossover}

for mut_p in [0.1,0.2,0.3,0.4,0.5,0.6,0.7,0.8,0.9]:
    for cross_p in [0.1,0.2,0.3,0.4,0.5,0.6,0.7,0.8,0.9]:
        if __name__ == '__main__':
            problem = load_sudoku("problem.txt")
            arr = np.array(problem)

            # running each combination of methods several times in order to calculate an average
            for _ in range(10):         
                pop = Population(
                    size=20,
                    full_array = arr,
                    replacement=False,
                    filename = 'mutation-'+ str(mut_p) + '_'+ 'crossover-'+ str(cross_p),  
                    folder=r"PT_", #parameter tunning
                    optim="max"
                )

                pop.evolve(gens = 30,
                        select = tournament,
                        crossover = single_point_crossover,
                        mutate = swap_mutation,
                        co_p = cross_p,
                        mu_p= mut_p,
                        elitism=False,
                        full_array_evolve=arr,
                        log = True)
